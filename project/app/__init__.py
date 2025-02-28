from flask import Flask
from flask_migrate import Migrate
from .extensions import db, jwt, cache, limiter, celery
from .routes.auth import auth_bp
from .routes.ai import ai_bp
from .routes.admin import admin_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
        JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY'),
        UPLOAD_FOLDER='uploads',
        CELERY_BROKER_URL=os.getenv('REDIS_URL')
    )
    
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(ai_bp, url_prefix='/ai')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    celery.conf.update(app.config)
    
    @app.before_request
    def log_request_info():
        app.logger.debug(f"Request: {request.method} {request.path}")
    
    return app

app = create_app()
