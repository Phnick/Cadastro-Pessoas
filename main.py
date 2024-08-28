
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt


# faz rodar a aplicação
app = Flask(__name__)
# aqui vamos chamasr as config
app.config.from_pyfile('config.py')
# instanciando o banco de dados
db = SQLAlchemy(app)
csrf =CSRFProtect(app)
bcrypt = Bcrypt(app)


from views_cadastro import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)

# app.run(host='0.0.0.0', port=8080)
