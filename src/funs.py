#file contains relevant functions to run the application
import sqlite3
from datetime import datetime,timedelta

def database_setup():
    conn = sqlite3.connect('int.db') #database file where sql database will exist
    cursor = conn.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        application_date DATE NOT NULL,
        follow_up_status TEXT DEFAULT 'pending'         
    )
'''
                   )
    conn.commit
    return conn

def add_application(conn):
    company = input("Enter company name: ")
    position = input("Enter position: ")
    date_str = input("Enter application date (YYYY-MM-DD): ")
    try:
        application_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO applications (company, position, application_date)
        VALUES (?, ?, ?)
    ''', (company, position, application_date))
    conn.commit()
    print('Added Successfully')
def delete_application(conn):
    app_id = input("Enter application ID to delete: ")
    
    cursor = conn.cursor()
    cursor.execute('DELETE FROM applications WHERE id = ?', (app_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Application deleted successfully.")
    else:
        print("No application found with that ID.")

def view_applications(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM applications ORDER BY application_date DESC')
    applications = cursor.fetchall()
    
    if not applications:
        print("No applications found.")
    else:
        print("\nCurrent Applications:")
        for app in applications:
            print(f"ID: {app[0]}, Company: {app[1]}, Position: {app[2]}, "
                  f"Applied: {app[3]}, Follow-up: {app[4]}")
            
    
