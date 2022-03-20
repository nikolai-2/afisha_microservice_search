from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv


load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)

    register_extensions(app)
    register_blueprint(app)

    return app


def register_extensions(app):
    swagger = Swagger(app, template=init_swagger())


def register_blueprint(app):
    from .search.views import search_module
    from .error.views import error_module

    app.register_blueprint(search_module)
    app.register_blueprint(error_module)


def init_swagger():
    template = dict(
        info={
            "openapi": "3.0.3",
            "info": {
                "title": "Petrenko API",
                "description": "Kostyl",
                "version": "0.0.0"
            }
        }
    )
    return template