from pydantic import BaseModel, confloat

class Location(BaseModel):
    lat: confloat(ge=-90, le=90)
    lng: confloat(ge=-180, le=180)

class SurgeResponse(BaseModel):
    location: Location
    activeRequests: int
    availableDrivers: int
    surge_multiplier: float