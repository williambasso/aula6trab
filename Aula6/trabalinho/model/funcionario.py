import sys
sys.path.append("C:/Users/900213/Desktop/trabalinho/")

# Importação da classe Pessoa, que recebe os dados pessoais dos funcionários
from trabalinho.model.pessoa import Pessoa

# Classe herdada de Pessoa, que recebe os dados profissionais privados de cada funcionário
class Funcionario(Pessoa):
    __linguagem = ''
    __equipe = ''
    __salario = 0
    __cargo = ''
    __pis = 0

    # Método getter, usados para buscarem/recuperarem os dados
    def get_salario(self):
        return self.__salario
    
    def get_linguagem(self):
        return self.__linguagem
    
    def get_equipe(self):
        return self.__equipe

    def get_cargo(self):
        return self.__cargo
    
    def get_pis(self):
        return self.__pis
    
    # Método setter, usados para setarem/alterarem os dados
    def set_salario(self, salario):
        self.__salario = salario
        
    def set_linguagem(self, linguagem):
        self.__linguagem = linguagem
        
    def set_equipe(self, equipe):
        self.__equipe = equipe

    def set_cargo(self, cargo):
        self.__cargo = cargo
    
    def set_pis(self, pis):
        self.__pis = pis


        
# class Funcionario(Pessoa):
#     getter
#     def get_cadastro(self):        
#         return {'Salario':self.salario, 'Cargo':self.cargo, 'Pis':self.pis}
#     setters
#     def set_salario(self, salario, cargo, pis):
#         self.salario = salario
#         self.cargo = cargo
#         self.pis = pis
#  teste.cadastrar_db(teste.get_cadastrar)
