import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

class Tic(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(700,100,600,600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('user.png'))
        self.key_button()
        self.quit_button()
        self.show()
     
    def key_button(self):
        self.button = QPushButton('BTN', self)
        self.button.resize(60, 60)
        self.button.move(25, 15)
        self.button.clicked.connect(self.cliked_button)

    def quit_button(self):
        self.qbtn = QPushButton('Вихід', self)
        self.qbtn.clicked.connect(QApplication.instance().quit)
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(500, 500)

    def cliked_button(self):
        print('CLICK')
        self.button.move(50, 15)

    def closeEvent(self, event):
        close = QMessageBox.question(self,"Вийти","Ви впевнені?",QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # def key_button_9(self):
    #     for i in range(9):
    #         self.but[i] = self.button
    #         print(i)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    Tac = Tic()
    
    sys.exit(app.exec_())

