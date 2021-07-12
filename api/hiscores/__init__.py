from flask import Flask


def create_app():
    # Creates the Flask app, with the API blueprint """
    app = Flask(__name__)

    from .api import bp_api
    from .web import web_bp
    
    app.register_blueprint(bp_api, url_prefix="/api")
    app.register_blueprint(web_bp)
    return app
