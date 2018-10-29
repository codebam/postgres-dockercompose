This is a docker-compose container that can be used to rollout a database that
can be connected to from your your local machine.

To run `docker-compose up`

To run commands on the database edit `forumdb.py` or `forum.py`, install the
appropriate libraries, and then run `python forum.py`.

- you need to install psycopg2 for python to use the python file

To connect to the database using adminer open
[localhost:8080](http://localhost:8080) and login using:

System | PostgreSQL
--- | ---
Server | postgres
Username | root
Password | toor
Database | postgres

or just click [here](http://localhost:8080/?pgsql=postgres&username=root&db=postgres&ns=public) to login directly
