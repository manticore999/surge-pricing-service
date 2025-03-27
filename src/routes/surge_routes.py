from flask import Blueprint, request
from ..models.schemas import Location, SurgeResponse
from ..data.surge_data import SurgeDataClient
from ..services.pricing_service import PricingService

surge_bp = Blueprint('surge', __name__, url_prefix='/surge')
data_client = SurgeDataClient()
pricing_service = PricingService()

@surge_bp.route('/', methods=['GET'])
def get_surge_multiplier():
    try:
        location = Location(
            lat=request.args.get('lat', type=float),
            lng=request.args.get('lng', type=float)
        )
    except ValueError as e:
        return {'error': str(e)}, 400
    
    active, drivers = data_client.get_demand_supply(location.lat, location.lng)
    multiplier = pricing_service.calculate_surge(active, drivers)
    
    return SurgeResponse(
        location=location,
        activeRequests=active,
        availableDrivers=drivers,
        surge_multiplier=multiplier
    ).dict()