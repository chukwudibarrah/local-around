from flask import Blueprint, request, jsonify, current_app

fare_bp = Blueprint('fare_bp', __name__)

@fare_bp.route('/fare', methods=['GET'])
def get_fare():
    start_location = request.args.get('start')
    end_location = request.args.get('end')
    if not start_location or not end_location:
        return jsonify({'error': 'Missing required parameters'}), 400

    bus_data = current_app.config['BUS_DATA']
    fare_info = [bus for bus in bus_data if bus['start'] == start_location and bus['end'] == end_location]
    
    if fare_info:
        return jsonify({
            'start': start_location,
            'end': end_location,
            'fare': fare_info[0]['fare'],
            'timetable': fare_info[0]['timetable']
        })
    else:
        return jsonify({'error': 'No fare information found for the given route'}), 404
    