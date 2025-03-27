class Config:
    PORT = 5001
    DEBUG = False
    MAX_SURGE = 2.5
    SURGE_THRESHOLDS = {
        'no_drivers': 2.5,
        'high_demand': 2.0,
        'moderate_demand': 1.5,
        'low_demand': 1.2,
        'balanced': 1.0
    }