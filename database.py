import sqlite3

# Function to create the posts table if it doesn't exist
def create_table():
    conn = sqlite3.connect('socialmedia.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        likes INTEGER,
        comments INTEGER,
        interactions INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# Function to get a connection to the database
def get_db_connection():
    conn = sqlite3.connect('socialmedia.db')
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn
