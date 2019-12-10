import sys
sys.path.append("C:/Users/900213/Desktop/trabalinho/")

# Importação da classe Funcionario, que recebe os dados profissionais de cada funcionário
from trabalinho.model.funcionario import Funcionario

# Classe herdada de Funcionario, que recebe o nome das linguagens que os funcionários usam/usarão
class LinguagemProgramacao(Funcionario):
    __id = 0
    __nome_linguagem = ''

   # Método getter, usados para buscarem/recuperarem os dados
    def get_id(self):
        return self.__id

    def get_nome_linguagem(self):
        return self.__nome_linguagem
    
   # Método setter, usados para setarem/alterarem os dados
    def set_id(self, id):
        self.__id = id

    def set_nome_linguagem(self, nome_linguagem):
        self.__nome_linguagem = nome_linguagem
    
