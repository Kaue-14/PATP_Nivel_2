from PyQt5 import QtWidgets 
import sys

from Designer.login import Ui_Login

class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # botão de login
        self.ui.btn_login.clicked.connect(self.abrir_janelas)
    
    def abrir_janelas(self):
        print('Funciona')
        
# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())