import sys
sys.path.append("C:/Users/900213/Desktop/trabalinho/")

from dao.funcionario_dao import FuncionarioDao
from model.pessoa import Pessoa
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def iniciar():
    return render_template('home.html')

@app.route('/listagem')
def listar():
    pessoa = FuncionarioDao()
    listar = pessoa.listar()
    return render_template('listagem.html', pessoa = listar)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/editar')    
def editar():
    id = request.args['id']
    pessoa = FuncionarioDao()
    pessoa.editar(id)
    return render_template('editar.html', pessoa = editar)

@app.route('/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    cargo = request.form['cargo']
    pis = request.form['pis']
    salario = request.form['salario']
    equipe_trabalho = request.form['equipe_trabalho']
    linguagem_programacao = request.form['linguagem_programacao']
    pessoa = FuncionarioDao()    
    pessoa.inserir(nome,sobrenome,cpf, cargo, pis, salario, equipe_trabalho, linguagem_programacao)
    return redirect('/')

# @app.route('/salvar_editar', methods=['POST'])
# def editar_salvar():
#     id = request.form['id']
#     nome = request.form['nome']
#     sobrenome = request.form['sobrenome']
#     cpf = request.form['cpf']
#     cargo = request.form['cargo']
#     pis = request.form['pis']
#     salario = request.form['salario']
#     pessoa = FuncionarioDao()
#     pessoa.editar_salvar(id, nome,sobrenome,cpf, cargo, pis, salario)
#     return redirect('/')

@app.route('/deletar')
def deletar():
    id = request.args['id']
    pessoa = FuncionarioDao()
    pessoa.deletar(id)
    return redirect('listagem.html')

app.run(port=80, debug=True)
