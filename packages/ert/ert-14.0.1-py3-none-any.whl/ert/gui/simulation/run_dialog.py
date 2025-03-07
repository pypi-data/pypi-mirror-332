from __future__ import annotations

import logging
from pathlib import Path
from queue import SimpleQueue
from typing import cast

from PyQt6.QtCore import QModelIndex, QSize, Qt, QThread, QTimer
from PyQt6.QtCore import pyqtSignal as Signal
from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtGui import QMouseEvent, QMovie, QTextCursor, QTextOption
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMessageBox,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QSplitter,
    QTableView,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from _ert.threading import ErtThread
from ert.config import QueueSystem
from ert.ensemble_evaluator import (
    EndEvent,
    EvaluatorServerConfig,
    FullSnapshotEvent,
    SnapshotUpdateEvent,
)
from ert.ensemble_evaluator import identifiers as ids
from ert.gui.ertnotifier import ErtNotifier
from ert.gui.ertwidgets.message_box import ErtMessageBox
from ert.gui.model.fm_step_list import FMStepListProxyModel
from ert.gui.model.node import IterNode
from ert.gui.model.real_list import RealListModel
from ert.gui.model.snapshot import (
    FM_STEP_COLUMNS,
    FileRole,
    IterNum,
    RealIens,
    SnapshotModel,
)
from ert.gui.tools.file import FileDialog
from ert.run_models import (
    BaseRunModelAPI,
    RunModelStatusEvent,
    RunModelTimeEvent,
    RunModelUpdateBeginEvent,
    RunModelUpdateEndEvent,
    StatusEvents,
)
from ert.run_models.event import RunModelDataEvent, RunModelErrorEvent
from ert.shared.status.utils import (
    byte_with_unit,
    file_has_content,
    format_running_time,
    get_mount_directory,
)

from ..find_ert_info import find_ert_info
from .queue_emitter import QueueEmitter
from .view import DiskSpaceWidget, ProgressWidget, RealizationWidget, UpdateWidget

_TOTAL_PROGRESS_TEMPLATE = "Total progress {total_progress}% — {iteration_label}"


class FMStepOverview(QTableView):
    def __init__(self, snapshot_model: SnapshotModel, parent: QWidget | None) -> None:
        super().__init__(parent)

        self._fm_step_model = FMStepListProxyModel(self, 0, 0)
        self._fm_step_model.setSourceModel(snapshot_model)

        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.clicked.connect(self._fm_step_clicked)
        self.setModel(self._fm_step_model)

        horizontal_header = self.horizontalHeader()
        assert horizontal_header is not None

        horizontal_header.resizeSections(QHeaderView.ResizeMode.ResizeToContents)
        for section in range(horizontal_header.count()):
            if horizontal_header.sectionSize(section) < 135:
                horizontal_header.resizeSection(section, 135)

            # Only last section should be stretch
            horizontal_header.setSectionResizeMode(
                section,
                QHeaderView.ResizeMode.Stretch
                if section == horizontal_header.count() - 1
                else QHeaderView.ResizeMode.Interactive,
            )

        vertical_header = self.verticalHeader()
        assert vertical_header is not None
        vertical_header.setMinimumWidth(20)
        self.setMinimumHeight(140)
        self.setMouseTracking(True)

    @Slot(int, int)
    def set_realization(self, iter_: int, real: int) -> None:
        self._fm_step_model.set_real(iter_, real)

    @Slot(QModelIndex)
    def _fm_step_clicked(self, index: QModelIndex) -> None:
        if not index.isValid():
            return
        selected_file = index.data(FileRole)
        file_dialog = self.findChild(QDialog, name=selected_file)
        if file_dialog and file_dialog.isVisible():
            file_dialog.raise_()
        elif selected_file and file_has_content(selected_file):
            fm_step_name = index.siblingAtColumn(0).data()
            FileDialog(
                selected_file,
                fm_step_name,
                index.row(),
                index.data(RealIens),
                index.data(IterNum),
                self,
            )
        elif FM_STEP_COLUMNS[index.column()] == ids.ERROR and index.data():
            error_dialog = QDialog(self)
            error_dialog.setWindowTitle("Error information")
            layout = QVBoxLayout(error_dialog)

            error_textedit = QPlainTextEdit()
            error_textedit.setReadOnly(True)
            error_textedit.setWordWrapMode(QTextOption.WrapMode.NoWrap)
            error_textedit.appendPlainText(index.data())
            layout.addWidget(error_textedit)

            dialog_button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
            dialog_button.accepted.connect(error_dialog.accept)
            layout.addWidget(dialog_button)
            error_dialog.resize(700, 300)
            error_textedit.moveCursor(QTextCursor.MoveOperation.Start)
            error_dialog.exec()

    def mouseMoveEvent(self, e: QMouseEvent | None) -> None:
        if e:
            index = self.indexAt(e.pos())
            if index.isValid():
                data_name = FM_STEP_COLUMNS[index.column()]
                if data_name in {ids.STDOUT, ids.STDERR} and file_has_content(
                    index.data(FileRole)
                ):
                    self.setCursor(Qt.CursorShape.PointingHandCursor)
                else:
                    self.setCursor(Qt.CursorShape.ArrowCursor)

        return super().mouseMoveEvent(e)


class RunDialog(QFrame):
    simulation_done = Signal(bool, str)
    progress_update_event = Signal(dict, int)
    _RUN_TIME_POLL_RATE = 1000

    def __init__(
        self,
        config_file: str,
        run_model_api: BaseRunModelAPI,
        event_queue: SimpleQueue[StatusEvents],
        notifier: ErtNotifier,
        parent: QWidget | None = None,
        output_path: Path | None = None,
    ):
        super().__init__(parent)
        self.output_path = output_path
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowFlags(Qt.WindowType.Window)
        self.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint, False)
        self.setWindowTitle(f"Experiment - {config_file} {find_ert_info()}")

        self._run_model_api = run_model_api
        self._queue_system = run_model_api.queue_system
        self._snapshot_model = SnapshotModel(self)
        self._event_queue = event_queue
        self._notifier = notifier
        self.fail_msg_box: ErtMessageBox | None = None

        self._ticker = QTimer(self)
        self._ticker.timeout.connect(self._on_ticker)

        self._total_progress_label = QLabel(
            _TOTAL_PROGRESS_TEMPLATE.format(
                total_progress=0, iteration_label="Starting..."
            ),
            self,
        )

        self._total_progress_bar = QProgressBar(self)
        self._total_progress_bar.setRange(0, 100)
        self._total_progress_bar.setTextVisible(False)

        self._iteration_progress_label = QLabel(self)
        self._progress_widget = ProgressWidget()

        self._tab_widget = QTabWidget(self)
        self._tab_widget.setMinimumHeight(250)
        self._tab_widget.currentChanged.connect(self._current_tab_changed)
        self._snapshot_model.rowsInserted.connect(self.on_snapshot_new_iteration)

        self._fm_step_label = QLabel(self)
        self._fm_step_label.setObjectName("fm_step_label")
        self._fm_step_overview = FMStepOverview(self._snapshot_model, self)

        self.running_time = QLabel("")
        self.memory_usage = QLabel("")
        self.disk_space = DiskSpaceWidget(
            get_mount_directory(self._run_model_api.runpath_format_string)
        )

        self.kill_button = QPushButton("Terminate experiment")
        self.restart_button = QPushButton("Rerun failed")
        self.restart_button.setHidden(True)

        size = 20
        spin_movie = QMovie("img:loading.gif")
        spin_movie.setSpeed(60)
        spin_movie.setScaledSize(QSize(size, size))
        spin_movie.start()

        self.processing_animation = QLabel()
        self.processing_animation.setFixedSize(QSize(size, size))
        self.processing_animation.setMovie(spin_movie)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.processing_animation)
        button_layout.addWidget(self.running_time)
        button_layout.addStretch()
        button_layout.addWidget(self.memory_usage)
        button_layout.addStretch()
        button_layout.addWidget(self.disk_space)
        button_layout.addStretch()
        button_layout.addWidget(self.kill_button)
        button_layout.addWidget(self.restart_button)

        button_widget_container = QWidget()
        button_widget_container.setLayout(button_layout)

        layout = QVBoxLayout()
        layout.addWidget(self._total_progress_label)
        layout.addWidget(self._total_progress_bar)
        layout.addWidget(self._iteration_progress_label)
        layout.addWidget(self._progress_widget)

        adjustable_splitter_layout = QSplitter()
        adjustable_splitter_layout.setOrientation(Qt.Orientation.Vertical)
        adjustable_splitter_layout.addWidget(self._tab_widget)

        adjustable_splitter_layout.setStyleSheet("""
            QSplitter::handle {
                image: url(img:drag_handle.svg);
                height: 13px;
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                   stop: 0.1 #10FFFFFF, stop: 0.5 #D3D3D3, stop: 0.9 #10FFFFFF);
            }
         """)

        self.fm_step_frame = QFrame(self)
        fm_step_frame_layout = QVBoxLayout(self.fm_step_frame)
        fm_step_frame_layout.setContentsMargins(0, 0, 0, 0)
        fm_step_frame_layout.addWidget(self._fm_step_label)
        fm_step_frame_layout.addWidget(self._fm_step_overview)

        adjustable_splitter_layout.addWidget(self.fm_step_frame)
        layout.addWidget(adjustable_splitter_layout)
        layout.addWidget(button_widget_container)

        self.setLayout(layout)

        self.kill_button.clicked.connect(self.killJobs)
        self.restart_button.clicked.connect(self.restart_failed_realizations)
        self.simulation_done.connect(self._on_simulation_done)

        self.setMinimumSize(1200, 600)
        self._restart = False
        self.flag_simulation_done = False

    def is_simulation_done(self) -> bool:
        return self.flag_simulation_done

    def _current_tab_changed(self, index: int) -> None:
        widget = self._tab_widget.widget(index)
        if isinstance(widget, RealizationWidget):
            widget.refresh_current_selection()

        self.fm_step_frame.setHidden(isinstance(widget, UpdateWidget))

    @Slot(QModelIndex, int, int)
    def on_snapshot_new_iteration(
        self, parent: QModelIndex, start: int, end: int
    ) -> None:
        if not parent.isValid():
            index = self._snapshot_model.index(start, 0, parent)
            iteration = cast(IterNode, index.internalPointer()).id_
            iter_row = start
            self._iteration_progress_label.setText(
                f"Progress for iteration {iteration}"
            )

            widget = RealizationWidget(iter_row)
            widget.setSnapshotModel(self._snapshot_model)
            widget.itemClicked.connect(self._select_real)
            self._select_real(widget._real_list_model.index(0, 0))
            tab_index = self._tab_widget.addTab(
                widget, f"Realizations for iteration {iteration}"
            )
            if self._tab_widget.currentIndex() == self._tab_widget.count() - 2:
                self._tab_widget.setCurrentIndex(tab_index)

    @Slot(QModelIndex)
    def _select_real(self, index: QModelIndex) -> None:
        if index.isValid():
            real = index.row()
            iter_ = cast(RealListModel, index.model()).get_iter()
            exec_hosts = None

            iter_node = self._snapshot_model.root.children.get(str(iter_), None)
            if iter_node:
                real_node = iter_node.children.get(str(real), None)
                if real_node:
                    exec_hosts = real_node.data.exec_hosts

            self._fm_step_overview.set_realization(iter_, real)
            text = f"Realization id {index.data(RealIens)} in iteration {index.data(IterNum)}"
            if exec_hosts and exec_hosts != "-":
                text += f", assigned to host: {exec_hosts}"
            self._fm_step_label.setText(text)

    def run_experiment(self, restart: bool = False) -> None:
        self._restart = restart
        self.flag_simulation_done = False
        if restart is False:
            self._snapshot_model.reset()
            self._tab_widget.clear()

        evaluator_server_config = EvaluatorServerConfig(
            use_ipc_protocol=self._queue_system == QueueSystem.LOCAL
        )

        def run() -> None:
            self._run_model_api.start_simulations_thread(
                evaluator_server_config=evaluator_server_config,
                restart=restart,
            )

        simulation_thread = ErtThread(
            name="ert_gui_simulation_thread", target=run, daemon=True
        )

        self._worker_thread = QThread(parent=self)

        self._worker = QueueEmitter(self._event_queue)
        self._worker.done.connect(self._worker_thread.quit)
        self._worker.new_event.connect(self._on_event)
        self._worker.moveToThread(self._worker_thread)

        self.destroyed.connect(lambda: _stop_worker(self._worker_thread, self._worker))

        self.simulation_done.connect(self._worker.stop)

        self._worker_thread.started.connect(self._worker.consume_and_emit)
        self._ticker.start(self._RUN_TIME_POLL_RATE)

        self._worker_thread.start()
        simulation_thread.start()
        self._notifier.set_is_simulation_running(True)

    def killJobs(self) -> QMessageBox.StandardButton:
        msg = "Are you sure you want to terminate the currently running experiment?"
        kill_job = QMessageBox.question(
            self,
            "Terminate experiment",
            msg,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if kill_job == QMessageBox.StandardButton.Yes:
            # Normally this slot would be invoked by the signal/slot system,
            # but the worker is busy tracking the evaluation.
            self._run_model_api.cancel()
        return kill_job

    @Slot(bool, str)
    def _on_simulation_done(self, failed: bool, msg: str) -> None:
        self.processing_animation.hide()
        self.kill_button.setHidden(True)
        self.restart_button.setVisible(self._run_model_api.has_failed_realizations())
        self.restart_button.setEnabled(self._run_model_api.support_restart)
        self._notifier.set_is_simulation_running(False)
        self.flag_simulation_done = True
        if failed:
            self.update_total_progress(1.0, "Failed")

            self._progress_widget.set_all_failed()

            self.fail_msg_box = ErtMessageBox("ERT experiment failed!", msg, self)
            self.fail_msg_box.setModal(True)
            self.fail_msg_box.show()
        else:
            self.update_total_progress(1.0, "Experiment completed.")
        for file_dialog in self.findChildren(FileDialog):
            file_dialog.close()

    @Slot()
    def _on_ticker(self) -> None:
        runtime = self._run_model_api.get_runtime()
        self.running_time.setText(format_running_time(runtime))

        maximum_memory_usage = self._snapshot_model.root.max_memory_usage

        self.disk_space.update_status()

        if maximum_memory_usage:
            self.memory_usage.setText(
                f"Maximal realization memory usage: {byte_with_unit(maximum_memory_usage)}"
            )

    @Slot(object)
    def _on_event(self, event: object) -> None:
        model = self._snapshot_model
        match event:
            case EndEvent(failed=failed, msg=msg):
                self.simulation_done.emit(failed, msg)
                self._ticker.stop()
            case FullSnapshotEvent(
                status_count=status_count, realization_count=realization_count
            ):
                if event.snapshot is not None:
                    if self._restart:
                        model._update_snapshot(event.snapshot, str(event.iteration))
                    else:
                        model._add_snapshot(event.snapshot, str(event.iteration))
                self.update_total_progress(event.progress, event.iteration_label)
                self._progress_widget.update_progress(status_count, realization_count)
                self.progress_update_event.emit(status_count, realization_count)
            case SnapshotUpdateEvent(
                status_count=status_count, realization_count=realization_count
            ):
                if event.snapshot is not None:
                    model._update_snapshot(event.snapshot, str(event.iteration))
                self._progress_widget.update_progress(status_count, realization_count)
                self.update_total_progress(event.progress, event.iteration_label)
                self.progress_update_event.emit(status_count, realization_count)
            case RunModelUpdateBeginEvent(iteration=iteration):
                widget = UpdateWidget(iteration)
                tab_index = self._tab_widget.addTab(widget, f"Update {iteration}")
                if self._tab_widget.currentIndex() == self._tab_widget.count() - 2:
                    self._tab_widget.setCurrentIndex(tab_index)
                widget.begin(event)
            case RunModelUpdateEndEvent():
                self._progress_widget.stop_waiting_progress_bar()
                self._get_update_widget(event.iteration).end(event)
                event.write_as_csv(self.output_path)
            case RunModelStatusEvent() | RunModelTimeEvent():
                self._get_update_widget(event.iteration).update_status(event)
            case RunModelDataEvent():
                self._get_update_widget(event.iteration).add_table(event)
                event.write_as_csv(self.output_path)
            case RunModelErrorEvent():
                self._get_update_widget(event.iteration).error(event)
                event.write_as_csv(self.output_path)

    def _get_update_widget(self, iteration: int) -> UpdateWidget:
        for i in range(self._tab_widget.count()):
            widget = self._tab_widget.widget(i)
            if isinstance(widget, UpdateWidget) and widget.iteration == iteration:
                return widget
        raise ValueError("Could not find UpdateWidget")

    def update_total_progress(
        self, progress_value: float, iteration_label: str
    ) -> None:
        progress = int(progress_value * 100)
        if not (0 <= progress <= 100):
            logger = logging.getLogger(__name__)
            logger.warning(f"Total progress bar exceeds [0-100] range: {progress}")
        self._total_progress_bar.setValue(progress)
        self._total_progress_label.setText(
            _TOTAL_PROGRESS_TEMPLATE.format(
                total_progress=progress, iteration_label=iteration_label
            )
        )

    def restart_failed_realizations(self) -> None:
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(
            "Note that workflows will only be executed on the restarted "
            "realizations and that this might have unexpected consequences."
        )
        msg.setWindowTitle("Restart failed realizations")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        msg.setObjectName("restart_prompt")
        result = msg.exec()

        if result == QMessageBox.StandardButton.Ok:
            self.restart_button.setVisible(False)
            self.kill_button.setVisible(True)
            self.run_experiment(restart=True)


# Cannot use a non-static method here as
# it is called when the object is destroyed
# https://stackoverflow.com/questions/16842955
def _stop_worker(worker_thread: QThread, worker: QueueEmitter) -> None:
    if worker_thread.isRunning():
        worker.stop()
        worker_thread.wait(3000)
    if worker_thread.isRunning():
        worker_thread.quit()
        worker_thread.wait(3000)
    if worker_thread.isRunning():
        worker_thread.terminate()
        worker_thread.wait(3000)
