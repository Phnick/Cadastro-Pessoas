from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, SubmitField,PasswordField
from wtforms.validators import DataRequired, NumberRange

# isso ajuda na segurança dos dados e na validação ou seja mostra que os campos possuem um padrao de preenchimento


class FormularioPessoa(FlaskForm):
    nome = StringField('Nome da pessoa', [validators.DataRequired(), validators.Length(min=1, max=50)])
    idade = IntegerField('Idade', [validators.DataRequired(), NumberRange(min=1, max=100)])
    sexo = StringField('Sexo', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nome_usuario = StringField('Nome de usuário', [validators.DataRequired(), validators.Length(min=1, max=20)])
    senha = PasswordField('Senha',[validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
