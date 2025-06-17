from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS 
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)  

    # Import and register blueprints
    from .controllers.restaurant_controller import restaurant_bp
    from .controllers.pizza_controller import pizza_bp
    from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    @app.route("/")
    def index():
        return "<h1>🍕 Pizza API is Running!</h1>"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
