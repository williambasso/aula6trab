from trabalinho.model.funcionario import Funcionario

class LinguagemProgramacao(Funcionario):
    __id = 0
    __nome_linguagem = ''

    #getter
    def get_id(self):
        return self.__id

    def get_nome_linguagem(self):
        return self.__nome_linguagem
    
    #setters

    def set_id(self, id):
        self.__id = id

    def set_nome_linguagem(self, nome_linguagem):
        self.__nome_linguagem = nome_linguagem
    