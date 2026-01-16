import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_dificil_de_adivinar'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # Descomentar cuando integremos DB
    DEBUG = True
