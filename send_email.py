import smtplib, ssl
import os


def send_mail(message):
    host = 'smtp.gmail.com'
    port = smtplib.SMTP_SSL_PORT
    username = 'ksparks0031@gmail.com'
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)


