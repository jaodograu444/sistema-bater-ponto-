from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tipo = db.Column(db.String(20), nullable=False, default='funcionario')  # 'admin' ou 'funcionario'
    ativo = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamentos com foreign_keys especificadas para evitar ambiguidade
    pontos = db.relationship('Ponto', backref='usuario', lazy=True)
    justificativas = db.relationship('Justificativa', 
                                   foreign_keys='Justificativa.usuario_id',
                                   backref='usuario', lazy=True)
    justificativas_aprovadas = db.relationship('Justificativa',
                                             foreign_keys='Justificativa.aprovado_por',
                                             backref='aprovador', lazy=True)
    horarios = db.relationship('Horario', backref='usuario', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Usuario {self.username}>'

class Ponto(db.Model):
    __tablename__ = 'pontos'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    data = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
    hora_entrada = db.Column(db.Time, nullable=True)
    hora_saida = db.Column(db.Time, nullable=True)
    hora_almoco_saida = db.Column(db.Time, nullable=True)
    hora_almoco_volta = db.Column(db.Time, nullable=True)
    observacoes = db.Column(db.Text, nullable=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Ponto {self.usuario.nome} - {self.data}>'

class Justificativa(db.Model):
    __tablename__ = 'justificativas'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    motivo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pendente')  # 'pendente', 'aprovada', 'rejeitada'
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    aprovado_por = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    data_aprovacao = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Justificativa {self.usuario.nome} - {self.data}>'

class Horario(db.Model):
    __tablename__ = 'horarios'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    dia_semana = db.Column(db.String(20), nullable=False)  # 'segunda', 'terca', etc.
    hora_entrada = db.Column(db.Time, nullable=False)
    hora_saida = db.Column(db.Time, nullable=False)
    hora_almoco_inicio = db.Column(db.Time, nullable=True)
    hora_almoco_fim = db.Column(db.Time, nullable=True)
    ativo = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Horario {self.usuario.nome} - {self.dia_semana}>'