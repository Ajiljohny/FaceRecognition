import sqlite3
import sys
import cv2
import os
import numpy as np
from PIL import Image
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QStyle, QLabel
from PyQt5.uic import loadUi
from os.path import expanduser


class Record(QDialog):
    def __init__(self):
        super(Record,self).__init__()
        loadUi('trainGUI.ui',self)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.image = None
        self.i=0
        self.selectButton.clicked.connect(self.selection)
        self.trainButton.clicked.connect(self.training)
        self.timer = QTimer(self)

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage=outImage.rgbSwapped()


        if window==1:
            self.label.setPixmap(QPixmap.fromImage(outImage))
            self.label.setScaledContents(True)

    def selection(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.path = input_dir
        self.folderLabel.setText(input_dir)

    def training(self):
        IDs, faces = self.getImagesWithID(self.path)
        self.recognizer.train(faces, IDs)
        self.recognizer.save('recognizer/trainningData.yml')
        self.label2.setText("Training Completed!")

    def getImagesWithID(self,path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L');
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            self.displayImage(faceNp, 1)

            #cv2.imshow("Training", faceNp)
        return np.array(IDs), faces

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Record()
    window.setWindowTitle('DataSet')
    window.show()
    sys.exit(app.exec())