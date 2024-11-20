# Pyqt5 Importe
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
import sys

# Banco de dados
import mysql.connector

# Importa as interface
import main
from Designer.widget_main import Ui_Sistema_de_Agendamento_Psicologico
from Designer.pesquisa_usuarios import Ui_pesquisa_perfil

# Classe principal(superClass)
class Usuarios:
    # Informações de Cadastro
    def __init__(self, nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo):
        self.nome_pessoa = nome_pessoa
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.tipo = tipo

    # Cadastrar Pessoa
    def Cadastrar(self):
        # Bug no meu pc
        conn = None
        cursor = None
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="admin",
                database="consultoriov1"
            )

            cursor = conn.cursor()

            # Converteções para formato adequado
            data_nascimento = self.data_nascimento.toString("yyyy-MM-dd")
            if self.sexo == "Masculino":
                sexo = 'M'
            elif self.sexo == "Femenino":
                sexo = 'F'

            if self.tipo == "Paciente":
                tipo = "paciente"
                
                # NÃO FUNCIONA ESSA PARTE
                    # # Gerar id com base no ultimo criado
                    # cursor.execute("SELECT MAX(id_paciente) FROM usuarios1")
                    # ultimo_id = cursor.fetchone()[0]

                    # id_paciente = ultimo_id + 1

                    # # Inserir dados na tabela usuarios
                    # cursor.execute(f"""
                    #     INSERT INTO usuarios1 (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo, id_paciente)
                    #     VALUES ('{self.nome_pessoa}', '{data_nascimento}', '{sexo}', '{self.cpf}', '{self.email}', '{self.senha}', '{self.telefone}', '{self.endereco}', '{tipo}', {id_paciente})
                    # """)

            elif self.tipo == "Psicólogo(a)":
                tipo = "psicólogo"

                # NÃO FUNCIONA ESSA PARTE
                    # # Gerar id com base no ultimo criado
                    # cursor.execute("SELECT MAX(id_paciente) FROM usuarios1")
                    # ultimo_id = cursor.fetchone()[0]

                    # id_psicologo = ultimo_id + 1

                    # # Inserir dados na tabela usuarios
                    # cursor.execute(f"""
                    #     INSERT INTO usuarios1 (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo, id_psicologo)
                    #     VALUES ('{self.nome_pessoa}', '{data_nascimento}', '{sexo}', '{self.cpf}', '{self.email}', '{self.senha}', '{self.telefone}', '{self.endereco}', '{tipo}', {id_psicologo})
                    # """)

            # Inserir dados na tabela usuarios
            cursor.execute(f"""
                INSERT INTO usuarios1 (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
                VALUES ('{self.nome_pessoa}', '{data_nascimento}', '{sexo}', '{self.cpf}', '{self.email}', '{self.senha}', '{self.telefone}', '{self.endereco}', '{tipo}')
             """)

            conn.commit()
            print("Cadastro realizado com sucesso!")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
              conn.close()

    # Atualizar informações do cadastro
    def Atualizar_informações(self):
        pass

    # Fazer login no sistema
    def Login(self, user, senha):
        # Bug no meu pc
        conn = None
        cursor = None
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="admin",
                database="consultoriov1"
            )

            cursor = conn.cursor()

            # Pegar informações para Login
            cursor.execute(f"""Select * From usuarios1 Where cpf = '{user}' And senha = '{senha}'""")
            cursor.fetchall()

            # Verificar as informações do Login
            if cursor.rowcount == 1:
                self.psy = main.sistema_de_agendamento_psicologico()
                self.psy.show()
                self.close()
            else:
                print('Dados invalidos')
        
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

class pesquisa_usuarios(QtWidgets.QWidget):
    # Define o sinal para emitir o nome e cpf do paciente selecionado
    usuario_selecionado = QtCore.pyqtSignal(str, str, int)  # Nome, CPF e ID usuario
    
    def __init__(self, tipo_selecionado):
        super(pesquisa_usuarios, self).__init__()
        self.ui = Ui_pesquisa_perfil()
        self.ui.setupUi(self)
        self.tipo_selecionado = tipo_selecionado


        # Permite a seleção do usuario com dois click
        self.ui.pesquisa_usuarios.cellDoubleClicked.connect(self.pegar_dados)

        # Bug no meu pc
        conn = None
        cursor = None
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="admin",
                database="consultoriov1"
            )

            cursor = conn.cursor()


            if self.tipo_selecionado == 1:
                cursor.execute("""SELECT nome_pessoa, cpf, idade, sexo, email, telefone, endereco, id_usuario FROM v_pacientes""")
            elif self.tipo_selecionado == 2:
                cursor.execute("""SELECT nome_pessoa, cpf, idade, sexo, email, telefone, endereco, id_usuario FROM v_psicologo""")

            rows = cursor.fetchall()

            # Número de linhas
            self.ui.pesquisa_usuarios.setRowCount(len(rows))

            # Pega os dados do banco de dados e coloca na pesquisa
            for i, row in enumerate(rows):
                for j, item in enumerate(row):
                    self.ui.pesquisa_usuarios.setItem(i, j, QTableWidgetItem(str(item)))
                    
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def pegar_dados(self, row):
        # Seleciona a linha e extrai os dados
        nome = self.ui.pesquisa_usuarios.item(row, 0).text()
        cpf = self.ui.pesquisa_usuarios.item(row, 1).text()
        idade = self.ui.pesquisa_usuarios.item(row, 2).text()
        sexo = self.ui.pesquisa_usuarios.item(row, 3).text()
        email = self.ui.pesquisa_usuarios.item(row, 4).text()
        telefone = self.ui.pesquisa_usuarios.item(row, 5).text()
        endereco = self.ui.pesquisa_usuarios.item(row, 6).text()
        id_usuario_str = self.ui.pesquisa_usuarios.item(row, 7).text()

        id_usuario = int(id_usuario_str)

        # Emite o sinal com o nome selecionado
        self.usuario_selecionado.emit(nome, cpf, id_usuario)

        # Exibir as informações no terminal
        if self.tipo_selecionado == 1:     
            print(f"\nID: {id_usuario} Paciente Selecionado: {nome}, CPF: {cpf}, Idade: {idade}, Sexo: {sexo}, Email: {email}, Telefone: {telefone}, Endereço: {endereco}\n")
        elif self.tipo_selecionado == 2:     
            print(f"\nID: {id_usuario} Psicólogo(a) Selecionado: {nome}, CPF: {cpf}, Idade: {idade}, Sexo: {sexo}, Email: {email}, Telefone: {telefone}, Endereço: {endereco}\n")

        
        self.close()
                

# Classe para os profissionais da área
class Psicologo(Usuarios):
    pass

# Classes dos pacientes
class Paciente(Usuarios):
    pass