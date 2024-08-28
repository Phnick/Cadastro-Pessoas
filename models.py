
from main import db

# criando as classes 'models' que vao ser a ponte do codigo python com o BD

class Pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Usuarios(db.Model):
    nome = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome
