import sqlite3

# This file is responsible for creating database for storing tasks for To do list


def create():    
    database_path = "../databse/todolist.db"

    # creates connection and file to ToDoList/database/ with name todolist.db
    conn = sqlite3.connect(database_path)

    # Creating cursor and creating new table named Tasks in Database. 
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE Tasks(
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            date DATE
        )''')
    
    # Commiting changes and closing connection
    cursor.close()
    conn.commit()
    conn.close()
