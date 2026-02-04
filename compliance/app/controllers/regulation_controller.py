from flask import Blueprint, jsonify, request
from compliance.app.services.regulation_service import RegulationService

regulation_blueprint = Blueprint('regulation', __name__)

@regulation_blueprint.route('/get_applicable_regulations', methods=['GET'])
def get_applicable_regulations():
    region = request.args.get('region')
    if not region:
        return jsonify({'error': 'Region parameter is required'}), 400

    regulations = RegulationService.identify_applicable_regulations(region)
    return jsonify([{'name': reg.name, 'country': reg.country} for reg in regulations]), 200