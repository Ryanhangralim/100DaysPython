from flight_data import FlightData
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, flight_data : FlightData, email : str, password : str):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user = email, password= password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}/{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}"
            )