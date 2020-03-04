# Code-Battle
An online judge that supports the following languages:
* C
* C++
* Python 2
* Python 3
### Tools Used
* **Python - Django**
* **Javascript**
* **Bootstrap**
### Third Party Services Used
* **sendgrid**: Used to send transactional emails like email-id verification.
**Instructions for setting up the project**
* Clone the repository
git clone 

* Rename the file .env-sample to .env and replace the value of SECRET_KEY with the secret key of your own project. To generate a new secret key

* Go to terminal and create a new django project django-admin startproject <proj-name>.
* Now get the value of SECRET_KEY in settings.py and use that as the secret key for the Stock-Bridge project.
* Now delete that new django project.
* Sendgrid setup:

 * Create an account on sendgrid.
* Add your sendgrid username and password to EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in credentials.py respectively.
* Change the email and name in DEFAULT_FROM_EMAIL and MANAGERS in all settings files with your name and email.
* Run the following commands
* python manage.py makemigrations
* python manage.py migrate
* python manage.py collectstatic

* Now load the questions, test cases, expected outputs and user submission into the database
* python manage.py loaddata questions/fixtures/questions.json
