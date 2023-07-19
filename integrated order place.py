from flask import Flask, jsonify
import requests

app = Flask(__name__)

PIZZA_MENU_URL = "http://localhost:8001/menu"

@app.route('/place_order', methods=['POST'])
def place_order():
    response = requests.get(PIZZA_MENU_URL)
    
    if response.status_code == 200:
        return response.json()
    else:
        return jsonify({"message": "Error retrieving pizza menu."}), 500

if __name__ == "__main__":
    app.run(port=8002)
