import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to get a connection to the database
def get_db_connection():
    conn = sqlite3.connect('socialmedia.db')
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn

# Function to create the posts table if it doesn't exist
def create_table():
    conn = get_db_connection()
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

# Initialize the database when the app starts
create_table()

# Route to display the social media feed
@app.route('/')
def index():
    conn = get_db_connection()
    # Fetch posts, ordered by score calculated as (Likes * 2) + (Comments * 3) + (Interactions * 4)
    posts = conn.execute('''
        SELECT * FROM posts
        ORDER BY (likes * 2 + comments * 3 + interactions * 4) DESC
    ''').fetchall()  # Fetch posts in descending order of score
    conn.close()
    return render_template('index.html', posts=posts)

# Route to handle new post submission
@app.route('/add_post', methods=['POST'])
def add_post():
    content = request.form['content']
    likes = int(request.form['likes'])
    comments = int(request.form['comments'])
    interactions = int(request.form['interactions'])

    # Insert the new post into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO posts (content, likes, comments, interactions)
        VALUES (?, ?, ?, ?)
    ''', (content, likes, comments, interactions))
    conn.commit()
    conn.close()

    return index()  # Return to the main feed page after submitting

if __name__ == "__main__":
    app.run(debug=True)
