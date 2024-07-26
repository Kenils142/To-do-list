import os
import sqlite3
from datetime import date

db_path = "./database/todolist.db"

# For creating database.
# Do not call this function anywhere else
# other functions in this module will handle creation of database if it doesn't already exist.
def create():
    query = '''
            CREATE TABLE Tasks(
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                date TEXT
            )'''
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


# Function for adding new tasks.
def add_task(name: str, description: str, date: date):

    # Check if database exist.
    if not os.path.exists(db_path):
        create()

    query = "INSERT INTO tasks(name, description, date) VALUES(?,?,?)"
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, ((name, description, date)))

        # Checking and commiting if query executed successfully
        if cursor.rowcount >= 1:
            conn.commit()
            print("Added Task")
            return True
        
    return False
    

# Function for getting all the tasks from database
def get_tasks():
    
    # Check if database exist.
    if not os.path.exists(db_path):
        create()

    query = "SELECT * FROM Tasks"
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query) 
        tasks = cursor.fetchall()
    
    return tasks


# Function for editing tasks
def edit_task(id, name, description, date):

    query = '''
            UPDATE Tasks
            SET name = ?, description = ?, date = ?
            WHERE id = ?
        '''
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (name, description, date, id))

        # Checking and commiting if query executed successfully
        if cursor.rowcount == 1:
            conn.commit()
            return True
        
    return False
        

# Function for deleting tasks
def del_task(id):
    query = '''
            DELETE FROM Tasks
            WHERE id = ?'''
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        
        if cursor.rowcount > 0:
            conn.commit()