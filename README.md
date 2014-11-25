ldapChat
========

#Installation
To run this app locally, you need to have Python 2.7 installed. If you don't, do a 

    sudo apt-get install python2.7

Then, you need to install all the reuirements. We'd suggest you to work on a virtual environment, but anyway the process is the same:

    pip intall -r requirements.txt

Now before you run it, setup the database.

And then, to run it, finally go to the directory with `manage.py` and enter:

    ./manage.py runserver

On your terminal. Your app would now be running at `localhost:8000`

#Setting up the database
We're using postgresql, so first, install that. Next create a user ldapchat with password ldapchat and then create a database called ldapchat. You're good to go.
