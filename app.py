import PySimpleGUI as sg

sg.theme('BlueMono')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('SabreIII')],
            [sg.Text('Enter TCNJ Username:'), sg.InputText()],
            [sg.Text('Enter Password:'), sg.InputText()],
            [sg.Text('Course Subject:'), sg.InputText()],
            [sg.Text('Course Number:'), sg.InputText()],
            [sg.Text('Semester Year:'), sg.InputText()],
            [sg.Text('Semester Season:'), sg.Combo(['Fall', 'Winter', 'Spring', 'Summer'])],
            [sg.Text('Phone Provider:'), sg.Combo(['AT&T', 'Verizon', 'Sprint', 'T-Mobil'])],
            [sg.Text('Phone Number:'), sg.InputText()],
            [sg.Text('Notifications:'), sg.Combo(['Both', 'Email', 'Text'])],
            [sg.Button('Submit'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('SabreIII GUI', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    thisdict =	{
        "username": values[0],
        "password": values[1],
        "subject": values[2],
        "number": values[3],
        "year": values[4],
        "semester": values[5],
        "carrier": values[6],
        "phone": values[7],
        "notif":values[8]
    }
    print(thisdict)



window.close()
