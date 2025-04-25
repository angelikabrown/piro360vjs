from flask import request, jsonify
from models import db, Data

def init_routes(app):
    @app.route('/', methods=['GET'])
    def hi():
        return "Hello, World!"
    
    @app.route('/data', methods=['GET'])
    def get_all_data():
        data = Data.query.all()
        return jsonify([d.to_dict() for d in data])

    @app.route('/api/data', methods=['GET'])
    def get_api_data():
        print("GET /api/data called")
        data = Data.query.all()
        return jsonify([d.to_dict() for d in data])

    @app.route('/api/data/<int:id>', methods=['GET'])
    def get_data_by_id(id):
        print(f"GET /api/data/{id} called")
        data = Data.query.get_or_404(id)
        return jsonify(data.to_dict())

    @app.route('/api/data', methods=['POST'])
    def create_data():
        new_data = Data(
            cycle_day=request.json['cycle_day'],
            temperature=request.json['temperature'],
            mood=request.json['mood'],
            energy=request.json['energy'],
            notes=request.json['notes'],
            date=request.json['date'],
            timestamp=request.json['timestamp']
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_data.to_dict()), 201
    @app.route('/api/data/<int:id>', methods=['PUT'])
    def update_data(id):
        data = Data.query.get_or_404(id)
        data.cycle_day = request.json.get('cycle_day', data.cycle_day)
        data.temperature = request.json.get('temperature', data.temperature)
        data.mood = request.json.get('mood', data.mood)
        data.energy = request.json.get('energy', data.energy)
        data.notes = request.json.get('notes', data.notes)
        data.date = request.json.get('date', data.date)
        data.timestamp = request.json.get('timestamp', data.timestamp)
        db.session.commit()
        return jsonify(data.to_dict())
    @app.route('/api/data/<int:id>', methods=['DELETE'])
    def delete_data(id):
        data = Data.query.get_or_404(id)
        db.session.delete(data)
        db.session.commit()
        return jsonify({'message': 'Data deleted successfully'})
    