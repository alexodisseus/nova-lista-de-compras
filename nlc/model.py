from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Instância do SQLAlchemy
db = SQLAlchemy()

def configure(app):
    """Função para configurar a aplicação Flask com o SQLAlchemy"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Defina seu banco de dados (SQLite)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilitar modificações de rastreamento
    db.init_app(app)  # Inicializa o SQLAlchemy com a app Flask

# Definindo o modelo User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Função para criar um novo usuário
def create_user(name, password, email):
    # Verificar se o email já está em uso
    user = User.query.filter_by(email=email).first()
    if user:
        return False  # Email já existe

    # Criptografar a senha antes de salvar
    hashed_password = generate_password_hash(password, method='sha256')

    # Criando o novo usuário
    new_user = User(username=name, email=email, password=hashed_password)

    # Adicionar o usuário ao banco de dados
    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()  # Reverte qualquer mudança se houver erro
        return False

# Função para buscar um usuário pelo email
def read_user(email):
    return User.query.filter_by(email=email).first()
