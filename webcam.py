#!/bin/env python3

from PySide6 import QtCore, QtQuick, QtWidgets, QtGui, QtMultimedia
import pyzbar, sys


class Frontend(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # --- Main Window ----
        self.setWindowTitle("Barcode Scanner")
        self.cameraButton = QtWidgets.QPushButton("Open Webcam")
        self.layout = QtWidgets.QVBoxLayout(self)


        # --- Clicked button commands ---
        #self.cameraButton.clicked.connect(self.webcam())
        
        # --- Display video ---
        self.webcam = QtMultimedia.QCameraDevice.id()
        self.video = QtMultimedia.QMediaCaptureSession.camera()
       # self.layout.addWidget(self.video_widget)


        # --- Layout ----
        self.layout.addWidget(self.video)

        @QtCore.Slot()
        def webcam(self):
            pass

        def listCam(self):
            pass

        # --- Check Availability of Webcam
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    print(Frontend.webcam)


    widget = Frontend()
    widget.resize(400,400)
    widget.show()
    sys.exit(app.exec())
