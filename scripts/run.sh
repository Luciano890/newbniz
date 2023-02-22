#!/bin/bash

# This script is used to run the application in the development environment.
python newbniz/manage.py migrate
python newbniz/manage.py runserver 0.0.0.0:$PORT