# onde fica as CONFIGURAÇÕES
# necessário para poder usar a session
from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
# dando acesso ao BD ou seja conectando com o banco de dados
SGBD = 'mysql+mysqlconnector'
usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')
servidor = 'localhost'
database = 'cadastros'
SQLALCHEMY_DATABASE_URI = \
    f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'
