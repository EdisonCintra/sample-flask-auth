import os
from flask import Flask, jsonify, request
from database import db
from flask_login import LoginManager, login_user, current_user, login_required
from models import user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login' #?

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user) #autenticação
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso."})
    return jsonify({"message": "Credenciais inválidas."}), 400


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso."})


@app.route("/user", methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        username = User(username=username, password=password)
        db.session.add(username)
        db.session.commit()
        jsonify({ "message" : "Usuário cadastrado com sucesso."})

    return jsonify({"message": "Dados inválidos."}), 400


@app.route("/user/<int:id_user>", methods=['GET'])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)
    if user:
        return {"username" : user.username}

    return jsonify({"message" : "Usuário não encontrado."}), 404
 

@app.route("/user/<int:id_user>", methods=['PUT'])
@login_required
def update_user(id_user):
    data = required.json
    user = User.query.get(id_user)
    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify({"username" : f"Usuário {id_user} atualizado com sucesso"})

    return jsonify({"message" : "Usuário não encontrado."}), 404




@app.route("/user/<int:id_user>", methods=['DELETE'])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)
    if id_user == current_user.id:
        return jsonify({"message" : "Você não pode deletar a si mesmo."}), 403
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message" : f"Usuário {id_user} deletado com sucesso."})

    return jsonify({"message" : "Usuário não encontrado."}), 404



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


