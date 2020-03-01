from lib import login, searchCourse
from app import show_gui
from send_email import send_text, send_email
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':

    #get credentials from GUI
    credentials = show_gui()

    while(True):

        #send crendentials over to bot and run
        driver = login(credentials)
        availibleSeats = searchCourse(credentials, driver)

        print("Availible seats: " + availibleSeats)

        time.sleep(1)
        driver.close()

        if (int(availibleSeats) > 0):

            message = MIMEMultipart("alternative")
            message["Subject"] = "Your class is open!"

            text = """\
            There are """ + availibleSeats + """ seats(s) available!"""

            message.attach(MIMEText(text, "plain"))
            #There are """ + availibleSeats + """ seat(s) available. Go Register Fast!"""

            if (credentials["carrier"] == "AT&T"):
                receiver = credentials["phone_num"] + "@txt.att.net"
            elif (credentials["carrier"] == "Verizon"):
                receiver = credentials["phone_num"] + "@vzwpix.com"
            elif (credentials["carrier"] == "Sprint"):
                receiver = credentials["phone_num"] + "@messaging.sprintpcs.com"
            elif (credentials["carrier"] == "T-Mobile"):
                receiver = credentials["phone_num"] + "@tmomail.net"

            print(receiver)

            if credentials["notif"] == "Email":
                send_email(credentials["email"], message)
            elif credentials["notif"] == "Text":
                send_text(receiver, message)
            else:
                send_email(credentials["email"], message)
                send_text(receiver, message)

            #if we find the class is open, end the program??
            exit()

        else:
            print("No class found, waiting a little while...")
            time.sleep(30) #if the class isnt found sleep for a period of time and check again
