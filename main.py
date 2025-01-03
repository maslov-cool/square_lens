import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import QPoint, QRectF
from PyQt6.QtGui import QPainter, QPixmap, QImage, QTransform, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>900</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
    <horstretch>80</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Квадрат объектив 1</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>20</y>
      <width>181</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Показать</string>
    </property>
   </widget>
   <widget class="QWidget" name="formLayoutWidget">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>20</y>
      <width>351</width>
      <height>91</height>
     </rect>
    </property>
    <layout class="QFormLayout" name="formLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>side</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>coeff</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="lineEdit"/>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="lineEdit_2"/>
     </item>
     <item row="2" column="1">
      <widget class="QLineEdit" name="lineEdit_3"/>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>n</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.color = QColor(255, 0, 0)

        self.btn.clicked.connect(self.act)

        self.flag = False

    def act(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_square(qp)
            qp.end()
        self.flag = False

    def draw_square(self, qp):
        side = int(self.lineEdit.text())
        coeff = float(self.lineEdit_2.text())
        x, y = 50, 130
        qp.setPen(self.color)
        for i in range(int(self.lineEdit_3.text())):
            qp.drawRect(QRectF(x, y, side, side))
            DELTA = side * (1 - coeff) / 2
            side *= coeff
            x += DELTA
            y += DELTA


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exception = except_hook
    sys.exit(app.exec())
