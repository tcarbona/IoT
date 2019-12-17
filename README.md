# IoT
OVERVIEW:
This directory contains 2 files that need to be run with python3.
The file manage.py sets up the Django server to display the data.
The file controller.py sets the IOs, reads the data and processes the data. The data and output is then passed onto the Django server.

INSTRUCTIONS FOR RUNNING:
In 2 separate terminal windows (both pointing to this directory level), you must do the following:
In the first window, use the command "python3 manage.py runserver"
In the second window, use the command "sudo python3 controller.py"
