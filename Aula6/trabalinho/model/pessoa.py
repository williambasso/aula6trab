# Classe Pessoa, que recebe os dados pessoais de cada funcionário
class Pessoa:
    __id = 0
    __nome = ''
    __sobrenome = ''
    __cpf = 0
    
    # Método getter, usados para buscarem/recuperarem os dados
    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome
    
    def get_cpf(self):
        return self.__cpf
    
    # Método setter, usados para setarem/alterarem os dados
    def set_nome(self, nome):
        self.__nome = nome

    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
