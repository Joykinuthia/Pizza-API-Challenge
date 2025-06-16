from flask import Flask
from server.config import Config
from server.models import db
from flask_migrate import Migrate

# Create and configure the Flask application
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    Migrate(app, db)


     # Register blueprints
    
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
