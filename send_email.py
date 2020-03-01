import smtplib, ssl

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(receiver, msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("SABREIIIHackTCNJ2020@gmail.com", "Hacktcnj2020")
        server.sendmail(
            "SABREIIIHackTCNJ2020@gmail.com", receiver, msg.as_string()
        )

def send_text(receiver, msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("SABREIIIHackTCNJ2020@gmail.com", "Hacktcnj2020")
        server.sendmail(
            "SABREIIIHackTCNJ2020@gmail.com", receiver, msg.as_string()
        )
