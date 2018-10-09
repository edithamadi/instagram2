# Project Title
This is a simple web clone of the instagram website. A user can create an account and sign into it. The site supports uploading images,liking and commenting on images as well as following other users. Logged in users can view photos uploaded by other users in the home page of app.


# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


Step 1: Clone the repository

Run the following command on the terminal: git clone `git@github.com:edithamadi/instagram2.git 
 
Step 2: Enter the Project root folder

cd instagram2 / install virtual environment (virtual) without pip

`python3.6 -m venv --without-pip virtual ``

Step 3: Activate virtual environment

`source virtual/bin/activate`

install pip using curl

`curl https://bootstrap.pypa.io/get-pip.py` | python run the application

python3.6 manage.py runserver

# Prerequisites
- Ubuntu Software
- Python3.6
- Postgres
- python virtualenv

# Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

# Create the Database
psql
CREATE DATABASE instagram;

# .env file
Create .env file and paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'instagram'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'

# Run initial Migration
python3.6 manage.py makemigrations insta
python3.6 manage.py migrate

# Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

# Running the tests
To run tests run `python3.6 manage.py test`

# Deployment
Deploy site to heroku

# Built With

# Python3.6 
 Python is a programming language that lets you work quickly and integrate systems more effectively 

# Django 
 Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design 

# postgresql 
 PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance. 

# Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

# Authors
Edith Amadi 

# License
This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments
MORINGA SCHOOL