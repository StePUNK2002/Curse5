# Form implementation generated from reading ui file 'интерфейс.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox
import math
from matplotlib import pyplot as plt

"""
self.lineEdit   = h
self.lineEdit_2 = T
self.lineEdit_3 = a
self.lineEdit_4 = b
self.lineEdit_5 = c
self.lineEdit_6 = d
"""
xs = [] # лист точек x(t)
ts = [] # лист точек t
masser = []
x0 = 0
h = 0
T = 0
#Коэффициенты у функции
a = 0
b = 0
c = 0
d = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 150, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 190, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 240, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 0, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 20, 201, 51))
        self.label_8.setStyleSheet("border-image: url(:/newPrefix/func.png);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/func.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 70, 391, 161))
        self.label_10.setStyleSheet("border-image: url(:/newPrefix/шаг.jpg);")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/newPrefix/шаг.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 230, 201, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 260, 271, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовая работа"))
        self.label.setText(_translate("MainWindow", "Введите h"))
        self.label_2.setText(_translate("MainWindow", "Введите T"))
        self.label_3.setText(_translate("MainWindow", "Введите a"))
        self.label_4.setText(_translate("MainWindow", "Введите b"))
        self.label_5.setText(_translate("MainWindow", "Введите c"))
        self.label_6.setText(_translate("MainWindow", "Введите d"))
        self.label_7.setText(_translate("MainWindow", "Функция"))
        self.pushButton_2.setText(_translate("MainWindow", "Построить график x(t)"))
        self.pushButton_3.setText(_translate("MainWindow", "Построить график погрешности"))

    def funcX(self, x):
        """
        Подсчет и возврат значения функции
        :param x: точка
        :return: значение функции
        """""
        return (a * (x ** 2) / (b * (x ** 4) + 4 + math.sin(c * x))) * math.sin((d * x) / 2)
    def K1(self, m):
        return h*self.funcX(m)
    def K2(self, m):
        return h*self.funcX(m + (self.K1(m)/4 ))

    def countK(self,h, f):
        return (h * f)

    def funcBySteps(self, h, N, massiveFunc, massiveEr):
        h = int(h)
        N = int(N)
        x0 = 1
        xm = x0
        for i in range(0, int(N+1)):
            K1h = self.countK(h, self.funcX(xm))
            K1halfh = self.countK(h / 2, self.funcX(xm))
            K2h = self.countK(h, self.funcX(xm + K1h / 4))
            K2halfh = self.countK(h / 2, self.funcX(xm + K1halfh / 4))
            K3h = self.countK(h, self.funcX(xm - 189 * K1h / 800 + 729 * K2h / 800))
            K3halfh = self.countK(h / 2, self.funcX(xm - 189 * K1halfh / 800 + 729 * K2halfh / 800))
            K4h = self.countK(h, self.funcX(xm + 214 * K1h / 891 + K2h / 33 + 650 * K3h / 891))
            K4halfh = self.countK(h / 2, self.funcX(xm + 214 * K1halfh / 891 + K2halfh / 33 + 650 * K3halfh / 891))

            f = xm + K1h * 533 / 2106 + K3h * 800 / 1053 - K4h * 1 / 78
            fhalf = xm + K1halfh * 533 / 2106 + K3halfh * 800 / 1053 - K4halfh * 1 / 78

            massiveFunc.append(f)
            massiveEr.append(self.rungeForStep(f, fhalf))

            xm = f

    def rungeForStep(self, yH, yhalfH):
        """
        :param yH: значение функции при шаге h
        :param yhalfH: значение функции при шаге h/2
        :return: значение погрешности
        """

        return (abs((yH - yhalfH)) / 15)

    def graphXt(self):
        """
        Функция для получения точек и построения функций
        """
        """
        self.lineEdit   = h
        self.lineEdit_2 = T
        self.lineEdit_3 = a
        self.lineEdit_4 = b
        self.lineEdit_5 = c
        self.lineEdit_6 = d
        """
        try:
            global a
            global b
            global c
            global d
            h = float(self.lineEdit.text())
            T = int(self.lineEdit_2.text())
            a = float(self.lineEdit_3.text())
            b = float(self.lineEdit_4.text())
            c = float(self.lineEdit_5.text())
            d = float(self.lineEdit_6.text())
            if T < h:
                print("T < h")
                dialog = QMessageBox(parent=self, text="Шаг не может быть больше T")
                ret = dialog.exec()
            elif T < 0:
                print("T < 0")
                dialog = QMessageBox(parent=self, text="T не может быть меньше 0")
                ret = dialog.exec()
            else:
                N = T / h  # Узнаем число узловых точек
                for i in range(int(N + 1)):
                    ts.append(i * h)
                print(ts)
                self.funcBySteps(h, N, xs, masser) #пока не работает
                plt.plot(ts, xs,color='red', label="x(t)")
                plt.plot(ts, masser, color='blue', label="Погрешность")
                plt.legend(loc='lower right', frameon=False)
                plt.show()
                print("x(t)")
                print(xs)
                print("Рунге")
                print(masser)
                ts.clear()
                xs.clear()
                masser.clear()
        except ValueError:
            print("В одной из строк или в строках находится неверный формат данных")
            dialog = QMessageBox(parent=self, text="В одной из строк или в строках находится неверный формат данных")
            ret = dialog.exec()

    def graphRunge(self):
        """
        Функция для построения графика
        погрешности методом Рунге
        """


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pixmap = QPixmap('func.png')
        pixmap1 = QPixmap('шаг.jpg')
        self.label_8.setPixmap(pixmap)
        self.label_8.setScaledContents(True)
        self.label_10.setPixmap(pixmap1)
        self.label_10.setScaledContents(True)
        self.pushButton_2.clicked.connect(self.graphXt)
        self.pushButton_3.clicked.connect(self.graphRunge)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    p = MainWindow()
    p.show()
    sys.exit(app.exec())
