# Django_CRUD_Project
This is CRUD based project using Django framework, where you can add, edit,delete of a person or employee or student information.

## Installing
Step by step commands on how to run this project on your computer.

1)- Install Virtualenv
```
pip install virtualenv
```
2)- Create Virtualenv
```
virtualenv venv
```
3)- Activate virtual env
```
source env/bin/activate
```
4)- Install requirements
```
pip install -r requirements.txt
```
Note: Above lines are required for first time installation.

5)- Execute below commands
```
python manage.py makemigrations
python manage.py migrate
```
Note: Above commands should be executed if there is any db level changes

6)- Create superuser for admin access and follow instruction, if not created one
```
python manage.py createsuperuser
```
## Running the server
```
python manage.py runserver
```
And the project is ready for use on your computer!.

## Screenshot of the project
Home Page:
<img width="1440" alt="Screenshot 2023-05-25 at 7 45 38 PM" src="https://github.com/Ajyrajput-2811/Django_CRUD_Project/assets/119350384/9b9d3e4c-f743-49f4-9fd9-11900950ea08">

Update Page:
<img width="1440" alt="Screenshot 2023-05-25 at 7 45 53 PM" src="https://github.com/Ajyrajput-2811/Django_CRUD_Project/assets/119350384/c6844143-1c10-4ef3-acd3-ba1ce9b63516">






