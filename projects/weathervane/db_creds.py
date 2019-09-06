import psycopg2
import os

db_username = str(os.environ.get('DB_USERNAME'))
db_password = str(os.environ.get('DB_PASSWORD'))
db_name = str(os.environ.get('DB_NAME'))

con = psycopg2.connect(dbname='postgres')

con.autocommit = True

cur = con.cursor()
cur.execute('CREATE DATABASE ' + db_name + ';')
cur.execute('CREATE USER ' + db_username +
            ' WITH PASSWORD \'' + db_password + '\';')

print('Postgres DB Credentials set up!')
