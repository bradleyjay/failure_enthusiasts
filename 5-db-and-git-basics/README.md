# Database and Git Basics

## Session Notes
Week 5 - *we covered...[TBD]...*
- *See [session_notes.md](https://github.com/bradleyjay/failure_enthusiasts/blob/master/1-basics_and_guessing_game/session_notes.md) for details*

## Database Basics - Postgres setup

1. Install Postgres and dependencies for Python
```brew update
brew install postgresql
pip3 install psycopg2
pip3 install sqlalchemy```

2. Start the Postgres server! (ideally in another Terminal window)
```postgres -D /usr/local/var/postgres/```

3. Log in to the Postgres server
```psql postgres```

4. Create the database and then use a command to see the list of your databases
```CREATE DATABASE <<dbname>>;
\list```

5. Create a user to access your database, then use a command to see your list of users
```CREATE ROLE <<username>> WITH LOGIN PASSWORD <<'password'>>;
\du```
  
6. Grant access to your user so that it can access the database
```ALTER ROLE <<username>> CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE <<dbname>> TO <<username>>;```
  
7. Quit out of the Postgres server
```\q```



### Github Basics

We'll start with this:
https://rogerdudler.github.io/git-guide/

For today, we'll practice some basic git:
1. Clone a repo locally via `git clone <repo name>`
2. Create a branch with `git checkout -b <feature_name>`

3. Make our changes, working locally

4. Stage those changes by adding them to Index with `git add <filename>`, then commiting with `git commit -m '<some_descriptive_message_here'`

5. Push those changes to the remote repository on github via `git push origin <branch_name>`

