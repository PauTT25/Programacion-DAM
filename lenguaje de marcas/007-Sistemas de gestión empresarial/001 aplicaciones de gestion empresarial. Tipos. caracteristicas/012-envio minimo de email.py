import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587          # 587 = STARTTLS, 465 = SSL
SMTP_USER = "user@example.com"
SMTP_PASS = "password"

msg = EmailMessage()
msg["From"] = "pau.contreras.romero@gmx.es"
msg["To"] = "pau.contreras.romero@gmx.es"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola esto es una prueba desde Python.\n")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")

