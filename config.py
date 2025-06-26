"""
Configurações da aplicação Flask
"""

import os

class Config:
    """Configurações base da aplicação"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-sistema-ponto-2025')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    
    # Diretório base do projeto
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Configuração do banco de dados
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "instance", "dados.db")}'

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

# Configuração padrão
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
