import sqlite3
from schema import user_schema, post_schema, comment_schema

con = sqlite3.connect("blog_app2.db")

cur = con.cursor()

cur.execute(user_schema)
cur.execute(post_schema)
cur.execute(comment_schema)

cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("jason123@jtc", "jason123@mail.com"))

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
