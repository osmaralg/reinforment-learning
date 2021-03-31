# reinforcement-learning

<a href="dds-pandemic-control.com">
<img  src="/static/assets/img/capture.JPG" alt="My cool logo"/>
</a>

Install
========

Install the virtualenv package

`pip install virtualenv`

Create virtual environment called env, myenv, etc. 

`virtualenv env`

Activate the virtualenvironmnent (LInux)

`source env/bin/activate`

Go the path of the project and install the required libraries 

`pip install -r requirements.txt`

Testing
-----------------
To run the server in the localhost run 

`python manage.py runserver`

Open your browser in the address localhost:8000 


File Description
-----------------
`RL_Corona.ipynb`: is used to generate reinforcement-learning model.

`project_emec2.py`: Takes input from the reinforcement learning model and creates the necessary JSON files for further visualization.

`manage.py`: Contains all the commands required to run the server

`requirements.txt`: Contains all library requirements to run the server

`articles\functions.py`: Contains general functions used by other scripts in the repository.

`articles\templates\welcome.html`: Contains Javascript and HTML scripts required for creating the dashboard

`static\data\RL Model`: Contains scripts for the reinfocement learning model
