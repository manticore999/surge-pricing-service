from src.config import Config

class PricingService:
    def __init__(self):
        self.config = Config()
    
    def calculate_surge(self, active: int, drivers: int) -> float:
        if drivers == 0:
            return self.config.MAX_SURGE
        
        ratio = active / drivers
        
        if ratio <= 1:
            return self.config.SURGE_THRESHOLDS['balanced']
        elif ratio <= 1.5:
            return self.config.SURGE_THRESHOLDS['low_demand']
        elif ratio <= 2.0:
            return self.config.SURGE_THRESHOLDS['moderate_demand']
        else:
            return self.config.SURGE_THRESHOLDS['high_demand']