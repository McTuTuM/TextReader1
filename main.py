from logic import Window
from text_reader import QtWidgets
import sys
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Window()
    application.show()
    sys.exit(app.exec_())