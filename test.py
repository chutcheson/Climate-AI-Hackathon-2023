from marvin import ai_fn
from pydantic import BaseModel

@ai_model
class Location(BaseModel):
    city: str
    state: str
    country: str
    lat: float
    lon: float

print(Location("The windy city"))
