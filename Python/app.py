import sqlite3

con = sqlite3.connect("blog_app2.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                email INTEGER UNIQUE
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                title TEXT,
                content TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                post_id INTEGER,
                content TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (post_id) REFERENCES posts(id) 
            )''')

cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("jason@jtc", "jason@mail.com"))

cur.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", ("2", "Spring Break!", "No class next week for Spring break!"))

cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", ("1", "3", "Yeah Spring Break!"))


cur.execute("SELECT * FROM users")
print(cur.fetchall())

cur.execute("SELECT * FROM posts")
print(cur.fetchall())

cur.execute("SELECT * FROM comments")
print(cur.fetchall())

con.commit()

con.close()
