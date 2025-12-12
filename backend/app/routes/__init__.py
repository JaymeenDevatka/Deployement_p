from flask import Blueprint

# Blueprints for modular routing
health_bp = Blueprint("health", __name__)
todos_bp = Blueprint("todos", __name__)
