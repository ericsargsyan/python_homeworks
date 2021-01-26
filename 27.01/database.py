import sqlite3
import logging
import time
import os

logging.basicConfig(filename='database_logs.log', format='%(asctime)s %(levelname)s: \t%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

database = os.path.join(os.getcwd(), 'sql', 'film.db')

try: 
	conn = sqlite3.connect(database)
except sqlite3.Error:
	logging.error("Connection ERROR")

curs = conn.cursor()

curs.execute("SELECT title FROM {} \
			  WHERE title like 'B%'".format("film"))

films_name = curs.fetchall()
print(films_name)

curs.execute("SELECT title, release_year, rate, max(length), special_features \
			  FROM film")

longest_film = curs.fetchall()
print(longest_film)

