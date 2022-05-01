import smtplib
import datetime

MY_EMAIL = ""
PASS = ""


class NotificationManager:
    def __init__(self):
        self.price = 0
        self.departure_City_Name = ""
        self.departure_Airport_IATA_Code = ""
        self.arrival_City_Name = ""
        self.arrival_Airport_IATA_Code = ""
        self.outbound_Date = ""
        self.x = ""
        self.inbound_Date = ""
        self.y = ""

    def send_mail(self,price, departure_City_Name, departure_Airport_IATA_Code, arrival_City_Name, arrival_Airport_IATA_Code, outbound_Data, inbound_Date, first, email):
        self.x = datetime.datetime.strptime(f'{outbound_Data}', '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
        self.y = datetime.datetime.strptime(f'{inbound_Date}', '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
        message = f"Low Price Alert! Only ${price} to fly from " \
                  f"{departure_City_Name}-{departure_Airport_IATA_Code} to {arrival_City_Name}-" \
                  f"{arrival_Airport_IATA_Code}, from {self.x} to {self.y} "

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Hi {first},"
                                                                                              f" New flight "
                                                                                          f"price\n\n{message}")
        self.outbound_Date = ""
        self.inbound_Date = ""
