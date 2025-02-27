from flask import Flask, render_template
import os

app = Flask(__name__)

# Configuración de base de datos para Heroku o local
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def home():
    return "<h1>Bienvenido a Mafra Auto Parts</h1>"

if __name__ == '__main__':
    app.run(debug=True)
