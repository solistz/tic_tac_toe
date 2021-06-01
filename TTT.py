import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox 
from PyQt5.QtGui import QIcon

class Tic(QWidget):

    def __init__(self):
        super().__init__()
        self.button_arr = [
            'button1',
            'button2',
            'button3',
            'button4',
            'button5',
            'button6',
            'button7',
            'button8',
            'button9',
        ]
        self.vertical = None
        self.horizont = None

        self.initUI()

    def initUI(self):

        self.setGeometry(700,100,600,600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('user.png'))
        # self.key_button()
        self.button_9()
        self.quit_button()
        
        self.show()

    def resizeEvent(self, event):
        print('test', self.height(), self.width())
        self.size_button()
        return super(Tic, self).resizeEvent(event)


    def size_button(self):
        self.vertical = int(round((self.height()/6)/2))
        self.horizont = int(round((self.width()/6)/2))
        print(self.vertical,self.horizont)
        print(type(self.vertical),type(self.horizont))
        
    
    def button_9(self):
        for i in range(len(self.button_arr)):
            if i <= 2:
                self.button_arr[i] = self.key_button(self.vertical,200+i*20)
            # # if i >= 3 & i <=5:
            #     self.button_arr[i] = self.key_button(100+i*20,200+i*20)
            # if i >= 6:
            #     self.button_arr[i] = self.key_button(100+i*20,200+i*20)

            # print(self.button_arr[i])
        

     
    def key_button(self,h,v):
        self.button = QPushButton('BTN', self)
        self.button.resize(60, 60)
        self.button.move(h, v)
        # self.button.clicked.connect(self.cliked_button)

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



if __name__ == '__main__':

    app = QApplication(sys.argv)

    Tac = Tic()
    
    sys.exit(app.exec_())

