class SurgeDataClient:
    def __init__(self):
        # To be replaced later  with actual service calls later
        self.mock_data = {
            (40.7128, -74.0060): (15, 5),  
            (34.0522, -118.2437): (8, 10), 
            (37.7749, -122.4194): (10, 10),  
            (41.8781, -87.6298): (5, 15),  
            (29.7604, -95.3698): (20, 5),  
            (33.4484, -112.0740): (5, 20),  
            (32.7157, -117.1611): (10, 10),  
            (29.9511, -90.0715): (10, 10),  
            (39.7392, -104.9903): (10, 10),  
            (42.3601, -71.0589): (10, 10)
        }
    
    def get_demand_supply(self, lat: float, lng: float) -> tuple[int, int]:
        """Fetch data from other microservices"""
        key = (round(lat, 4), round(lng, 4))
        return self.mock_data.get(key, (0, 0))