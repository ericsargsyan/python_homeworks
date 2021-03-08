import sqlite3
from sqlite3 import Error
import os

# Creating a connection to our database
database = os.path.join(os.getcwd(), "film.db")
print(database)
try:
	conn = sqlite3.connect(database)
except Error as e:
	print(e)

# conn = sqlite3.connect(database)
# Creating a cursor to execute commands (queries)

curs = conn.cursor()

# # Create a table with name projects which has rows: id , name , begin_date, end_date
project_query = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

# executing the query
curs.execute(project_query)

# # we should commit the changes
conn.commit()

# Filling the projects table with values
# query:
insert_query = """INSERT INTO projects(id, name, begin_date, end_date)
                    VALUES(222, 'python', '2020-09-01', '2020-12-01');
                """

curs.execute(insert_query)
conn.commit()

Updating the date of created row
update_query = """UPDATE projects
                    SET begin_date = '2020-10-01'
                    WHERE id = 1
                """

curs.execute(update_query)
conn.commit()

# better way not to use conn.commit every time

update_query = """UPDATE projects
                    SET begin_date = '2020'
                    WHERE id = 1
                """
with conn:
    curs.execute(update_query)



# # Grabing data from database
curs.execute("SELECT * FROM {}".format("film"))

# Fetch the values
a = curs.fetchall()
print(a[0])
for i in a[0]:
    print(F"type of {i} is {type(i)}")

# lets create a new film for film table
class Film:
    def __init__(self,film_id,title,description,release_year: str,rate,length: int,special_features):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.rate = rate
        self.length = length
        self.special_features = special_features

    def get_atr_as_tuple(self):
    	return (self.film_id, self.title, self.description, self.release_year, self.rate, self.length, self.special_features)

    def get_atr_as_dict(self):
    	return {'film_id':self.film_id, 'title':self.title, 'description':self.description, 'release_year':self.release_year, 'rate':self.rate, 'length':self.length, 'special_features':self.special_features}
    def __repr__(self):
        return self.title

desc = """In_a post-apocalyptic wasteland, Max, a drifter and survivor, unwillingly joins Imperator Furiosa,
		a rebel warrior, in a quest to overthrow a tyrant who controls the lands water supply."""
film_1 = Film(500,'Mad_Max', "asd",desc, '2015', 120, 'Action')
film_2 = Film(600,'Avangers','marvel movie', '2015',5, 120, 'Action')
film_3 = Film(700,'Avangers 2','marvel movie', '2015',5, 120, 'Action')

def insert_function_film(value):
	insert_query = """INSERT INTO film(film_id, title, description, release_year, rate, length, special_features)
 	                    VALUES(?,?,?,?,?,?,?);
	                    """
	curs.execute(insert_query, value)
	conn.commit()

def insert_function_film_2(value):
	insert_query = """INSERT INTO film(film_id, title, description, release_year, rate, length, special_features)
 	                    VALUES(:film_id,:title,:description,:release_year,:rate,:length,:special_features);
	                    """
	curs.execute(insert_query, value)
	conn.commit()
insert_function_film(film_2.get_atr_as_tuple())
insert_function_film_2(film_3.get_atr_as_dict())
