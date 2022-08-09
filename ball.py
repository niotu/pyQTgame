import sys

from PyQt5.QtWidgets import QApplication

from ballform import BallForm


def main():
    app = QApplication(sys.argv)
    wnd = BallForm(None)
    wnd.showMaximized()
    app.exec()


if __name__ == "__main__":
    main()
