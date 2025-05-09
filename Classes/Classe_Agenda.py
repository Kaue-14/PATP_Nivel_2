# Pyqt5 Importe
from PyQt5 import QtWidgets, QtCore 
from PyQt5.QtWidgets import QTableWidgetItem
import sys

# Banco de dados
import mysql.connector

# Importa as interface
import main
from Designer.widget_main import Ui_Sistema_de_Agendamento_Psicologico

class Agenda:
    # Informações da consulta
    def __init__(self, data, hora, paciente, psicologo, observacoes, status):
        self.data = data
        self.hora = hora
        self.paciente = paciente
        self.psicologo = psicologo
        self.status = status
        self.observacoes = observacoes

    # Adicionar e Marcar consultas
    def Marca_Consulta(self):
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
                # Data
            data = self.data.toString("yyyy-MM-dd")
                # Horário
            if self.hora == '7 : 00':
                hora = '07:00:00'
            elif self.hora == '8 : 00':
                hora = '08:00:00'
            elif self.hora == '9 : 00':
                hora = '09:00:00'
            elif self.hora == '10 : 00':
                hora = '10:00:00'
            elif self.hora == '11 : 00':
                hora = '11:00:00'
            elif self.hora == '12 : 00':
                hora = '12:00:00'
            elif self.hora == '13 : 00':
                hora = '13:00:00'
            elif self.hora == '14 : 00':
                hora = '14:00:00'
            elif self.hora == '15 : 00':
                hora = '15:00:00'
            elif self.hora == '16 : 00':
                hora = '16:00:00'
            elif self.hora == '17 : 00':
                hora = '17:00:00'

            # Inserir dados na tabela agendamentos
            cursor.execute(f"INSERT INTO agendamentos1 (id_paciente, id_psicologo, observacoes, data, hora) VALUES ({self.paciente}, {self.psicologo}, '{self.observacoes}', '{data}', '{hora}')")
            conn.commit()

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    # Cancelar e remover consultas marcadas
    def Cancelar_Consultas(self):
        pass