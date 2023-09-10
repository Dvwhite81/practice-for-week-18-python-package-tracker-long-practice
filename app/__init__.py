from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .routes import packages
from app.models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(packages.bp)
db.init_app(app)
migrate = Migrate(app, db)
