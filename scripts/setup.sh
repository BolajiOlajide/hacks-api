#!/bin/bash

set -e

# if any code doesn't return 0, exit the script
set -o pipefail

# print each step of your code to the terminal
set -x


# run migrations for the DB
python manage.py migrate

# create a super user
python manage.py createsuperuser


echo "Setup Complete!"
