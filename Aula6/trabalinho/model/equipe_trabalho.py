from funcionario import Funcionario

class EquipeTrabalho(Funcionario):
    def __init__(self, nome):
        self.nome = nome

    #getter
    def get_nome(self):
        return self.nome

    # setter
    def set_nome(self, nome):
        self.nome = nome