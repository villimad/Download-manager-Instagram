import sys
from PyQt5 import QtWidgets
import design
from first import InstDWIMG
from pars_page import Profile
import os


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.download)

    def add(self):
        textboxValue = self.textEdit.toPlainText()
        self.listWidget.addItem(textboxValue)

    def delete(self):
        item = self.listWidget.takeItem(self.listWidget.currentRow())
        item = None

    def download(self):
        linkTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        print(linkTextList)

        p = len(linkTextList)
        for q1 in range(0, p, 1):
            g = linkTextList[q1]
            One = Profile(g)
            d = One.Pars()
            k = len(d)
            for q2 in range(0, k, 1):
                r = d[q2]
                r = r[:-1]
                r = r[1:]
                two = InstDWIMG(r)
                two.dw()
                pass
            pass


def main():
        app = QtWidgets.QApplication(sys.argv)
        window = ExampleApp()
        window.show()
        app.exec_()


if __name__ == '__main__':
    main()
