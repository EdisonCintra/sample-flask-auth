from main import app
from database import db
from models import user 


with app.app_context():
    # Criação do banco de dados
    db.create_all()  
    print('BD CRIADO')   
    