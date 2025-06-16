from server.models import db
from server.models.restaurant_pizza import RestaurantPizza

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete')