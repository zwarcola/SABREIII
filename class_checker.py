from lib import login, searchCourse
from app import show_gui


if __name__ == '__main__':

    credentials = show_gui()

    # driver = login(credentials)
    # availibleSeats = searchCourse(credentials, driver)

    if (availibleSeats > 0):

        message = """\
        Subject: Your class is open!

         There are """ + availibleSeats + """seats availble. You're Welcome."""

        if (credentials["carrier"] == "AT&T"):
            receiver = credentials["phone_num"] + "@txt.att.net"
        elif (credentials["carrier"] == "Verizon"):
            receiver = credentials["phone_num"] + "@vtext.com"
        elif (credentials["carrier"] == "Sprint"):
            receiver = credentials["phone_num"] + "@messaging.sprintpcs.com"
        elif (credentials["carrier"] == "T-Mobile"):
            receiver = credentials["phone_num"] + "@tmomail.net"

        if credentials["notif"] == "Email":
            send_email(credentials["email"], message)
        elif credentials["notif"] == "Text":
            send_text(receiver, message)
        else:
            send_email(credentials["email"], message)
            send_text(receiver, message)
