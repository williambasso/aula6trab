import sys
sys.path.append("C:/Users/900213/Desktop/trabalinho/")

# Importação do arquivo com a classe que realiza conexão com o banco de dados
from dao.basedao import BaseDao

# Importação da classe Pessoa, que recebe os dados pessoais dos funcionários
from model.pessoa import Pessoa

# Classe herdada da classe de conexão com o banco de dados e que irá enviar os comandos para as açlões no banco de dados
class FuncionarioDao(BaseDao):
    
    def listar(self):
        return super().listar('SELECT * from funcionarios')

    def buscar_por_id(self, id):
        return super().buscar_por_id(f'SELECT FROM funcionarios WHERE id = {id}')

    def inserir(self, nome, sobrenome, cpf, cargo, salario, pis, equipe_trabalho, linguagem_programacao):
        super().inserir(
            f'INSERT INTO funcionarios( nome, sobrenome, cpf, cargo, salario, pis, equipe_trabalho, linguagem_programacao) VALUES("{nome}" , "{sobrenome}" , "{cpf}" , "{cargo}" , {salario} , {pis}, "{equipe_trabalho}", "{linguagem_programacao}")')

    def editar(self, p:Pessoa):
        super().alterar(
            f'UPDATE funcionarios SET nome = "{p.nome}" WHERE id = {id} , sobrenome = "{p.sobrenome}", cpf = "{p.cpf}", cargo = "{p.cargo}", salario = {p.salario}, pis = {p.pis},equipe_trabalho = "{p.equipe_trabalho}", linguagem_programacao = "{p.linguagem_programacao}" where id = {id}')

    def deletar(self, id):
        super().deletar(f'DELETE FROM funcionarios WHERE id = {id}')


#inserir('Joao','Joao', 6456465) 
# alterar(5,'Lucas','William',15115)
# deletar(4)
# lista = FuncionarioDao()
# for l in lista():
#     print(l)
