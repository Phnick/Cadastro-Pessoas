from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Pessoas
from helpers import FormularioPessoa

# onde fica as rotas criadas


@app.route('/')
def index():
    # query faz uma consulta na tabela Pessoas e entrega e ordena essa consulta atraves do 'order_by' com base a coluna 'id
    lista = Pessoas.query.order_by(Pessoas.id)
    return render_template('lista.html', titulo='Cadastros', usuarios=lista)


@app.route('/novo')
def novo():
    # verificando se o usuario passou pelo login para poder ter acesso a pagina que cria  um novo cadastro, caso isso não ocorra ele retorna para o login
    if 'usuario_cadastrado' not in session or session['usuario_cadastrado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioPessoa()
    # render_template mostra na tela o html
    return render_template('novo.html', titulo='Cadastrar', form=form)

# esta capturando as informações do form


@app.route('/criar', methods=['POST',])
# é um redirecionamento para mandar os dados para a lista.html /
def criar():
    # pego o formulario criado, depois verifico se ele foi validado
    form = FormularioPessoa(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('novo'))
    # requisição para pegar exatamente o que esta no codigo html,porem como mudamos para o fwt o request.form['nome vai ser substituido]
    nome = form.nome.data
    idade = form.idade.data
    sexo = form.sexo.data
    # fazendo uma consulta se ja tem algum nome na tabela pessoas igual a pessoa adicionada na variável nome acima.
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    if pessoa:
        flash('Pessoa ja cadastrada')
        return redirect(url_for('index'))

    nova_pessoa = Pessoas(nome=nome, idade=idade, sexo=sexo)
    # agora tenho que adicionar o objeto nova_pessoa que gera essas novas pessoas cadasrtradas no BD
    # session é usado para fazer transaçoes no banco de dados, ou seja quando for fazer alguma mudança
    db.session.add(nova_pessoa)
    # commit serve para fazer as mudanças
    db.session.commit()

    return redirect(url_for('index'))

# <int:id> ta passando para rota a indormação criada no lista.html no botao editar que vai redirecionar para pagina editar.html, ele nao vai so redirecionar como passar tambem a informação do id daquele usuario cadastrado na lista.html


@app.route('/editar/<int:id>')
def editar(id):
    # verificando se o usuario passou pelo login para poder ter acesso a pagina que cria  um novo cadastro, caso isso não ocorra ele retorna para o login
    if 'usuario_cadastrado' not in session or session['usuario_cadastrado'] == None:
        return redirect(url_for('login', proxima=url_for('editar',id=id)))
    pessoa = Pessoas.query.filter_by(id=id).first()
    # aqui tambem tenho que passar o metodo wtf para o formulario
    form = FormularioPessoa()
    form.nome.data = pessoa.nome
    form.idade.data = pessoa.idade
    form.sexo.data = pessoa.sexo
    # render_template mostra na tela o html
    return render_template('editar.html', titulo='Editar cadastros', id=id, form=form)


@app.route('/atualizar',  methods=['POST'],)
def atualizar():
    form = FormularioPessoa(request.form)
    if form.validate_on_submit():
        pessoa = Pessoas.query.filter_by(id=request.form['id']).first()
        pessoa.nome = form.nome.data
        pessoa.idade = form.idade.data
        pessoa.sexo = form.sexo.data

        db.session.add(pessoa)
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_cadastrado' not in session or session['usuario_cadastrado'] == None:
        return redirect(url_for('login'))
    Pessoas.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')
    return redirect(url_for('index'))


