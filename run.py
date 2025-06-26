#!/usr/bin/env python3
"""
Sistema de Ponto Eletrônico
"""

from flask import Flask
from config import config
from models import db, Usuario
from routes import routes

def create_app(config_name='development'):
    """Criar e configurar a aplicação Flask"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    app.register_blueprint(routes)
    
    # Criar tabelas e usuários padrão
    with app.app_context():
        db.create_all()
        criar_usuarios_padrao()
    
    return app

def criar_usuarios_padrao():
    """Criar usuários padrão se não existirem"""
    if Usuario.query.count() > 0:
        return
    
    # Admin padrão
    admin = Usuario(
        username='admin',
        nome='Administrador do Sistema',
        email='admin@empresa.com',
        tipo='admin',
        ativo=True
    )
    admin.set_password('admin123')
    
    # Funcionário padrão
    funcionario = Usuario(
        username='funcionario',
        nome='João da Silva',
        email='joao@empresa.com',
        tipo='funcionario',
        ativo=True
    )
    funcionario.set_password('123456')
    
    db.session.add_all([admin, funcionario])
    db.session.commit()
    print("Usuários padrão criados!")
    print("Admin: admin/admin123 | Funcionário: funcionario/123456")

if __name__ == '__main__':
    print("SISTEMA DE PONTO ELETRÔNICO")
    print("Servidor: http://127.0.0.1:5000")
    app = create_app()
    app.run(host='127.0.0.1', port=5000)
