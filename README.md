# CW6.Django
Project «Mailing Service using Django»
Description
This project provides ability to create a basic mailing service for sending newsletters to the list of recipients. 

User actions:

Create, update, view and delete newsletter
Create, update, view and delete client (recipient )

Manager actions:

View and deactivate newsletter
View and block users
To stop newsletter user or manager has to change its status to finished. Mailing logs are generated and stored automatically in ./logs/logs.txt

Scheduling
Each letter can be scheduled to be sent daily, weekly, or monthly. 
The scheduler runs every minute to track which letters must be sent. The time is determined during newsletter creation.

Create database and make migrations:
python3 manage.py makemigrations
python3 manage.py migrate

Run Django server:
python3 manage.py runserver
