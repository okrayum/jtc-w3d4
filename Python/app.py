import sqlite3
from schema import user_schema, post_schema, comment_schema

con = sqlite3.connect("blog_app2.db")

con.execute("PRAGMA foreign_keys = ON;")

cur = con.cursor()

cur.execute(user_schema)
cur.execute(post_schema)
cur.execute(comment_schema)

# Create a user here
try:
  username = "test_delete"
  email = "delete@mail.com"

  cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
  print("User created!")
except sqlite3.IntegrityError as e:
  print("User not created successfully:", e)

# Update a users email here
try:
  email = "jason123@mail.com"
  username = "jason@jtc"

  cur.execute("UPDATE users SET email=? WHERE username=?", (email, username))
  if cur.rowcount == 0:
    print("No changes were made.")
  else:
    print("Email updated!")  
except sqlite3.Error as e:
  print("Error occurred.", e)  

# Update a users username here
try:
  new_username = "jason123"
  old_username = "jason@jtc"

  cur.execute("UPDATE users SET username=? WHERE username=?", (new_username, old_username))
  if cur.rowcount == 0:
    print("No changes were made.")
  else:
    print("Username updated!")
except sqlite3.Error as e:
  print("Error occurred:", e)    

# Create a post here
try:
  user_id = "2"
  title = "This is a deletion test"
  content = "Testing Testing"

  cur.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
  if cur.rowcount == 0:
    print("Post not created.")
  else:
    print("Post created!")  
except sqlite3.Error as e:
  print("Error occurred:", e)

# Create a comment here
try:
  user_id = "2"
  post_id = "1"
  content = "Testing Again!!!"

  cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (user_id, post_id, content))
  if cur.rowcount == 0:
    print("Comment not created.")
  else:
    print("Comment created!")
except sqlite3.Error as e:
  print("Error occurred:", e)      

# Delete a user here
try:
  username = "sammy"

  cur.execute("DELETE FROM users WHERE username=?", (username,))
  if cur.rowcount == 0:
    print("User not deleted.")
  else:
    print("User deleted!")
except sqlite3.Error as e:
  print("Error occurred:", e)

# Displays all users in the terminal
cur.execute("SELECT * FROM users")
print(cur.fetchall())

# Displays all posts in the terminal
cur.execute("SELECT * FROM posts")
print(cur.fetchall())

# Displays all comments in the terminal
cur.execute("SELECT * FROM comments")
print(cur.fetchall())

con.commit()
con.close()
