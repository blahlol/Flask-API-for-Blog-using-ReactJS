from flask import Flask
from .blog import views
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app.register_blueprint(views.blog_bp)
    CORS(app)
    return app

create_app()