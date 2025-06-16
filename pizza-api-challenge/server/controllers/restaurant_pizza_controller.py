from flask import Blueprint, request, jsonify
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

# Create a Blueprint for the restaurant pizza controller
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)
# Route to add a pizza to a restaurant
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])