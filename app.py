import PySimpleGUI as sg
from send_email import send_text, send_email

sg.theme('BlueMono')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('SabreIII')],
            [sg.Text('Enter TCNJ Username:'), sg.InputText()],
            [sg.Text('Enter Password:'), sg.InputText()],
            [sg.Text('Course Subject:'), sg.InputText()],
            [sg.Text('Course Number:'), sg.InputText()],
            [sg.Text('Semester Year:'), sg.InputText()],
            [sg.Text('Semester Season:'), sg.Combo(['Fall', 'Winter', 'Spring', 'Summer'])],
            [sg.Text('Phone Provider:'), sg.Combo(['AT&T', 'Verizon', 'Sprint', 'T-mobile'])],
            [sg.Text('Phone Number:'), sg.InputText()],
            [sg.Text('Receiving Email:'), sg.InputText()],
            [sg.Text('Notifications:'), sg.Combo(['Both', 'Email', 'Text'])],
            [sg.Button('Submit'), sg.Button('Cancel')] ]

message = """\
Subject: Your class is open!

Your Welcome."""

# Create the Window
window = sg.Window('SabreIII GUI', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    credentials =	{
        "username": values[0],
        "password": values[1],
        "subject": values[2],
        "number": values[3],
        "year": values[4],
        "semester": values[5],
        "carrier": values[6],
        "phone": values[7],
        "email": values[8],
        "notif":values[9]
    }
    print(credentials)
    if (credentials["carrier"] == "AT&T"):
        receiver = credentials["phone"] + "@txt.att.net"
    elif (credentials["carrier"] == "Verizon"):
        receiver = credentials["phone"] + "@vtext.com"
    elif (credentials["carrier"] == "Sprint"):
        receiver = credentials["phone"] + "@messaging.sprintpcs.com"
    elif (credentials["carrier"] == "T-Mobile"):
        receiver = credentials["phone"] + "@tmomail.net"

    if credentials["notif"] == "Email":
        send_email(credentials["email"], message)
    elif credentials["notif"] == "Text":
        send_text(receiver, message)
    else:
        send_email(credentials["email"], message)
        send_text(receiver, message)

window.close()
