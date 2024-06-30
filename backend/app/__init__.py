# app/__init__.py

from flask import Flask
from app.services.xml_parser import parse_xml_folder

def create_app():
    app = Flask(__name__)
    
    # Load bus data once when the app starts
    app.config['BUS_DATA'] = parse_xml_folder('app/data')
    
    from .routes.timetable import timetable_bp
    from .routes.fare import fare_bp
    
    app.register_blueprint(timetable_bp)
    app.register_blueprint(fare_bp)
    
    return app