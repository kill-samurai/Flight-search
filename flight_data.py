from notification_manager import NotificationManager
import requests
import datetime as dt
HEADER = {
    "apikey": ""
}

TEQUILA_URI = "https://tequila-api.kiwi.com/v2/search?"
class FlightData:
    def __init__(self):

        self.dt = dt.datetime.now() # date now

        self.tomorrows_date = self.dt + \
            dt.timedelta(days=1) # tomorrows date

        self.six_months = self.dt + \
                     dt.timedelta(days=6*30) # date 6 months from now

        self.formatted_tomorrow = self.tomorrows_date.strftime("%d/%m/%Y") # dd/mm/yyyy
        self.formatted_six_months = self.six_months.strftime("%d/%m/%Y") # dd/mm/yyyy
        self.parameters = {
            "fly_from": "SDQ",
            "fly_to": "",
            "date_from": f"{self.formatted_tomorrow}",
            "date_to": f"{self.formatted_six_months}",
            "curr": "USD",
            "sort": "price",
            "limit": 1,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
        }
        self.data = {}

    def price_search(self, iata):
        self.parameters["fly_to"] = iata
        try:
            r = requests.get(url=TEQUILA_URI, headers=HEADER, params=self.parameters)
            d = r.json()
            data = d["data"][0]
            #pprint.pprint(data)
            self.data = data

        except IndexError:
            return "no flight"
        else:
            return data["price"]

    def send_email(self, first, email):
        NotificationManager().send_mail(price=self.data["price"], departure_City_Name=self.data["cityFrom"],
                            departure_Airport_IATA_Code=self.data["flyFrom"], arrival_City_Name=self.data["cityTo"],
                            arrival_Airport_IATA_Code=self.data["flyTo"],
                            outbound_Data=self.data["route"][0]["local_departure"],
                            inbound_Date=self.data["route"][-1]["local_departure"], first=first, email=email)

