from funcionario import Funcionario

class EquipeTrabalho(Funcionario):
    __nome = ''

    #getter
    def get_nome(self):
        return self.__nome

    # setter
    def set_nome(self, nome):
        self.__nome = nome