const db = require("./db")

db.run("INSERT INTO users (username, email) VALUES (?, ?)", ["Admin", "Admin@mail.com"], function (err) {
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

db.run("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", ["4", "Site Maintenance", "Site will be down this Saturday."], function (err) {
  if (err) {
    console.log("Error creating post:", err);
    return;
  }
  console.log("Post created successfully");

  db.all("SELECT * FROM posts", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All posts:", rows);
  });
});

db.run("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", ["3", "1", "Is class earlier or later now?"], function (err) {
  if (err) {
    console.log("Error creating comment:", err);
    return;
  }
  console.log("Comment created successfully");

  db.all("SELECT * FROM comments", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving data:", err);
      return;
    }
    console.log("All comments:", rows);
  });
});

db.close();