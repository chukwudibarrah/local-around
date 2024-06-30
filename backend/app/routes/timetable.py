"""
timetable.py

This module defines routes related to bus timetables.
"""

# app/routes/timetable.py

from flask import Blueprint, request, jsonify, current_app

timetable_bp = Blueprint('timetable_bp', __name__)

@timetable_bp.route('/timetable', methods=['GET'])
def get_timetable():
    start_location = request.args.get('start')
    end_location = request.args.get('end')
    if not start_location or not end_location:
        return jsonify({'error': 'Missing required parameters'}), 400

    bus_data = current_app.config['BUS_DATA']
    timetable_info = [bus for bus in bus_data if bus['start'] == start_location and bus['end'] == end_location]
    
    if timetable_info:
        return jsonify(timetable_info)
    else:
        return jsonify({'error': 'No timetable found for the given route'}), 404
    