from flask import Blueprint, request, jsonify
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

# Create a Blueprint for the restaurant pizza controller
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)
# Route to add a pizza to a restaurant
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
# Add a pizza to a restaurant
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    if not rp.is_valid():
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    db.session.add(rp)
    db.session.commit()

    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza.id,
        "restaurant_id": rp.restaurant.id,
        "pizza": {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        },
        "restaurant": {
            "id": rp.restaurant.id,
            "name": rp.restaurant.name,
            "address": rp.restaurant.address
        }
    }), 201