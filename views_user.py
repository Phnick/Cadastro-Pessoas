from flask import render_template, request, redirect, session, flash, url_for
from main import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    if proxima == None:
        proxima = url_for('novo')
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    form =FormularioUsuario(request.form)
   
    # uma consulta filtrando se o nome é igual ao que esta sendo fornecido no request.form['usuario'])
    usuario = Usuarios.query.filter_by(nome=form.nome_usuario.data).first()
    # check_password_hash é utilizado para verificar se uma senha fornecida pelo usuário corresponde ao hash da senha armazenado no banco de dados
    senha =check_password_hash(usuario.senha, form.senha.data)

    if usuario and senha:
        session['usuario_cadastrado'] = usuario.nome
        flash(usuario.nome + ' logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)

    else:
        flash('usuário não encontrado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_cadastrado'] = None
    flash('Logout executado com sucesso')
    # url_for é uso de boas praticas para indicar a rota atravez da função
    return redirect(url_for('login'))
