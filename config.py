# onde fica as CONFIGURAÇÕES
# necessário para poder usar a session
SECRET_KEY = 'alura'
# dando acesso ao BD ou seja conectando com o banco de dados
SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = 'Ph1140'
servidor = 'localhost'
database = 'cadastros'
SQLALCHEMY_DATABASE_URI = \
    f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'
