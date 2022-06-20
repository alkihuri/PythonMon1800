#pyqt 3.0 
# https://docs.google.com/presentation/d/14PsvFT_9wBGSXjAtZ1D0K909I5fUud2U4GPuVMDoypQ/edit#slide=id.p
# Caesar cipher
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit
import sys



class View(QMainWindow):
    def __init__(self):
        super(View,self).__init__()
        self.controller=newController
        self.setGeometry(300,200,300,250)
        self.setWindowTitle("Shizaaaaa")
        self.word=self.CreateInputField("Word: ", 25,25)
        self.result=self.CreateInputField("Result: ", 25,75)
        self.encryptBtn=self.CreateButton("Encrypt", 25,125,self.EncryptHandler)
        self.decryptBtn=self.CreateButton("Decrypt", 25,175,self.DecryptHandler)

    def EncryptHandler(self):
        self.controller.SetWorldToEncrypt(self.word.text())
        self.controller.DoCrypt()

    def DecryptHandler(self):
        self.controller.SetWorldToDecrypt(self.word.text())
        self.controller.DoDerypt()

    def CreateLabel(self,text,x,y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x,y)
        return newLabel

    def CreateInputField(self,label,x,y):
        offsetForInputField = 50
        self.CreateLabel(label,x,y)
        line = QLineEdit(self)
        line.move(x+offsetForInputField, y)
        line.resize(200, 32)
        return line

    def CreateButton(self,text,x,y,fun):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.resize(250, 32)
        newButton.move(x,y)
        newButton.clicked.connect(fun)
        newButton.clicked.connect(self.UpdateUI)
        return newButton
  
    def UpdateUI(self):
        self.result.setText(myController.GetResult())


class controller():
    def __init__(self,newModel):
        self.model = newModel

    def SetWordToDecrypt(self,word):
        self.wordToDecrypt = word

    def SetWordToEncrypt(self,word):
        self.wordToEncrypt = word

    def DoCrypt(self):
        self.encryptedword = self.model.Encrypt(self.wordToEncrypt)
        self.result = self.encryptedword

    def DoDecrypt(self):
        self.decryptedword = self.model.Decrypt(self.wordToDecrypt)
        self.result = self.decryptedword

    def GetResult(self):
        return self.result

class model():
    def __init__(self,key):
        self.key = key

    def Encrypt(self,word):
        wLength = len(word)
        ecnrypted = ""
        listWord = list(word)
        for i in range(wLength):
            eachCharacter = word[i]
            eachCharacterInt = int(ord(word[i]))
            encryptedCahracter = (eachCharacterInt - self.key) % 255 
            ecnrypted += chr(encryptedCahracter)
        return ecnrypted

    def Decrypt(self,word):
        wLength = len(word)
        Decrypted = ""
        listWord = list(word)
        for i in range(wLength):
            eachCharacter = word[i]
            eachCharacterInt = int(ord(word[i]))
            decryptedCahracter = (eachCharacterInt + self.key) % 255 
            decrypted += chr(decryptedCahracter)
        return ecnrypted