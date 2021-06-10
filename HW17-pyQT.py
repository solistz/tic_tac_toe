import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox 
from PyQt5.QtGui import QIcon

class Tic(QWidget):

    def __init__(self):
        super().__init__()
        self.button_arr = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ]
        self.width_window = 600.6
        self.height_window = 600
       
        self.initUI()

    def initUI(self):

        self.setGeometry(700,100,self.width_window,self.height_window)
        self.setWindowTitle('}{PECTIKI')
        self.setWindowIcon(QIcon('user.png'))
        self.key_button()
        
        self.show()


# Кніпочка
    def key_button(self):
        self.button_0 = QPushButton('BTN', self)
        # self.button.resize(self.w, self.h)
        # self.button_0.resize(200,100)
        self.resize_key_button()
        print('Button',self.width())

    def resize_key_button(self):
        w_r = int(round(self.width()/5))
        h_r = int(round(self.height()/3))
        w_m = int(round((self.width()/2)-(w_r/2)))
        h_m = int(round((self.height()/2)-(h_r/2)))

        self.button_0.resize(w_r,h_r)
        self.button_0.move(w_m, h_m)

# метод вказує розмір вікна
    def resizeEvent(self, event):
        print('test', self.height(), self.width())
        self.resize_key_button()
        return super(Tic, self).resizeEvent(event)

# # Кніпочка - Вихід
#     def quit_button(self):
#         self.qbtn = QPushButton('Вихід', self)
#         self.qbtn.clicked.connect(QApplication.instance().quit)
#         self.qbtn.resize(self.qbtn.sizeHint())
#         self.qbtn.move(500, 500)

# # Метод - вікно пепед закриттям програми
#     def closeEvent(self, event):
#         close = QMessageBox.question(self,"Вийти","Ви впевнені?",QMessageBox.Yes | QMessageBox.No)
#         if close == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    Tac = Tic()
    
    sys.exit(app.exec_())

