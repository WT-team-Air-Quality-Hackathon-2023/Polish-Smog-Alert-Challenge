import json
import os

import requests

from models.air_pollution import AirPollutionData

class AirPollutionService:
    _api_token = os.getenv('API_TOKEN')

    def get_full_address(self, lat, lng) -> str:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={self._api_token}"
        response = requests.request("GET", url)
        return response.json()["results"][0]["formatted_address"]

    def get_air_pollution(self, lat, lng):
        url = f"https://airquality.googleapis.com/v1/history:lookup?key={self._api_token}"
        payload = json.dumps({
            "hours": 336,
            "extraComputations": [
                "POLLUTANT_CONCENTRATION"
            ],
            "pageSize": 168,
            "location": {
                "latitude": lat,
                "longitude": lng
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }        
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        hourly_data = response.json()["hoursInfo"]
        current_value = hourly_data[0]["indexes"][0]["aqi"]
        cumulative_value = sum(h["indexes"][0]["aqi"] for h in hourly_data if "indexes" in h)
        lungs_coverage = self.compute_lungs_coverage(cumulative_value)
        return AirPollutionData(
            current_value=current_value, 
            cumulative_value=cumulative_value, 
            lungs_coverage=lungs_coverage,
            address=self.get_full_address(lat, lng)
        )
    
    def compute_lungs_coverage(self, cumulative_value):
        # TODO replace with more accurate formula based on real data from PSA campaigns
        CUMULATIVE_INDEX_VAUE_FOR_MAX_LUNGS_COVERAGE = 10000
        return min(1.0, cumulative_value / CUMULATIVE_INDEX_VAUE_FOR_MAX_LUNGS_COVERAGE)
