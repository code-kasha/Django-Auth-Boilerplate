# awesome-django-auth
A complete Implementation of Authentication system in Django

Also, please check the notes.txt if you need more to read.
I have tried my best to keep the code as clean and minimal as possible,
If you like it and find it useful, consider leaving a star on the repo!

## I have used Class Based Views. Please watch my livestream on youtube if you want more to look at, or how I implement it.

# Installation.

Kindly note, 
.db_user - postgresql db username.
.db_pass - postgresql db password.

.django_secret_key - django secret key.

.email_provider_pass - Your email account's password.

these four files are required to run the project with the default configuration.

I like to store them in a folder named .secrets and exclude from my version control.
I advise you to do the same because then it simplifies the task of switching to enviornment variables in production.

If you don't plan on using postgresql, you don't need the first two. but check it out, it's awesome :D

Then as far as any project goes, do a git clone, followed by cd __folder_name and run pip install -r requirements.txt

Be free to modify the requirements file if you don't like black or flake8, but they are awesome.

Make sure you have created above mentioned files, and your postgres is running, do a python manage.py migrate.

Create a superuser and start your project happily with authentication implemented!

Also note, I'm using bootstrap 4.5 for this project as crispy_forms work the best with that and I don't wanna spend 
extra time making the forms look nice. so, I'm sorry.


# some conventions I like to use

1] using an apps folder to store all my apps.

2] keeping source files as short as possible but my module library richer 

