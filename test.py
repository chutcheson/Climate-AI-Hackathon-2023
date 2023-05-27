from marvin import ai_model
from marvin import ai_fn
from pydantic import BaseModel

@ai_model
class Location(BaseModel):
    city: str
    state: str
    country: str
    lat: float
    lon: float

@ai_fn
def list_fruits(n: int) -> list[str]:
    """Generate a list of n fruits"""


print(list_fruits(n=3)) # ["apple", "banana", "orange"]

