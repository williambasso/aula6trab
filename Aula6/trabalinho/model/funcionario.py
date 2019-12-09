from trabalinho.model.pessoa import Pessoa
# import sys
# sys.path.append('../dao')

class Funcionario(Pessoa):
    def __init__(self, salario, cargo, pis):
        self.salario = salario
        self.cargo = cargo
        self.pis = pis

    #getter
    def get_salario(self):
        return self.salario

    def get_cargo(self):
        return self.cargo
    
    def get_pis(self):
        return self.pis
    
    #setters

    def set_salario(self, salario):
        self.salario = salario

    def set_cargo(self, cargo):
        self.cargo = cargo
    
    def set_pis(self, pis):
        self.pis = pis


        
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