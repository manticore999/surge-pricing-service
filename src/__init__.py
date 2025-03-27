from flask import Flask
from src.config import Config
from src.routes.surge_routes import surge_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(surge_bp)
    
    # Add error handlers
    @app.errorhandler(404)
    def not_found(e):
        return {'error': 'Endpoint not found'}, 404
    
    return app