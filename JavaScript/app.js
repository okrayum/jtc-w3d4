const db = require("./db")

// Create a user here
db.run("INSERT INTO users (username, email) VALUES (?, ?)", ["new_user@jtc", "new_user@mail.com"], (err) => {
  if (err) {
    console.log("Error creating user:", err);
    return;
  }
  console.log("User created successfully");

  db.all("SELECT * FROM users", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All users:", rows);
  });
});

// Update user email here
db.run("UPDATE users SET email=? WHERE username=?", ["Tester@mail.com", "Tester"], (err) => {
  if (err) {
    console.log("Error updating email:", err);
    return;
  }
  console.log("Email changed!");

  db.all("SELECT * FROM users", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All users:", rows);
  });
})

// Create a post here
db.run("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", ["3", "Hello", "New here!"], function (err) {
  if (err) {
    console.log("Error creating post:", err);
    return;
  }
  console.log("Post created!");

  db.all("SELECT * FROM posts", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All posts:", rows);
  });
});

// Create a comment here
db.run("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", ["3", "1", "Is the site back up?"], function (err) {
  if (err) {
    console.log("Error creating comment:", err);
    return;
  }
  console.log("Comment created!");

  db.all("SELECT * FROM comments", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All comments:", rows);
  });
});

// Delete a user here
db.run("DELETE FROM users WHERE username=?", ["Tester"], (err) => {
  if (err) {
    console.log("Error deleting user:", err);
    return;
  }
  console.log("User deleted!");

  db.all("SELECT * FROM users", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All users:", rows);
  });
});

db.close();