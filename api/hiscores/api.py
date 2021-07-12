from flask import Blueprint, jsonify, request
from api.models.score_manager import ScoreManager

bp_api = Blueprint("api", __name__)

@bp_api.route("/scores")
def show_list():
    # Return list of scores in JSON format
    manager = ScoreManager()
    return jsonify([score.to_json() for score in manager._scores.values()])


@bp_api.route("/score/<int:score_id>")
def show_score(score_id):
    # Returns score instance in JSON format
    manager = ScoreManager()
    score = manager.get_score_by_id(score_id)
    if not score:
        return "Score ID not found", 404
    return jsonify(score.to_json())


@bp_api.route("/score", methods=["PUT"])
def create_score():
    # Create a new score instance 
    manager = ScoreManager()
    data = request.get_json()

    if "name" not in data or "score" not in data:
        return "the JSON data is incorrect", 400
    else:
        manager.add_score(name=data["name"], score=data["score"])
        manager.save()
        return "", 204


@bp_api.route("/score/<int:score_id>", methods=["POST"])
def update_score(score_id):
    # Updates score instance based on score ID.
    manager = ScoreManager()
    data = request.get_json()

    if "name" not in data.keys() or 'score' not in data.keys():
            return "JSON data is invalid", 400
    
    for key, value in manager._scores.items():
        if key == score_id:
            score = value
            score._name = data["name"]
            score._score = data["score"]
            manager.save()
            return "", 204
        else:
            return "Score not found", 404
    

@bp_api.route("/score/<int:score_id>", methods=["DELETE"])
def remove_score(score_id):
    # Deletes one student based on their ID.
    manager = ScoreManager()
    score = manager.remove_score_by_id(score_id)
    manager.save()
    if not score:
        return "Score not found", 404
    else:
        return "", 204