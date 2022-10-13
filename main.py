import math
import sys
import random as rnd
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.windowSize = (2000, 1300)
        self.rec = False
        self.kol = 1000000
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 70, self.windowSize[0], self.windowSize[1])
        self.setWindowTitle('Рисование')
        self.size = 1200
        self.rectangle()

    def paintEvent(self, event):
        if self.rec:
            qp = QPainter()
            qp.begin(self)
            self.draw_rectangle(qp)
            points = self.find_points()
            self.draw_points(qp, points)
            # self.rec = False
            qp.end()


    def draw_points(self, qp, points):
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('red'))
        qp.setPen(pen)
        for i in points:
            qp.drawPoint(*i)


    def find_points(self):
        ans = []
        a, b, c = 1, -1, 1
        while not ((a < 0 and b < 0 and c < 0) or (a > 0 and b > 0 and c > 0)):
            x0 = rnd.randint(0, self.windowSize[0])
            y0 = rnd.randint(0, self.windowSize[1])
            a = (self.p1[0] - x0) * (self.p2[1] - self.p1[1]) - (self.p2[0] - self.p1[0]) * (self.p1[1] - y0)
            b = (self.p2[0] - x0) * (self.p3[1] - self.p2[1]) - (self.p3[0] - self.p2[0]) * (self.p2[1] - y0)
            c = (self.p3[0] - x0) * (self.p1[1] - self.p3[1]) - (self.p1[0] - self.p3[0]) * (self.p3[1] - y0)

        ans.append((x0, y0))
        for i in range(self.kol):
            p = rnd.randint(1, 3)
            match p:
                case 1:
                    p = self.p1
                case 2:
                    p = self.p2
                case 3:
                    p = self.p3

            l = (min(x0, p[0]) + (max(x0, p[0]) - min(x0, p[0])) // 2, min(y0, p[1]) + (max(y0, p[1]) - min(y0, p[1])) // 2)
            ans.append(l)
            x0, y0 = l
        print(len(ans))
        return ans


    def draw_rectangle(self, qp):
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('red'))
        qp.setPen(pen)
        qp.drawPoint(*self.p1)
        qp.drawPoint(*self.p2)
        qp.drawPoint(*self.p3)

        # pen.setColor(QtGui.QColor('black'))
        # qp.setPen(pen)
        #
        # qp.drawLine(*(self.p1 + self.p2))
        # qp.drawLine(*(self.p2 + self.p3))
        # qp.drawLine(*(self.p1 + self.p3))

    def rectangle(self):
        self.p1 = (400, self.windowSize[1] - 150)
        self.p2 = (int(self.p1[0] + self.size * 0.5), int(self.p1[1] - self.size * 0.8660254))
        self.p3 = (self.p1[0] + self.size, self.p1[1])
        self.rec = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())