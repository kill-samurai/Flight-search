import requests

HEADER = {
    "apikey": ""
}

TEQUILA_URI = "https://tequila-api.kiwi.com/locations/query?/"

class FlightSearch:
    def __init__(self):
        self.parameters = {
            "term": "",
            "location_types": "city",
            "active_only": "true",
            "locale": "en-US",
            "limit": 1
        }

    def flight_search(self, term):
        self.parameters["term"] = term
        response = requests.get(url=TEQUILA_URI, params=self.parameters, headers=HEADER)
        data = response.json()
        return data["locations"][0]["code"]