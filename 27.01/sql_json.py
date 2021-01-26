import sqlite3
import json
import time
import os

logging.basicConfig(filename='database_logs.log', format='%(asctime)s %(levelname)s: \t%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

database = os.path.join(os.getcwd(), 'sql', 'film.db')

try:
	conn = sqlite3.connect(database)
except sqlite3.Error:
	logging.error('Connection Error')
	print("conecction error")

curs = conn.cursor()

curs.execute("SELECT * FROM film")

with open("sql_json.json", 'a') as json_file:
	json.dump(curs.fetchall(), json_file, indent=4)


