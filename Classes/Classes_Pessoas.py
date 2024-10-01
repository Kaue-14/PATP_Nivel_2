# Pyqt5 Importe
from PyQt5 import QtWidgets, QtCore 
import sys

# Banco de dados
import mysql.connector

# Importa as interface
from Designer.widget_main import Ui_Sistema_de_Agendamento_Psicologico

# Classe principal(superClass)
class Pessoas:
    # Informações de Cadastro
    def __init__(self, nome, data_nascimento, sexo, cpf, email, senha, telefone, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        pass

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
                database="banco_de_dados_agendamento_psicologia"
            )

            cursor = conn.cursor()

            # Inserir dados na tabela usuarios
            cursor.execute("""
                INSERT INTO usuarios (nome, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'paciente')
            """, (self.nome, self.data_nascimento, self.sexo, self.cpf, self.email, self.senha, self.telefone, self.endereco))

            conn.commit()
            print("Usuário cadastrado com sucesso.")

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
    def Login(self):
        pass

# Classe para os profissionais da área
class Psicologo(Pessoas):
    pass

# Classes dos pacientes
class Paciente(Pessoas):
    pass