from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class AirPollutionData:
    current_value: float
    cumulative_value: float
    lungs_coverage: float
    address: str


class AirPollutionRequest(BaseModel):
    latitude: float
    longitude: float