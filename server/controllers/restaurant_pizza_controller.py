from flask import Blueprint, request, jsonify
from ..app import db
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if not pizza or not restaurant:
        return jsonify({'errors': ['Invalid pizza_id or restaurant_id']}), 400

    new_entry = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    db.session.add(new_entry)
    db.session.commit()

    return jsonify({
        'id': new_entry.id,
        'price': new_entry.price,
        'pizza_id': pizza.id,
        'restaurant_id': restaurant.id,
        'pizza': pizza.to_dict(),
        'restaurant': restaurant.to_dict()
    }), 201

@restaurant_pizza_bp.route('', methods=['GET'])
@restaurant_pizza_bp.route('/', methods=['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    return jsonify([{
        **rp.to_dict(),
        'pizza': rp.pizza.to_dict() if rp.pizza else None,
        'restaurant': rp.restaurant.to_dict() if rp.restaurant else None
    } for rp in restaurant_pizzas]), 200
