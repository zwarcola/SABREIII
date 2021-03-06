# SABRE III Peoplesoft App

Super Automated Browser Requesting Enrollment or SABRE III is an application designed to give students notifications based on if a class they with to enroll in has opened up. It is common for students to miss getting in to a class during enrollment, when they do, SABRE III is here to automatically monitor the status of the availible seats in the class. If a seat is found to be availible, the user is notified via text, email, or both about the opening. An example of the program with the user info inserted is displayed below.

<div align="center">
    <img src="Screenshots/SABRE_III_GUI.jpg" width="1982px"></img>
</div>


## Using on Mac

Prerequisites: brew and python3
Follow this link:  https://docs.python-guide.org/starting/install3/osx/ to install brew and python3. Once they are both installed. Verify that python3 is installed by running "$ python3 --version". The command should return your python version. Next run mac_install.sh by doing "$ ./mac_install.sh requirements.txt". To run the class checker, do "$ python3 class_checker.py".

## Using on Windows

Download the source code from https://github.com/zwarcola/SABREIII, be sure to have the latest version of Python3. Once installed, run the program by executing the file "class_checker.py" by running the following command.
```
python class_checker.py
```
When opened, you will be prompted to enter your PAWS information as well as the course number. Note that this course number is the 5-digit code associated with the class name and section **NOT** the 3-digit code associated with the course type. A screenshot of where to find this code is shown below. Enter the information and click *Submit* in order to begin the program. From here, the program will check every 30 minutes if a course is availible. It is recommended to run the program on a device than can be running 24/7 so the application can always be searching.

<div align="center">
    <img src="Screenshots/Course_Number_Locations.jpg" width="3191px"></img>
</div>

## Built With

* Python3 - Source Code and GUI
* Selenium
* PySimpleGUI


## Contributors

* **Jake Bezold** - *Mastermind*
* **Casey Futterman** - *Graphical User Interface*
* **Adam Varone** - *User Notification System*
* **Zachary Warcola** - *Backend Web Navigation*
