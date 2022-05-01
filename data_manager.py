import requests
import pprint

SHEETY_URL = "https://api.sheety.co/*********/flighDeals"
PARAMS = {
    "Authorization": ""
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.new_price = 0
        self.id = 0
        self.users = {}

    def read_data(self):
        r = requests.get(url=f"{SHEETY_URL}/prices", headers=PARAMS)
        d = r.json()
        self.destination_data = d["prices"]
        return self.destination_data

    def put_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_URL}/pices/{city['id']}", json=new_data, headers=PARAMS)

    def put_new_price(self):
        new_price = {
            "price": {
                "lowestPrice": self.new_price
            }
        }

        response = requests.put(url=f"{SHEETY_URL}/prices/{self.id}", json=new_price, headers=PARAMS)

    def get_users(self):
        r = requests.get(url=f"{SHEETY_URL}/users", headers=PARAMS)
        d = r.json()
        users = d["users"]
        print(users)
        return users

    def add_user(self, first, last, email):
        body = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }
        r = requests.post(url=f"{SHEETY_URL}/users", headers=PARAMS, json=body)


