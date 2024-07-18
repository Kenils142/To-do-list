import os
import sqlite3
from datetime import date
from create_db import create

def add_task(name: str, description: str, date: date):
    
    database_path = "../database/todolist.db"

    # Check if database already exist.
    if not os.path.exists(database_path):
        create()
    
    # SQL query for inserting values for task
    query = "INSERT INTO tasks(name, description, date) VALUES(?,?,?)"

    # Doing database stuff for inserting task
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, ((name, description, date)))
        conn.commit()
