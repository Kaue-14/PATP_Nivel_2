# Classe principal(superClass)
class Pessoas:
    # Informações de Cadastro
    def __init__(self, nome, idade, sexo, cpf, email, senha, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        pass

    # Cadastrar Pessoa
    def Cadastrar(self):
        pass

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