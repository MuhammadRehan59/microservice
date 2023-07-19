from flask import Flask, jsonify

app = Flask(__name__)

pizza_menu = {
    1: {"name": "Margherita", "size": "Medium", "price": 10.99},
    2: {"name": "Pepperoni", "size": "Large", "price": 12.99},
    3: {"name": "Vegetarian", "size": "Medium", "price": 11.99},
}

@app.route('/menu', methods=['GET'])
def get_pizza_menu():
    return jsonify(pizza_menu)

if __name__ == "__main__":
    app.run(port=8001)





