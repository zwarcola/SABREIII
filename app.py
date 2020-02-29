import PySimpleGUI as sg
from send_email import send_text, send_email

sg.theme('BlueMono')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('User Input')],
            [sg.Text('TCNJ Username:', size=(16, 1)), sg.InputText()],
            [sg.Text('Password:', size=(16, 1)), sg.InputText()],
            [sg.Text('Course Subject:', size=(16, 1)), sg.InputText()],
            [sg.Text('Course Number:', size=(16, 1)), sg.InputText()],
            [sg.Text('Semester Year:', size=(16, 1)), sg.InputText()],
            [sg.Text('Semester Season:', size=(16, 1)), sg.Combo(['Fall', 'Winter', 'Spring', 'Summer'])],
            [sg.Text('Phone Provider:', size=(16, 1)), sg.Combo(['AT&T', 'Verizon', 'Sprint', 'T-mobile'])],
            [sg.Text('Phone Number:', size=(16, 1)), sg.InputText()],
            [sg.Text('Receiving Email:', size=(16, 1)), sg.InputText()],
            [sg.Text('Notifications:', size=(16, 1)), sg.Combo(['Both', 'Email', 'Text'])],
            [sg.Text('Recurrence:', size=(16, 1)), sg.InputText(), sg.Text('Minutes')],
            [sg.Button('Submit'), sg.Button('Cancel')] ]

message = """\
Subject: Your class is open!

You're Welcome."""

# Create the Window
window = sg.Window('SABREIII', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    credentials =	{
        "username": values[0],
        "password": values[1],
        "subject": values[2],
        "class_num": values[3],
        "year": values[4],
        "semester": values[5],
        "carrier": values[6],
        "phone_num": values[7],
        "email": values[8],
        "notif":values[9],
        "time":values[10]
    }
    print(credentials)
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

window.close()
