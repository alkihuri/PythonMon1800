from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class NewWin(QMainWindow):
    def __init__(self):
        super(NewWin,self).__init__()
        self.counter=0
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Counter")
        
        

    def CreateLabel(self,x=50,y=50):
        self.newLabel=QtWidgets.QLabel(self)
        self.newLabel.setText("0")
        self.newLabel.Move(x,y)
    
    def CreateButton(self,x=50,y=50):
        self.newButton=QtWidgets.QPushButton(self)
        self.newButton.setText("CLick")
        self.newButton.Move(x,y)
        self.newButton.clicked.connect(self.CounterFunc)


    def CounterFunc(self):
        self.counter+=1
        self.newLabel.setText(str(self.counter))

app=QApplication(sys.argv)
window=NewWin()
window.show()

sys.exit(app.exec_())
