import psycopg2

con = psycopg2.connect(dbname='postgres')

con.autocommit = True

cur = con.cursor()
cur.execute('CREATE DATABASE testingtesting;')
cur.execute('CREATE USER mikesucks WITH PASSWORD \'bananafana\';')
