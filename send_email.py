import smtplib, ssl

port = 465  # For SSL
receiver_email = input("Enter your email: ")
receiver_number = input("Enter your phone number: ")
receiver_carrier = input("Enter your phone carrier: ")

if (receiver_carrier == "AT&T"):
    receiver = receiver_number + "@txt.att.net"
elif (receiver_carrier == "verizon"):
    receiver = receiver_number + "@vtext.com"
elif (receiver_carrier == "sprint"):
    receiver = receiver_number + "@messaging.sprintpcs.com"
elif (receiver_carrier == "t-mobile"):
    receiver = receiver_number + "@tmomail.net"

message = """\
Subject: Your class is open!

Your Welcome."""

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

#send_email(receiver_email, message)
send_text(receiver, message)
