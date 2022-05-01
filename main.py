from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch()
fd = FlightData()
nm = NotificationManager()

get_data = dm.read_data()
user_list = dm.get_users()
emails = [item["email"] for item in user_list]

print("Welcome to Luis's Flifht Club.\nWe find the best flight deals and email it to you.\n")

validation = True
empty = True

while empty:
    first_name = input("What is your first name? ")
    last_name = input("\nWhat is you last name? ")
    if first_name == "" or last_name == "":
        print("Either the first name or the last name is empty, please try again.")
        pass
    else:
        empty = False

while validation:
    email = input("What is your email? ").lower()
    validate_email = input("Please validate your email: ").lower()
    if email == "" or validate_email == "":
        print("Email or Validate email is empty please try again.")
        pass
    else:
        if email == validate_email:
            validation = False
        else:
            print("Incorrect Email, please try again.")

if validate_email in emails:
    pass
else:
    dm.add_user(first=first_name, last=last_name, email=validate_email)
    print("Your user has been added.")

#check if the Iata code is there and update it if is not
for item in get_data:
    if item["iataCode"] == "":
        item["iataCode"] = fs.flight_search(term=item["city"])
        dm.destination_data = get_data
        dm.put_data()

#check Prices and update them if it's there
for item in get_data:
    flight_price = fd.price_search(item["iataCode"])
    if flight_price == "no flight":
        pass
    elif int(flight_price) < int(item["lowestPrice"]):
        item["lowestPrice"] = flight_price
        dm.new_price = flight_price
        dm.id = item['id']
        dm.put_new_price()

updated_user_list = dm.get_users()
print(updated_user_list)
for item in updated_user_list:
    first = item["firstName"]
    last = item["lastName"]
    email = item["email"]
    fd.send_email(first=first, email=email)







