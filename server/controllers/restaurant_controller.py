from flask import Blueprint, jsonify, request
from ..app import db
from ..models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    return jsonify(restaurant.to_dict(include_pizzas=True)), 200

@restaurant_bp.route('', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    if not name or not address:
        return jsonify({'errors': ['Name and address are required']}), 400
    restaurant = Restaurant(name=name, address=address)
    db.session.add(restaurant)
    db.session.commit()
    return jsonify(restaurant.to_dict()), 201

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return {"error": "Restaurant not found"}, 404
    db.session.delete(restaurant)
    db.session.commit()
    return {}, 204

