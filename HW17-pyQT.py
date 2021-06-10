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
        self.width_window = 600
        self.height_window = 600
        # self.width_resize_button = int(round(self.width()/3))
        # self.height_resize_button = int(round(self.height()/3))
       
        self.initUI()

    def initUI(self):

        self.setGeometry(700,100,self.width_window,self.height_window)
        self.setWindowTitle('}{PECTIKI')
        self.setWindowIcon(QIcon('user.png'))
        self.key_button()
        self.key_9()
        
        self.show()

    def key_9(self):
        for iter in range(len(self.button_arr)):
            print(iter)

            # # if i >= 3 & i <=5:
            #     self.button_arr[i] = self.key_button(100+i*20,200+i*20)
            # if i >= 6:
            #     self.button_arr[i] = self.key_button(100+i*20,200+i*20)

            # print(self.button_arr[i])

# Кніпочка
    def key_button(self):
        self.button_0 = QPushButton('BTN', self)
        self.resize_key_button()
        print('Button',self.width())

# Метод зміни розміру і координат
    def resize_key_button(self):
        self.width_resize_button = int(round(self.width()/3))
        self.height_resize_button = int(round(self.height()/3))
        w_m = int(round(self.width() - (self.width_resize_button*1)))
        h_m = int(round(self.height() - (self.height_resize_button*1)))

        self.button_0.resize(self.width_resize_button,self.height_resize_button)
        self.button_0.move(w_m, h_m)

# метод вказує розмір вікна при зміні онлайн
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

