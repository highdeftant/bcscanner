#!/bin/env python3

from PySide6 import QtCore, QtQuick, QtWidgets, QtGui
from PySide6.QtMultimedia import QMediaDevices, QCamera
import pyzbar, sys


class Frontend(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # --- Main Window ----
        self.setWindowTitle("Barcode Scanner")
        self.cameraButton = QtWidgets.QPushButton("Open Webcam")


        # --- Clicked button commands ---
        self.cameraButton.clicked.connect(self.openCamera)
        
        # --- Display video ---
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)


        # --- Layout ----
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self)

        @QtCore.Slot()
        def webcam(self):
            pass

        def listCam():
            pass

        # --- Check Availability of Webcam
        def check_cam():
            if QMediaDevices.videoInputs().count() > 0:
                return True
            else:
                return False

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = Frontend()
    widget.resize(400,400)
    wiget.show()
    sys.exit(app.exec())
