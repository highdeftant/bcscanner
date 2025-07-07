#!/bin/env python3

from PySide6 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
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
        self.mediaSession = QtMultimedia.QMediaCaptureSession()
        self.webcam = QtMultimedia.QCamera()
        self.videoWidget = QtMultimedia.QVideoWidget()
        self.mediaSession.setVideoOutput(self.videoWidget)



        # --- Layout ----
        self.layout.addWidget(self.videoWidget)

        @QtCore.Slot()
        def webcam(self):



            pass

        def listCam(self):
            pass

        # --- Check Availability of Webcam
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = Frontend()
    widget.resize(400,400)
    widget.show()
    sys.exit(app.exec())
