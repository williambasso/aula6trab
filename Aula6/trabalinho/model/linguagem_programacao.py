from trabalinho.model.funcionario import Funcionario

class LinguagemProgramacao(Funcionario):
    def __init__(self, id, nome_linguagem):
        self.id = id
        self.nome_linguagem = nome_linguagem

    #getter
    def get_id(self):
        return self.id

    def get_nome_linguagem(self):
        return self.nome_linguagem
    
    #setters

    def set_id(self, id):
        self.id = id

    def set_nome_linguagem(self, nome_linguagem):
        self.nome_linguagem = nome_linguagem
    