from flask import Blueprint, jsonify
from server.models.pizza import Pizza

# Create a Blueprint for the pizza controller
pizza_bp = Blueprint('pizza_bp', __name__)

# Route to get all pizzas
@pizza_bp.route('/pizzas', methods=['GET'])