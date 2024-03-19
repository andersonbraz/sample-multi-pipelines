import sqlite3

# Connect to the database
conn = sqlite3.connect('data/sqlite/shop_cars.db')

# Create a cursor object
cursor = conn.cursor()

# Create the tables
cursor.execute('''CREATE TABLE authors
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

cursor.execute('''CREATE TABLE posts
                  (id INTEGER PRIMARY KEY, title TEXT, content TEXT, author_id INTEGER,
                  FOREIGN KEY(author_id) REFERENCES authors(id))''')

cursor.execute('''CREATE TABLE comments
                  (id INTEGER PRIMARY KEY, content TEXT, post_id INTEGER, author_id INTEGER,
                  FOREIGN KEY(post_id) REFERENCES posts(id),
                  FOREIGN KEY(author_id) REFERENCES authors(id))''')

# Close the connection
conn.close()