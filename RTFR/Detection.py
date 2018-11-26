import sqlite3
import pymysql
import sys
import cv2
import os
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QStyle, QLabel
from PyQt5.uic import loadUi
from os.path import expanduser


class Record(QDialog):
    def __init__(self):
        super(Record,self).__init__()
        loadUi('mygui.ui',self)

        self.cap = cv2.VideoCapture(0)
        #self.cap = cv2.VideoCapture("3.mp4")
        self.image=None
        self.path=None



        self.snapButton.setStyleSheet("background-color: white; border: none;")
        icon = QIcon()
        icon.addPixmap(QPixmap("camera.png"))
        self.snapButton.setIcon(icon)
        self.snapButton.clicked.connect(self.capture)
        self.faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def insertOrUpdate(self,Id, Name, UID, Skills):
        db = pymysql.connect("localhost", "root", "root", "hrm")
        cursor = db.cursor()
        sql = "SELECT * FROM dataset WHERE ID=" + str(Id)
        cursor.execute(sql)
        isRecordExist = 0
        for row in cursor:
            print(row)
            isRecordExist = 1
        if isRecordExist == 1:
            sql = "UPDATE dataset SET Name = '" + str(Name) + "', UID = '" + str(UID) + "', Skills = '" + str(
                Skills) + "' WHERE ID=" + str(Id)
        else:
            sql = "INSERT INTO dataset(ID, UID, name, Skills) Values(" + str(Id) + ",'" + str(UID) + "','" + str(Name) + "','" + str(Skills) + "')"
        cursor.execute(sql)
        db.commit()
        db.close()



    def update_frame(self):
        ret,self.image=self.cap.read()
        self.image=cv2.flip(self.image,1)


        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            self.snapButton.setStyleSheet("background-color: green; border: none;")

            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        self.displayImage(self.image,1)


    def capture(self):
        self.snapButton.setStyleSheet("background-color: red; border: none;")
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.path = input_dir
        print(self.path)

        self.id = self.lineEdit_id.text()
        print(self.id)
        self.name = self.lineEdit_name.text()
        print(self.name)
        self.uid = self.lineEdit_uid.text()
        print(self.uid)
        self.skills = self.lineEdit_skills.text()
        print(self.skills)
        self.insertOrUpdate(self.id, self.name, self.uid, self.skills)
        print("inserted")

        self.count=0
        while (True):

            ret,img_frame = self.cap.read()

            gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            self.count += 1

            cv2.imwrite(os.path.join(self.path, "User." + str(self.id) + '.' + str(self.count) + ".jpg"), gray[y:y + h, x:x + w])
            #cv2.imwrite(os.path.join(self.path, "User." + str(self.id) + '.' + str(self.count) + ".jpg"),img_frame)

            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

            elif self.count > 49:
                break

        print("Dataset successfully created!!")



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
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Record()
    window.setWindowTitle('DataSet')
    window.show()
    sys.exit(app.exec())