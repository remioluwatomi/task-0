from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app, resources={
        r"/*": {
            "origins": "*", 
            "methods": ["GET"], 
            "allow_headers": ["Content-Type"]  ##only content type is needed for now.. limited this on purpose
        }
    })


    from .routes import main
    app.register_blueprint(main)

    return app
