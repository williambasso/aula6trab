import sys
sys.path.append("C:/Users/900213/Desktop/trabalinho/")

# Importação da classe Funcionário, que recebe os dados profissionais dos funcionarios
from trabalinho.model.funcionario import Funcionario

# Classe herdada de Funcionário, que irá receber o nome da equipe que o funcionário trabalhará
class EquipeTrabalho(Funcionario):
    __nome_equipe = ''

    #getter
    def get_nome_equipe(self):
        return self.__nome_equipe

    # setter
    def set_nome_equipe(self, nome_equipe):
        self.__nome_equipe = nome_equipe
