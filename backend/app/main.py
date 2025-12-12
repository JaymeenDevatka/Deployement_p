from flask import Flask
from .routes.health import health_bp
from .routes.todos import todos_bp

def create_app():
    app = Flask(__name__)

    # REGISTER BLUEPRINTS
    app.register_blueprint(health_bp)
    app.register_blueprint(todos_bp)

    return app
