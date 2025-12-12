from flask import Blueprint, request, jsonify
from uuid import uuid4

todos_bp = Blueprint("todos", __name__, url_prefix="/todos")
TASKS = {}

@todos_bp.get("/")
def get_todos():
    return jsonify(list(TASKS.values())), 200

@todos_bp.post("/")
def create_todo():
    data = request.get_json()
    todo_id = str(uuid4())

    todo = {"id": todo_id, "title": data.get("title"), "done": False}
    TASKS[todo_id] = todo

    return jsonify(todo), 201

@todos_bp.put("/<todo_id>")
def update_todo(todo_id):
    if todo_id not in TASKS:
        return {"error": "Task not found"}, 404

    data = request.get_json()
    TASKS[todo_id].update(data)
    return jsonify(TASKS[todo_id]), 200

@todos_bp.delete("/<todo_id>")
def delete_todo(todo_id):
    if todo_id in TASKS:
        del TASKS[todo_id]
        return "", 204

    return {"error": "Task not found"}, 404
