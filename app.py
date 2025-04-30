from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
# Session <- conexao ativa

@app.route("/", methods=["GET"])
def hello_world():
    return "Beautiful"

if __name__ == "__main__":
    app.run(debug=True)
