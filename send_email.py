import smtplib, ssl

port = 465  # For SSL
receiver_email = input("Type email and press enter: ")
receiver_number = input("Enter your phone number: ")
receiver_carrier = input("Enter your phone carrier: ")

if (receiver_carrier == "AT&T"):
    receiver = receiver_number + "@txt.att.net"
elif (receiver_carrier == "verizon"):
    receiver = receiver_number + "@vtxt.com"
elif (receiver_carrier == "sprint"):
    receiver = receiver_number + "@messaging.sprintpcs.com"
elif (receiver_carrier == "t-mobile"):
    receiver = receiver_number + "@tmomail.net"

sender_email = "SABREIIIHackTCNJ2020@gmail.com"
message = """\
Subject: Your class is open!

Your Welcome."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("SABREIIIHackTCNJ2020@gmail.com", "Hacktcnj2020")
    server.sendmail(sender_email, receiver_email, message)
    server.sendmail(sender_email, receiver, message)
