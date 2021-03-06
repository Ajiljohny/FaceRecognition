import sys
import sqlite3
from PyQt5 import QtCore

import numpy as np
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton,QListWidget,QListWidgetItem,QMessageBox
from PyQt5.uic import loadUi

ids = []


class Record(QDialog):
    def __init__(self):
        super(Record,self).__init__()
        loadUi('RecGUI.ui',self)

        self.faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.rec = cv2.face.LBPHFaceRecognizer_create()
        self.rec.read("recognizer/trainningData.yml")
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.cap = cv2.VideoCapture(0)
        self.listWidget.itemClicked.connect(self.Clicked)
        #self.cap = cv2.VideoCapture("3.mp4")
        self.image=None
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.face_Enabled = True

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)


    def update_frame(self):

        ret, self.image = self.cap.read()
        self.image = cv2.flip(self.image,1)
        if (self.face_Enabled):
           detected_image = self.detect_face(self.image)

           self.displayImage(detected_image, 1)
        #else:
            #self.displayImage(self.image, 1)

    def detect_face(self,img):

        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = self.faceDetect.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, conf = self.rec.predict(gray[y:y + h, x:x + w])
            if id not in ids:
                ids.append(id)
            if(conf<80):
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, str(id), (x+50, y + h + 50), self.font, 2, (0, 255, 0), 3)

                for x in ids:
                    print("ids:", x)

                    if (len(self.listWidget.findItems(str(x), QtCore.Qt.MatchExactly)) == 0):
                        self.listWidget.addItem(str(x))
                        self.listWidget.show()
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, "Unknown", (x -80, y + h + 50), self.font, 2, (0, 0, 255), 3)
            print(conf)

            if(id==1):
                self.label_2.setText("Welcome AJIL")




        return img

    def Clicked(self, item):
        #QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
        conn = sqlite3.connect("FaceBase1.db")
        cmd = "SELECT * FROM People WHERE ID =" + item.text()
        cursor = conn.execute(cmd)
        profile = None

        for row in cursor:
            profile = row
            print(profile)
            self.label_1.setText(str(profile[2]))
            self.label_2.setText(profile[1])
            self.label_3.setText(profile[3])
        conn.close()

    def displayImage(self, img, window=1):
            qformat = QImage.Format_Indexed8
            if len(img.shape) == 3:
                if img.shape[2] == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
            outImage = outImage.rgbSwapped()

            if window == 1:
                self.frameLabel.setPixmap(QPixmap.fromImage(outImage))
                self.frameLabel.setScaledContents(True)





if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Record()
    window.setWindowTitle('Recognition')
    window.show()

    sys.exit(app.exec())

