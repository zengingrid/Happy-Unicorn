""" Web blueprint. Defines the route /, which shows an HTML page with the list of students """
from flask import Blueprint, render_template
from api.models.score_manager import ScoreManager

web_bp = Blueprint("web", __name__)


@web_bp.route("/")
def index():
    manager = ScoreManager()
    raw_scores = [score.to_json() for score in manager._scores.values()]
    sorted_scores = sorted(raw_scores, key = lambda i: i['score'],reverse=True)
    return render_template("index.html", scores = sorted_scores)
