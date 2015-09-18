__author__ = 'Sotaya'

"""

This is the SQLite database helper script, it provides functions to create, drop table
Update comment in the table, fetch the last id in the table, fetch data of a particular
id, fetch all the rows in the table and update comment of a specific id.

"""

import sqlite3
import os

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')


class Database:
    def __init__(self):
        pass

    #creates the database instance
    def create_db(self, path=DATA_PATH + 'model'):
        try:
            db = sqlite3.connect(path)

            cursor = db.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS model(id INTEGER PRIMARY KEY,
                question TEXT, answer TEXT, category TEXT, rating INTEGER)''')
            db.commit()

        except Exception as a:
            db.rollback()
            print('some errors occurred')
            raise a
        finally:
            db.close()

    #inserts all the data into the db, answer, rating are optional, can be updated later
    def insert(self, question, category, answer="", rating=0, path=DATA_PATH + 'model'):
        try:
            db = sqlite3.connect(path)
            cursor = db.cursor()
            cursor.execute('''INSERT INTO model(question, category, answer, rating)
                                VALUES(?,?,?,?)''', (question, category, answer, rating))
            db.commit()
            print('inserted question and info')
        except Exception as b:
            db.rollback()
            print('some error occurred')
            raise b
        finally:
            db.close()

    #reads all question, answer, category and rating in the db
    def read_all(self, path=DATA_PATH + 'model'):
        try:
            db = sqlite3.connect(path)
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM model''')
            all_rows = cursor.fetchall()
        except Exception as c:
            raise c
        finally:
            db.close()
        return all_rows

    def drop_table(self, path=DATA_PATH + 'model'):
        try:
            db = sqlite3.connect(path)
            cursor = db.cursor()
            cursor.execute('''DROP TABLE model''')
            db.commit()
        except Exception as d:
            raise d
        finally:
            db.close()

    def update_answer(self, id, answer, path=DATA_PATH + 'model'):
        try:
            db = sqlite3.connect(path)
            cursor = db.cursor()
            cursor.execute('''UPDATE model SET answer=:answer WHERE id=:id''', {"answer": answer, "id": id})
            db.commit()
        except Exception as e:
            raise e
        finally:
            db.close()

    def update_rating(self, id, rating, path=DATA_PATH + 'model'):
        try:
            db = sqlite3.connect(path)
            cursor = db.cursor()
            cursor.execute('''UPDATE model SET rating=:rating WHERE id=:id''', {"rating": rating, "id": id})
            db.commit()
        except Exception as f:
            raise f
        finally:
            db.close()
