from flask import Flask, render_template, request, redirect
from trabalinho.model.pessoa import Pessoa

app = Flask(__name__)

@app.route('/')
def iniciar():
    return render_template('home.html')

@app.route('/listagem')
def listar():
    pessoa = Pessoa()
    listar = pessoa.listar()
    return render_template('listagem.html', pessoa = listar)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/editar')    
def editar():
    id = request.args['id']
    pessoa = Pessoa()
    editar = pessoa.editar(id)
    return render_template('editar.html', pessoa = editar)

@app.route('/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    cargo = request.form['cargo']
    pis = request.form['pis']
    salario = request.form['salario']
    pessoa = Pessoa()
    pessoa.salvar(nome,sobrenome,cpf, cargo, pis, salario)
    return redirect('/')

@app.route('/salvar_editar', methods=['POST'])
def editar_salvar():
    id = request.form['id']
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    cargo = request.form['cargo']
    pis = request.form['pis']
    salario = request.form['salario']
    pessoa = Pessoa()
    pessoa.editar_salvar(id, nome,sobrenome,cpf, cargo, pis, salario)
    return redirect('/')

@app.route('/deletar')
def deletar():
    id = request.args['id']
    pessoa = Pessoa()
    pessoa.deletar(id)
    return redirect('listagem.html')

app.run(port=80, debug=True)
