import os
from flask import Flask, jsonify, request
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if login and password:
        pass

    return jsonify({"message": "Credenciais inválidas."}), 400

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Flask rodando no Firebase Studio 🎉"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


