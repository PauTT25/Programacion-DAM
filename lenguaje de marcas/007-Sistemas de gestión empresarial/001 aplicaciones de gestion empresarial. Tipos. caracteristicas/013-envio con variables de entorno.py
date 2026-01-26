import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = "smtp.gmx.com"
SMTP_PORT = 587          # 587 = STARTTLS, 465 = SSL
SMTP_USER = "pau.contreras.romero@gmx.es"
SMTP_PASS = "LO4DOV7MQV4JO5TWOSJH"

msg = EmailMessage()
msg["From"] = "pau.contreras.romero@gmx.es"
msg["To"] = "contrerasromeropau@gmail.com"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola esto es una prueba desde Python.\n")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")



