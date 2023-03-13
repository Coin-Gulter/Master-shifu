from PyQt5.QtWidgets import QDialog, QListWidget, QLineEdit
from PyQt5 import QtCore


class ChildListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
                event.accept()
        else:
                event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
                event.setDropAction(QtCore.Qt.CopyAction)
                event.accept()
        else:
                event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
                event.setDropAction(QtCore.Qt.CopyAction)
                event.accept()

                links = []

                for url in event.mimeData().urls():
                        if url.isLocalFile():
                                links.append(str(url.toLocalFile()))

                self.addItems(links)
        else:
                event.ignore()

class ChildLineEdit(QLineEdit):
        focus_in_signal = QtCore.pyqtSignal()
        focus_out_signal = QtCore.pyqtSignal()

        def focusInEvent(self, event):
                super().focusInEvent(event)
                self.focus_in_signal.emit()

        def focusOutEvent(self, event):
                super().focusOutEvent(event)
                self.focus_out_signal.emit()

class ChildDialog(QDialog):

        window_closing = QtCore.pyqtSignal()

        def closeEvent(self, event):
               self.window_closing.emit()
