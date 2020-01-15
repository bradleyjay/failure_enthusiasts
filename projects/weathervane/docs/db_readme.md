Dependencies (make sure pip is installed if these commands don’t work)

```
brew install postgresql
pip3 install psycopg2
pip3 install sqlalchemy
```

2. Start the Postgres server! (ideally in another Terminal window)
```postgres -D /usr/local/var/postgres/```

3. Log in to the Postgres server
```psql postgres```

4. Create the database and then use a command to see the list of your databases
```CREATE DATABASE weather_app_db;
\list```

5. Create a user to access your database, then use a command to see your list of users
```CREATE ROLE weather_app_user WITH LOGIN PASSWORD '1234';
\du```

6. Grant access to your user so that it can access the database
```ALTER ROLE weather_app_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE weather_app_db TO weather_app_user;```

7. Quit out of the Postgres server
```\q```

8. Pray.

9.  run ps
find the  process number  PID
kill  -9  PID

##############
If you encounter an error for a column that should exist but doesn't, follow the steps below

1. Try: Start the Postgres server! (ideally in another Terminal window)
```postgres -D /usr/local/var/postgres/```

2. If already running: Log in to the Postgres server
```psql postgres```

3. Use below command to see list of databases, then look for weather_app_db
```\list```

4. Switch into the database
```\c weather_app_db```

5. Use the following to see list of tables in database
```\dt```

6. If actual and predictive tables already exist in db, drop both using the following
```DROP TABLE actual_weather;
DROP TABLE predictive_weather;```





#. Pray again.