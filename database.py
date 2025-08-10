import sqlite3

DB_NAME = "gan_images.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS images
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filename TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_image(filename):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO images (filename) VALUES (?)", (filename,))
    conn.commit()
    conn.close()

def get_all_images():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM images")
    rows = c.fetchall()
    conn.close()
    return rows

def update_image(id, filename):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE images SET filename=? WHERE id=?", (filename, id))
    conn.commit()
    conn.close()

def delete_image(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM images WHERE id=?", (id,))
    conn.commit()
    conn.close()
