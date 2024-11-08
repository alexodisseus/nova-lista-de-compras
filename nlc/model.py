from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Instância do SQLAlchemy
db = SQLAlchemy()

# Definindo o modelo User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Definindo o modelo Lista
class Lista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)  
    
    tag = db.Column(db.String(120)) 
    data_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    data_closing = db.Column(db.DateTime, nullable=True)  
    
    def __repr__(self):
        return f'<Lista {self.name}>'


# Função para criar um novo usuário
def create_user(name, password, email):
    user = User.query.filter_by(email=email).first()
    if user:
        return False  # Email já existe

    # Criptografar a senha
    hashed_password = generate_password_hash(password, method='sha256')

    # Criar e salvar o novo usuário
    new_user = User(username=name, email=email, password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()  # Reverte se houver erro
        return False

# Função para buscar um usuário pelo email
def read_user(email):
    return User.query.filter_by(email=email).first()
