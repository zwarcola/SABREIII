import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")
sender_email = "varonea1njtg@gmail.com"
receiver_email = "varonea14@gmail.com"
message = """\
Subject: Your Class is Open!

Your Welcome."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("varonea1njtg@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
