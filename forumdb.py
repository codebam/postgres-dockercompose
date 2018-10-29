""" "Database code" for the DB Forum. """

import datetime
import psycopg2

PARAMS = {
    'database': 'postgres',
    'user': 'root',
    'password': 'toor',
    'host': '127.0.0.1',
    'port': 5432
}


def get_posts():
    """Return all posts from the 'database', most recent first."""
    try:
        database = psycopg2.connect(**PARAMS)
        cur = database.cursor()

        cur.execute("SELECT * FROM posts;")

        data = cur.fetchall()

        cur.close()
        database.close()

        return data

    except psycopg2.OperationalError:
        return [("COULD NOT CONNECT TO DATABASE", datetime.datetime.now(), 0)]


def add_post(text):
    """ Add a post to the 'database' with the current timestamp """
    try:
        database = psycopg2.connect(**PARAMS)  # completed
        cur = database.cursor()

        cur.execute("INSERT INTO posts VALUES ('{text}', '{date}')".format(
            date=datetime.datetime.now(), text=text))

        database.commit()

        cur.close()
        database.close()

        return True
    except psycopg2.OperationalError:
        return False
