from PyQt5 import QtWidgets, QtCore 
import sys

from Designer.login import Ui_Login
from Designer.register import Ui_Register
from Designer.calendar import Ui_Calendario
from Designer.widget_main import Ui_Sistema_de_Agendamento_Psicologico

class login(QtWidgets.QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # Remover barra da janela e deixar o fundo transparente
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # botão de login
        self.ui.button_login.clicked.connect(self.botao_login)
    
        # Conectar os QLineEdit
        self.ui.input_user.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password.returnPressed.connect(self.next_qlineedit)

    def botao_login(self):
        self.psy = sistema_de_agendamento_psicologico()
        self.psy.show()
        self.close()
        print(f"Usuário: {self.ui.input_user.text()} \nSenha: {self.ui.input_password.text()}")
        
    # Altera entre QLineEdit
    def next_qlineedit(self):
        indentificador_qlineedit = self.sender()
        if indentificador_qlineedit == self.ui.input_user:
            self.ui.input_password.setFocus()
        elif indentificador_qlineedit == self.ui.input_password:
            self.ui.button_login.click()

class sistema_de_agendamento_psicologico(QtWidgets.QWidget):
    def __init__(self):
        super(sistema_de_agendamento_psicologico, self).__init__()
        self.ui = Ui_Sistema_de_Agendamento_Psicologico()
        self.ui.setupUi(self)

        # Trocar paginas
        self.ui.Button_main_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_main))
        self.ui.Button_register_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_register))
        self.ui.Button_view_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_view))
        self.ui.Button_make_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_make))

        # Usar botões para abrir calendario
        self.ui.button_calendar.clicked.connect(self.botao_calendario)
        self.ui.button_calendar_make.clicked.connect(self.botao_calendario)
        
        # Botão de registro
        self.ui.button_register.clicked.connect(self.registrar)

        # Conectar os QLineEdit
        self.ui.input_name.returnPressed.connect(self.next_qlineedit)
        self.ui.input_email.returnPressed.connect(self.next_qlineedit)
        self.ui.input_adress.returnPressed.connect(self.next_qlineedit)
        self.ui.input_sexo.returnPressed.connect(self.next_qlineedit)
        self.ui.input_phone.returnPressed.connect(self.next_qlineedit)
        self.ui.input_cpf.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password_confirme.returnPressed.connect(self.next_qlineedit)

    def registrar(self):
        if self.ui.input_password.text() == self.ui.input_password_confirme.text():
            print(f"Nome: {self.ui.input_name.text()} \nData de Nacimento: {self.ui.input_data.text()} \nCPF: {self.ui.input_cpf.text()} \nSexo: {self.ui.input_sexo.text()} \nCelular: {self.ui.input_phone.text()} \nEndereço: {self.ui.input_adress.text()} \nEmail: {self.ui.input_email.text()} \nSenha: {self.ui.input_password.text()}")
        else:
            print("As senhas não são iguais.")

    # Altera entre QLineEdit
    def next_qlineedit(self):
        indentificador_qlineedit = self.sender()
        if indentificador_qlineedit == self.ui.input_name:
            self.ui.input_email.setFocus()
        elif indentificador_qlineedit == self.ui.input_email:
            self.ui.input_adress.setFocus()
        elif indentificador_qlineedit == self.ui.input_adress:
            self.ui.input_phone.setFocus()
        elif indentificador_qlineedit == self.ui.input_phone:
            self.ui.input_sexo.setFocus()
        elif indentificador_qlineedit == self.ui.input_sexo:
            self.ui.input_cpf.setFocus()
        elif indentificador_qlineedit == self.ui.input_cpf:
            self.ui.input_password.setFocus()
        elif indentificador_qlineedit == self.ui.input_password:
            self.ui.input_password_confirme.setFocus()
        elif indentificador_qlineedit == self.ui.input_password_confirme:
            self.ui.button_register.click()
        
            

    # abrir calendario para selecionar data de nacimento
    def botao_calendario(self):
        self.calendar = calendario()
        self.calendar.show()

        # receber a data
        self.calendar.data_selected.connect(self.atualizar_data)

    # colocar a data recebida
    def atualizar_data(self, date):
        self.ui.input_data.setDate(date)
        self.ui.input_data_make.setDate(date)
        self.calendar.close()    

class register(QtWidgets.QWidget):
    def __init__(self):
        super(register, self).__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)

        # Remover barra da janela e deixar o fundo transparente
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.button_calendar.clicked.connect(self.botao_calendario)

        self.ui.button_register.clicked.connect(self.registrar)

    def registrar(self):
        if self.ui.input_password.text() == self.ui.input_password_confirme.text():
            print(f"Nome: {self.ui.input_name.text()} \nData de Nacimento: {self.ui.input_data.text()} \nCPF: {self.ui.input_cpf.text()} \nSexo: {self.ui.input_sexo.text()} \nCelular: {self.ui.input_phone.text()} \nEndereço: {self.ui.input_adress.text()} \nEmail: {self.ui.input_email.text()} \nSenha: {self.ui.input_password.text()}")
        else:
            print("As senhas não são iguais.")

    # abrir calendario para selecionar data de nacimento
    def botao_calendario(self):
        self.calendar = calendario()
        self.calendar.show()

        # receber a data
        self.calendar.data_selected.connect(self.atualizar_data)

    # colocar a data recebida
    def atualizar_data(self, date):
        self.ui.input_data.setDate(date)
        self.calendar.close()

class calendario(QtWidgets.QWidget):
    data_selected = QtCore.pyqtSignal(QtCore.QDate)

    def __init__(self):
        super(calendario, self).__init__()
        self.ui = Ui_Calendario()
        self.ui.setupUi(self)

        # Remover barra da janela e deixar o fundo transparente
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Pegar a data
        self.ui.calendar.selectionChanged.connect(self.info_data)
    
    # Enviar a data selecionada
    def info_data(self):
        data_selecionada = self.ui.calendar.selectedDate()
        self.data_selected.emit(data_selecionada)

# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())