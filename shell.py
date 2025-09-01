from main import app
from database import db
from models.user import User


with app.app_context():
    # Criação do banco de dados
    db.create_all()  
    print('BD CRIADO')   
    
    user = User(username='admin', password='123')
    db.session.add(user) #add
    db.session.commit() #salvar
    print('Usuário criado')