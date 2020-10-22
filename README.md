# Online Exam Taking Application
An exam application created in django to conduct mcq quizzes. The application has the following features : 
1) Add/update/delete questions from admin.
2) Add dynamic category to each question.

# Installation
1) Install python3
2) Install pip for python3
3) Install virtualenv
  `pip install virtualenv` or `pip3 install virtualenv`
4) Create virtual environment and cd into it
  `virtualenv OnlineExamWebApp --python python3 && cd OnlineExamWebApp`
5) Clone git repository into src folder and cd into it `git clone <url> src && cd src`
6) Install requirements `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
7) Make appropriate changes to settings module and make migrations using `python manage.py makemigrations` and then 
  `python manage.py migrate`
8) Run using `python manage.py runserver`
9) Create superuser to log into admin `python manage.py createsuperuser`

# Implementation
1) Add questions from admin
2) Conduct the quiz
