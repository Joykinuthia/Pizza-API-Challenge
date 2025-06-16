from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models import db

# Create a Blueprint for the restaurant controller
restaurant_bp = Blueprint('restaurant_bp', __name__)

# Route to get all restaurants
@restaurant_bp.route('/restaurants', methods=['GET'])