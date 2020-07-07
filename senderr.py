import smtplib
import ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "i15.piorkowski@gmail.com"
receiver_email = "adam977p@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

You did it you son of the bitch you did it."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)