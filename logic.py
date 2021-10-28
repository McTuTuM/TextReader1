from PyQt5 import QtWidgets
from text_reader import Ui_MainWindow
import easyocr

class Window(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.addFunctions()


    def addFunctions(self):
        self.pushButton.clicked.connect(lambda:self.showDialog())
        self.pushButton_2.clicked.connect(lambda:self.saveDialog())
        self.pushButton_3.clicked.connect(lambda:self.main())

    def text_recognition(self, file_path,text_file_name):
        reader = easyocr.Reader(["ru", "en"])
        result = reader.readtext(file_path, detail= 0, paragraph= True)
        with open(text_file_name, "w") as file:
            for line in result:
                file.write(f"{line}\n\n\n\n")
        return self.label_3.setText(f"Result wrote into {text_file_name}")

    def main(self):
        file_path = self.lineEdit.text()
        text_file_name = self.lineEdit_2.text()
        self.text_recognition(file_path=file_path, text_file_name=text_file_name)
        
    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "C:\cod\TextReader")[0]
        try:
            f = open(fname, 'r')
            with f:
                # data = f.read()
                self.lineEdit.setText(fname)
                f.close()
        except:
            pass
    def saveDialog(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "C:\cod\TextReader")[0]
        try:
            f = open(fname, 'w')
            with f:
                self.lineEdit_2.setText(fname)
                f.close()
        except:
            pass
