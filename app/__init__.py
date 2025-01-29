from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)

def create_app():
    app = Flask(__name__, static_url_path='/static',)

    CORS(app, resources={
        r"/*": {
            "origins": "*", 
            "methods": ["GET"], 
            "allow_headers": ["Content-Type"]  ##only content type is needed for now.. limited this on purpose
        }
    })


    from .routes import main
    app.register_blueprint(main)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
