# Pyqt5 Importe
from PyQt5 import QtWidgets, QtCore 
import sys

# Banco de dados
import mysql.connector

# Importa as classes
import Classes.Classe_Agenda
import Classes.Classes_Usuarios

# Importa as interface
from Designer.login import Ui_Login
from Designer.calendar import Ui_Calendario
from Designer.widget_main import Ui_Sistema_de_Agendamento_Psicologico
from Designer.cadastro_ok import Ui_cadastro_ok

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
        # Enviar as informações para verificar Login
        Classes.Classes_Usuarios.Usuarios.Login(self,
            user = self.ui.input_user.text(),
            senha = self.ui.input_password.text()
            )
        
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
        self.ui.Button_update_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_update))
        self.ui.Button_view_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_view))
        self.ui.Button_make_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_make))
            # Trocar paginas tela inicial
        self.ui.Button_register_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_register))
        self.ui.Button_update_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_update))
        self.ui.Button_view_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_view))
        self.ui.Button_make_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_make))

        # Usar botões para abrir calendario
        self.ui.button_calendar.clicked.connect(self.botao_calendario)
        self.ui.button_calendar_make.clicked.connect(self.botao_calendario)
        self.ui.button_calendar_update.clicked.connect(self.botao_calendario)
        
        # Botão de registro e marcar consulta
        self.ui.button_make.clicked.connect(self.marcar_consulta)
        self.ui.button_register.clicked.connect(self.registrar)

        # Conectar os QLineEdit
            # Page de registrar Usúario
        self.ui.input_name.returnPressed.connect(self.next_qlineedit)
        self.ui.input_email.returnPressed.connect(self.next_qlineedit)
        self.ui.input_adress.returnPressed.connect(self.next_qlineedit)
        
            # Depois de selecionado o QComboBox mudar para QLineEdit
        self.ui.input_sexo.currentIndexChanged.connect(self.next_qlineedit_for_qcombobox_sexo)
        self.ui.input_category.currentIndexChanged.connect(self.next_qlineedit_for_qcombobox_categoria)
        
        self.ui.input_phone.returnPressed.connect(self.next_qlineedit)
        self.ui.input_cpf.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password_confirme.returnPressed.connect(self.next_qlineedit)
          
            # Page de update Usúario
        self.ui.input_name_update.returnPressed.connect(self.next_qlineedit)
        self.ui.input_email_update.returnPressed.connect(self.next_qlineedit)
        self.ui.input_adress_update.returnPressed.connect(self.next_qlineedit)
        
            # Depois de selecionado o QComboBox mudar para QLineEdit
        self.ui.input_sexo_update.currentIndexChanged.connect(self.next_qlineedit_for_qcombobox_sexo)
        self.ui.input_category_update.currentIndexChanged.connect(self.next_qlineedit_for_qcombobox_categoria)
        
        self.ui.input_phone_update.returnPressed.connect(self.next_qlineedit)
        self.ui.input_cpf_update.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password_update.returnPressed.connect(self.next_qlineedit)
        self.ui.input_password_confirme_update.returnPressed.connect(self.next_qlineedit)

            # Page de marcar consultas
        self.ui.input_patient.returnPressed.connect(self.next_qlineedit)
        self.ui.input_psychologist.returnPressed.connect(self.next_qlineedit)

    def registrar(self):
        if self.ui.input_password.text() == self.ui.input_password_confirme.text():
            
            # Cadastrar uma nova pessoa
            cadastrar_usuario = Classes.Classes_Usuarios.Usuarios(
                nome = self.ui.input_name.text(),
                data_nascimento = self.ui.input_data.date(),
                sexo = self.ui.input_sexo.currentText(),
                cpf = self.ui.input_cpf.text(),
                email = self.ui.input_email.text(),
                senha = self.ui.input_password.text(),
                telefone = self.ui.input_phone.text(),
                endereco = self.ui.input_adress.text(),
                categoria = self.ui.input_category.currentText()
            )
            
            # Chama o método Cadastrar
            cadastrar_usuario.Cadastrar()
            self.confirmacao_cadastro()
        else:
            print("As senhas não são iguais.")

    def marcar_consulta(self):
        print(f"Paciente: {self.ui.input_patient.text()} \nPsicólogo(a): {self.ui.input_psychologist.text()} \nHorário: {self.ui.input_time.text()} \nData: {self.ui.input_data_make.text()}")

    # Altera entre QLineEdit
    def next_qlineedit(self):
            # Page de registrar Usúarios
        indentificador_qlineedit = self.sender()
        if indentificador_qlineedit == self.ui.input_name:
            self.ui.button_calendar.click()
        elif indentificador_qlineedit == self.ui.input_email:
            self.ui.input_adress.setFocus()
        elif indentificador_qlineedit == self.ui.input_adress:
            self.ui.input_phone.setFocus()
        elif indentificador_qlineedit == self.ui.input_phone:
            self.ui.input_sexo.showPopup()
        elif indentificador_qlineedit == self.ui.input_sexo:
            self.ui.input_cpf.setFocus()
        elif indentificador_qlineedit == self.ui.input_cpf:
            self.ui.input_password.setFocus()
        elif indentificador_qlineedit == self.ui.input_password:
            self.ui.input_password_confirme.setFocus()
        elif indentificador_qlineedit == self.ui.input_password_confirme:
            self.ui.button_register.click()
          
            # Page de atualizar Usúarios
        if indentificador_qlineedit == self.ui.input_name_update:
            self.ui.button_calendar_update.click()
        elif indentificador_qlineedit == self.ui.input_email_update:
            self.ui.input_adress_update.setFocus()
        elif indentificador_qlineedit == self.ui.input_adress_update:
            self.ui.input_phone_update.setFocus()
        elif indentificador_qlineedit == self.ui.input_phone_update:
            self.ui.input_sexo_update.showPopup()
        elif indentificador_qlineedit == self.ui.input_sexo_update:
            self.ui.input_cpf_update.setFocus()
        elif indentificador_qlineedit == self.ui.input_cpf_update:
            self.ui.input_password_update.setFocus()
        elif indentificador_qlineedit == self.ui.input_password_update:
            self.ui.input_password_confirme_update.setFocus()
        elif indentificador_qlineedit == self.ui.input_password_confirme_update:
            self.ui.button_update.click()
            
            # Page de marcar consulta
        if indentificador_qlineedit == self.ui.input_patient:
            self.ui.input_psychologist.setFocus()
        elif indentificador_qlineedit == self.ui.input_psychologist:
            self.ui.button_calendar_make.click()

    # Alterar QComboBox para QLineEdit 
    def next_qlineedit_for_qcombobox_sexo(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.page_register:
                # page register
            if self.ui.input_sexo == 'Masculino':
                self.ui.input_category.showPopup()
            else:
                self.ui.input_category.showPopup()
        else:
                # page update
            if self.ui.input_sexo_update == 'Masculino':
                self.ui.input_category_update.showPopup()
            else:
                self.ui.input_category_update.showPopup()
    
    def next_qlineedit_for_qcombobox_categoria(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.page_register:
            # page register
            if self.ui.input_category == 'Paciente':
                self.ui.input_cpf.setFocus()
            else:   
                self.ui.input_cpf.setFocus()
        else:
                # page update
            if self.ui.input_category_update == 'Paciente':
                self.ui.input_cpf_update.setFocus()
            else:
                self.ui.input_cpf_update.setFocus()
        

    # abrir confirmação de Cadastro
    def confirmacao_cadastro(self):
        self.confirmacao_cadastro = janela_confirmacao_cadastro()
        self.confirmacao_cadastro.show()

    # abrir calendario para selecionar data de nacimento
    def botao_calendario(self):
        self.calendar = calendario()
        self.calendar.show()

        # receber a data
        self.calendar.data_selected.connect(self.atualizar_data)

    # colocar a data recebida
    def atualizar_data(self, date):
        if self.ui.stackedWidget.currentWidget() == self.ui.page_register:
            self.ui.input_data.setDate(date)
            self.ui.input_email.setFocus()
        elif self.ui.stackedWidget.currentWidget() == self.ui.page_update:
            self.ui.input_data_update.setDate(date)
            self.ui.input_email_update.setFocus()
        else:
            self.ui.input_data_make.setDate(date)
        self.calendar.close()    

class calendario(QtWidgets.QWidget):
    data_selected = QtCore.pyqtSignal(QtCore.QDate)

    def __init__(self):
        super(calendario, self).__init__()
        self.ui = Ui_Calendario()
        self.ui.setupUi(self)

        # Remover barra da janela e deixar o fundo transparente
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Pegar a data
        self.ui.calendar.selectionChanged.connect(self.info_data)
    
    # Enviar a data selecionada
    def info_data(self):
        data_selecionada = self.ui.calendar.selectedDate()
        self.data_selected.emit(data_selecionada)

class janela_confirmacao_cadastro(QtWidgets.QWidget):
    def __init__(self):
        super(janela_confirmacao_cadastro, self).__init__()
        self.ui = Ui_cadastro_ok()
        self.ui.setupUi(self)

        # Remover barra da janela e deixar o fundo transparente
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.ui.Button_quit.clicked.connect(self.close)

# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())