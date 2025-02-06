import smtplib, ssl
import os
from dotenv import load_dotenv


load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    # Use the environment variable to get the password
    sender_email = "jefkint20@gmail.com"
    password = os.getenv('EMAIL_PASSWORD')
    receiver_email = "jefkint20@gmail.com"

    if not password:
        raise ValueError("EMAIL_PASSWORD environment variable not set")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



