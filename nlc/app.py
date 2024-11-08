import admin
# import shareholder
# import quote
# import itens
import lists
# import people
# from flask_bootstrap import Bootstrap
import model

from flask import Flask
from flask_migrate import Migrate

# Criar instância do Flask
app = Flask(__name__)

# Configuração do título e chave secreta
app.config['TITLE'] = "Nova Lista de Compras"
app.secret_key = b'guerra aos senhores'

# Configuração do banco de dados e migrações
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Defina o URI do seu banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilita o rastreamento de modificações

# Inicializando o db (instância do SQLAlchemy) e o Flask-Migrate
db = model.db  # Obtém a instância do db do model.py
migrate = Migrate(app, db)  # Inicializa o Flask-Migrate



# Configura o modelo com a app
db.init_app(app)


admin.configure(app)
lists.configure(app)

