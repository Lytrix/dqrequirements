# Django DQ Requirements #

Demo website for creating requirements.

### Install procedure ###
download and install <a href="https://www.docker.com">docker</a></br>

```
git clone https://github.com/lytrix/dqrequirements.git ibprojecten
cd ibprojecten
docker-compose build database
docker-compose up database
```

Create a local environment and activate it:
```
virtualenv --python=$(which python3) venv
source venv/bin/activate
```

Install the packages 
```
pip install -r ./web/requirements.txt
```

Before you can login to the site, you must create the tables and an admin useraccount in the database:
```
./web/manage.py migrate
./web/manage.py createsuperuser
```

You can run the website locally with using only the database in a docker by using:
```
docker-compose up database
./web/manage.py runserver
```

The site can be found on http://localhost:8000</br>
The docker postgres database can be found on localhost:5401

To start the website in a docker you can use this command:
```
docker-compose build web
docker-compose up web
```

The site can be found on http://localhost:8113</br>
