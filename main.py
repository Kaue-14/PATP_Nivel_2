from PyQt5 import QtWidgets, QtCore 
import sys

from Designer.login import Ui_Login
from Designer.register import Ui_Register

class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # Sem barra da janela
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # botão de login
        self.ui.button_login.clicked.connect(self.botao_login)
    
    def botao_login(self):
        self.reg = register()
        self.reg.show()
        self.close()
        print(f"Usuário: {self.ui.input_user.text()} \nSenha: {self.ui.input_password.text()}")
        
        
class register(QtWidgets.QMainWindow):
    def __init__(self):
        super(register, self).__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        
        # Sem barra da janela
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())