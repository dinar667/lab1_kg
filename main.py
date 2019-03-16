# coding: utf-8

import sys

from PyQt5 import QtWidgets

from gui.main_window import MainWindow


class PointInSpace:
    def __init__(self):
        self.main_window = MainWindow()

    def run(self):
        if self.main_window:
            self.main_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)

    ps = PointInSpace()
    ps.run()

    app.exec()


if __name__ == '__main__':
    main()
