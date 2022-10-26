# Successible-Api

For windows to activate env
1. Go into the Successible-Api repo then run commands
python3 -m venv env
Set-ExecutionPolicy Unrestricted -Scope Process
env\Scripts\activate
2. cd into the api folder
py -m pip install -r requirements.txt 

For mac
1. Go into the Successible-Api repo then run commands
python3 -m venv env  
source env/bin/activate
2. cd into the api folder then run the following
python3 -m pip install -r requirements.txt 

To run the app cd into the api folder and run the following commands

python3 manage.py makemigrations app
python3 manage.py migrate app
python3 manage.py migrate   

python3 manage.py runserver 
