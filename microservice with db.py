from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_file.db'
db = SQLAlchemy(app)
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/menu', methods=['GET'])
def get_pizza_menu():
    pizzas = Pizza.query.all()
    pizza_menu = {pizza.id: {"name": pizza.name, "size": pizza.size, "price": pizza.price} for pizza in pizzas}
    return jsonify(pizza_menu)

if __name__ == "__main__":
    app.run(port=8001)
