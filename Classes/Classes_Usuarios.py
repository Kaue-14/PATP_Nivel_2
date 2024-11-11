# Pyqt5 Importe
from PyQt5 import QtWidgets, QtCore 
import sys

# Banco de dados
import mysql.connector

# Importa as interface
import main
from Designer.widget_main import Ui_Sistema_de_Agendamento_Psicologico

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
                password="",
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
                tipo = "Paciente"
            elif self.tipo == "Psicólogo(a)":
                tipo = "Psicólogo(a)"

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
                password="",
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
        
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                

# Classe para os profissionais da área
class Psicologo(Usuarios):
    pass

# Classes dos pacientes
class Paciente(Usuarios):
    pass