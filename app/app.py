from config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


app_config = Config()
app = create_app(app_config)

db = SQLAlchemy(app)
