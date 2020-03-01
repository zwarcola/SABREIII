import PySimpleGUI as sg
from send_email import send_text, send_email


def show_gui():

    sg.theme('BlueMono')	# Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('User Input')],
                [sg.Text('TCNJ Username:', size=(16, 1)), sg.InputText()],
                [sg.Text('Password:', size=(16, 1)), sg.InputText()],
                [sg.Text('Course Subject:', size=(16, 1)), sg.Combo(['ACC', 'AAS', 'ASL', 'ANT', 'ARA', 'AAE', 'AAH', 'AAV', 'BIO', 'BME', 'BUS', 'CCS', 'CHE', 'CHI', 'CIV', 'CLS', 'COM', 'CMP', 'CSC', 'COUN', 'CWR', 'CRI', 'CURR', 'DFHH', 'DHH', 'ECE', 'ECED', 'ECO', 'EDAD', 'SED', 'EDUC', 'EDFN', 'EFN', 'EDIN', 'EPSY', 'SUPV', 'ELC', 'ELE', 'ELEM', 'ENG', 'ENGL', 'EED', 'LNG', 'ESLM', 'ESE', 'ENV', 'FIN', 'FRE', 'FSP', 'GER', 'GRE', 'HES', 'HIS', 'HED', 'HGS', 'HON', 'HSS', 'ISTG', 'IST', 'SCI', 'IMM', 'IDS', 'INB', 'INTL', 'INT', 'ITL', 'JPN', 'JPW', 'LAC', 'LAT', 'LIT', 'MGTG', 'MGT', 'MKT', 'MST', 'MAT', 'MATH', 'MTT', 'MEC', 'MSCI', 'MUS', 'NUR', 'NURS', 'PBHR', 'PBHG', 'PHL', 'PHY', 'POL', 'VCPD', 'PSY', 'PBH', 'RDLG', 'RAL', 'REGS', 'REL', 'RUS', 'SAFT', 'AMM', 'SCED', 'SOM', 'SOC', 'SPA', 'SPE','SPED','SLP', 'STA', 'TST', 'TED', 'ETE', 'VPA', 'WGS', 'WGST', 'WLC', 'WRI', 'STEM'])],
                [sg.Text('Course Number:', size=(16, 1)), sg.InputText()],
                [sg.Text('Semester Year:', size=(16, 1)), sg.InputText()],
                [sg.Text('Semester Season:', size=(16, 1)), sg.Combo(['Fall', 'Winter', 'Spring', 'Summer'])],
                [sg.Text('Phone Provider:', size=(16, 1)), sg.Combo(['AT&T', 'Verizon', 'Sprint', 'T-mobile'])],
                [sg.Text('Phone Number:', size=(16, 1)), sg.InputText()],
                [sg.Text('Receiving Email:', size=(16, 1)), sg.InputText()],
                [sg.Text('Notifications:', size=(16, 1)), sg.Combo(['Both', 'Email', 'Text'])],
                [sg.Text('Recurrence:', size=(16, 1)), sg.InputText(), sg.Text('Minutes')],
                [sg.Button('Submit'), sg.Button('Cancel')] ]

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
        #window.close()
        return credentials
