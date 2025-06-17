from .app import create_app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza


app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    r1 = Restaurant(name="Domino's", address="123 Pizza St")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Cheese Ave")

    p1 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p2 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Peppers, Olives, Onions")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=7, pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("✅ Done seeding!")
