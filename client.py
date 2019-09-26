import threading
from datetime import datetime
from time import sleep

import requests
from PyQt5 import QtWidgets
from chatclient import Ui_MainWindow


class ClientApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.append('string')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ClientApp()
    window.show()
    app.exec_()
