#!/bin/env python3

from PySide6 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
import pyzbar, sys


class Frontend(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # --- Main Window ---
        # TBD


        
        # --- Viewfinder Window---

        self.setWindowTitle("Barcode Scanner")
        self.mediaSession = QtMultimedia.QMediaCaptureSession()
        self.webcam = QtMultimedia.QCamera()
        self.viewFinder = QtMultimediaWidgets.QVideoWidget()
        self.mediaSession.setCamera(self.webcam)
        self.mediaSession.setVideoOutput(self.viewFinder)
        self.viewFinder.show()
        self.webcam.start()

        # --- Clicked button commands ---
        #self.cameraButton.clicked.connect(self.webcam())

        # --- Layout ----

        @QtCore.Slot()
        def webcam(self):
            pass

        def listCam(self):
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = Frontend()
    sys.exit(app.exec())
