from flask import Blueprint, request, jsonify

todos_bp = Blueprint("todos", __name__, url_prefix="/todos")

# In-memory DB
TODOS = []

@todos_bp.post("/")
def create_todo():
    data = request.get_json()
    title = data.get("title")

    todo = {"id": len(TODOS) + 1, "title": title}
    TODOS.append(todo)

    return jsonify(todo), 201

@todos_bp.get("/")
def get_todos():
    return jsonify(TODOS), 200
