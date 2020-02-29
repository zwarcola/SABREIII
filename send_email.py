import smtplib, ssl

port = 465  # For SSL
# receiver_email = input("Enter your email: ")
# receiver_number = input("Enter your phone number: ")
# receiver_carrier = input("Enter your phone carrier: ")

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(receiver, msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("SABREIIIHackTCNJ2020@gmail.com", "Hacktcnj2020")
        server.sendmail("SABREIIIHackTCNJ2020@gmail.com", receiver, msg)

def send_text(receiver, msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("SABREIIIHackTCNJ2020@gmail.com", "Hacktcnj2020")
        server.sendmail("SABREIIIHackTCNJ2020@gmail.com", receiver, msg)
