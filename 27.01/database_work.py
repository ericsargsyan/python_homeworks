import logging
import time
import sqlite3
import os

logging.basicConfig(filename='sql_database_logs.log', format='%(asctime)s %(levelname)s: \t%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

database = os.path.join(os.getcwd(), 'sql', 'film.db')

try:
	conn = sqlite3.connect(database)
except sqlite3.Error:
	logging.error('Connection Error')
	
curs = conn.cursor()

curs.execute("SELECT * FROM film \
			  WHERE release_year > 2010 AND rate BETWEEN 3 and 5")
data = curs.fetchall()

project_query = """ CREATE TABLE IF NOT EXISTS filtered_films (
                    					id integer PRIMARY KEY,
                    					title text NOT NULL,
                    					description text,
                    					release_year integer,
                    					rate text,
                    					length integer,
                    					genre text NOT NULL
                    			); """

curs.execute(project_query)
conn.commit()

insert_query = """ INSERT INTO filtered_films(id, title, description, release_year, rate, length, genre)
 				   VALUES(?,?,?,?,?,?,?); """

for i in data:
	with conn:
		curs.execute(insert_query, i)


