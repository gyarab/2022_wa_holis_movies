# WA Movies

## Prerequisite

- installed python 3+
- installed pip
- installed all dependencies

## Installation and start

All requirements are described in file `requirements.txt` in root folder of repository.
All dependencies can be installed with command `pip install -r requirements.txt`

After downloading all requirements you can run project with commands:

1. `python3 filmdb/manage.py migrate` - preparing database and all schemas 
2. `python3 filmdb/manage.py loaddata filmdb/fixtures/*` - loading all data into database
3. `python3 filmdb/manage.py runserver` - starting server

After completing commands mentioned above you can see your application running on
[http://localhost:8000/](http://localhost:8000/) (admin can be found at same address with `/admin`) 
