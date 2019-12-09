from trabalinho.dao.basedao import BaseDao

class FuncionarioDao(BaseDao):
    base = BaseDao()

    def listar(self):
        return self.base.listar('select * from funcionarios')

    def buscar_por_id(self, id):
        return self.base.buscar_por_id(f'select from funcionarios where id = {id}')

    def inserir(self, nome, sobrenome, cpf, cargo, salario, pis, equipe_trabalho, linguagem_programacao):
        self.base.inserir(
            f'insert into funcionarios( nome, sobrenome, cpf, cargo, salario, pis, equipe_trabalho, linguagem_programacao) values("{nome}" , "{sobrenome}" , "{cpf}" , "{cargo}" , {salario} , {pis}, "{equipe_trabalho}", "{linguagem_programacao}")')

    def alterar(self, id, nome, sobrenome, cpf, cargo, salario, pis, equipe_trabalho, linguagem_programacao):
        self.base.alterar(
            f'update funcionarios set nome = "{nome}" , sobrenome = "{sobrenome}", cpf = "{cpf}", cargo = "{cargo}", salario = {salario}, pis = {pis},equipe_trabalho = "{equipe_trabalho}", linguagem_programacao = "{linguagem_programacao}" where id = {id}')

    def deletar(self, id):
        self.base.deletar(f'delete from funcionarios where id = {id}')


#inserir('Joao','Joao', 6456465)
# alterar(5,'Lucas','William',15115)
# deletar(4)
lista = FuncionarioDao()

for l in ():
    print(l)
