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
        # Converteções para formato adequado
        data = self.data.toString("yyyy-MM-dd")

        print(f"Paciente: {self.paciente} \nPsicólogo(a): {self.psicologo} \nObservações: {self.observacoes} \nHorário: {self.hora} \nData: {data}")


    # Cancelar e remover consultas marcadas
    def Cancelar_Consultas(self):
        pass