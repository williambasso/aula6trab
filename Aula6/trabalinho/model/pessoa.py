class Pessoa:
    def __init__(self, nome, sobrenome, cpf, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    #getter
    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome
    
    def get_cpf(self):
        return self.cpf
    
    #setters

    def set_nome(self, nome):
        self.nome = nome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome
    
    def set_cpf(self, cpf):
        self.cpf = cpf
        
