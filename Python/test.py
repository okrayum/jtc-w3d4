import unittest
import sqlite3

con = sqlite3.connect("blog_app2.db")
con.execute("PRAGMA foreign_keys = ON;")
cur = con.cursor()

class TestDataBase(unittest.TestCase):

  def setUp(self):
      self.con = sqlite3.connect("blog_app2.db")
      self.cur = self.con.cursor()

  def tearDown(self):
      self.con.close()    

  # Test to create a new user  
  def test_create_user(self):
      self.cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("test_user", "test_user@mail.com"))
      self.con.commit()
      self.cur.execute("SELECT * FROM users WHERE username=?", ("test_user",))
      user = self.cur.fetchone()
      self.assertIsNotNone(user, "User creation failed") 
      print("User created successfully")

  # Test to udate an existing users email  
  def test_update_user(self):
      self.cur.execute("UPDATE users SET email=? WHERE username=?", ("test@mail.com", "test_user"))
      self.con.commit()
      self.cur.execute("SELECT * FROM users WHERE username=?", ("test_user",))
      user = self.cur.fetchone()
      self.assertEqual(user[2], "test@mail.com") 
      print("User updated successfully")

  # Test to add a post
  def test_create_post(self):
      self.cur.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", ("2", "Hello!", "New user here."))
      self.con.commit()
      self.cur.execute("SELECT * FROM posts WHERE title=?", ("Hello!",))
      post = self.cur.fetchone()
      self.assertIsNotNone(post, "Post creation failed") 
      print("Post created successfully")

  # Test to add a comment
  def test_create_comment(self):
      self.cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", ("2", "1", "How is testing going?"))
      self.con.commit()
      self.cur.execute("SELECT * FROM comments WHERE content=?", ("How is testing going?",))
      comment = self.cur.fetchone()
      self.assertIsNotNone(comment, "Comment creation failed") 
      print("Comment created successfully")

  # Test to make sure can NOT create a new user with an existing user name
  def test_creating_user_with_existing_username(self):
      with self.assertRaises(sqlite3.IntegrityError):
          self.cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("jason123", "jason@mail.com"))
          self.con.commit()
      print("Username already exists")    

  # Test to delete a user
  def test_delete_user(self):
      self.cur.execute("DELETE FROM users WHERE username=?", ("test_delete",))
      self.con.commit()
      self.cur.execute("SELECT * FROM users WHERE username=?", ("test_delete",))
      user = self.cur.fetchone()
      self.assertIsNone(user, "User deletion failed")
      print("User deleted successfully")

if __name__ == '__main__':
    unittest.main()