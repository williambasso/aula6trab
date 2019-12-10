import sys
sys.path.append("C:/Users/900224/Desktop/Aula6/trabalinho/")

from dao.funcionario_dao import FuncionarioDao
from dao.linguagem_dao import LinguagemDao
from dao.equipe_dao import EquipeDao

from model.funcionario import Funcionario
from model.linguagem_programacao import LinguagemProgramacao
from model.equipe_trabalho import EquipeTrabalho

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def iniciar():
    return render_template('home.html')


@app.route('/listagem')
def listar():
    pessoa = FuncionarioDao
    listar = pessoa.listar
    return render_template('listagem.html', pessoa = listar)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


@app.route('/salvar', methods = ['POST'])
def salvar():
    # nome_linguagem =  request.form['nome_linguagem']
    # linguagem = LinguagemProgramacao(nome_linguagem)
    # dao_ling = LinguagemDao()
    # linguagem.set_id( dao_ling.salvar_linguagem(linguagem) )

    # nome_equipe = request.form['nome_equipe']
    # equipe = EquipeTrabalho(nome_equipe)
    # dao_equip = EquipeDao()
    # equipe.set_id( dao_equip.salva_equipe(equipe) )

    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    salario = request.form['salario']
    cargo = request.form['cargo']
    pis = request.form['pis']    

    funcionario = Funcionario(nome, sobrenome, cpf, salario, cargo, pis, linguagem, equipe)

    func_dao = FuncionarioDao()   
    func_dao.inserir(funcionario)
    return redirect('/')

@app.route('/editar', methods=['POST'])
def editar():
    id = request.form['id']
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    salario = request.form['salario']
    cargo = request.form['cargo']
    pis = request.form['pis']
    funcionario = Funcionario(nome, sobrenome, cpf, salario, cargo, pis, id=id)
    dao = FuncionarioDao()
    dao.alterar(funcionario)
    return redirect('/')

@app.route('/deletar')
def deletar():
    id = request.args['id']
    funcionario = FuncionarioDao()
    funcionario.deletar(id)
    return redirect('listagem.html')

app.run(port=80, debug=True)
