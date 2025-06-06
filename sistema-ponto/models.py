from db import db

class Contato
 __tablename__ = 'contatos'
 nome = db.Column(db.String(50), nullable=False)
 telefone = db.Column(db.Integer, nullable=False)

 