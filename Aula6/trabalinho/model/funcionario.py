from trabalinho.model.pessoa import Pessoa
# import sys
# sys.path.append('../dao')

class Funcionario(Pessoa):
    __salario = 0
    __cargo = ''
    __pis = 0

    #getter
    def get_salario(self):
        return self.__salario

    def get_cargo(self):
        return self.__cargo
    
    def get_pis(self):
        return self.__pis
    
    #setters

    def set_salario(self, salario):
        self.__salario = salario

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