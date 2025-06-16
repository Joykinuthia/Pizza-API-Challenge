from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models import db

# Create a Blueprint for the restaurant controller
restaurant_bp = Blueprint('restaurant_bp', __name__)

# Route to get all restaurants
@restaurant_bp.route('/restaurants', methods=['GET'])
# Get all restaurants
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'address': r.address
    } for r in restaurants])

# Route to get a restaurant by ID
@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
# Get a restaurant by ID
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients
        } for rp in restaurant.restaurant_pizzas]
    })

# Route to delete  a restaurant
@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE']) 
# Delete a restaurant
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
