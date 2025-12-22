import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from ui_form.login import LoginForm
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets


class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginForm()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    pixmap = QtGui.QPixmap("assets/images/logo.png")
    splash =QtWidgets.QSplashScreen(pixmap)
    splash.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    splash.show()

    def show_login():
        splash.close()
        login.show()

    QtCore.QTimer.singleShot(5000, show_login)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()