const { describe, afterEach, test, expect } = require("@jest/globals");

const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database("blog_app.db");

describe("Database tests", () => {

  afterAll(() => {
    db.close();
  });

  // Test to create a new user
  test("Creating a new user", (done) => {
    db.run("INSERT INTO users (username, email) VALUES (?, ?)", ["unit_tester2", "tester1234@mail.com"], (err) => {
      expect(err).toBeNull();
      db.get("SELECT * FROM users WHERE username=?", ["unit_tester2"], (err, row) => {
        expect(err).toBeNull();
        expect(row).toBeDefined();
        done();
      });
    });
  });

  // Test to update a users email
  test("Update a users email", (done) => {
    db.run("UPDATE users SET email=? WHERE username=?", ["jonny@mail.com", "john@jtc"], (err) => {
      expect(err).toBeNull();
      db.get("SELECT * FROM users WHERE username=?", ["john@jtc"], (err, row) => {
        expect(err).toBeNull();
        expect(row).toBeDefined();
        expect(row.email).toEqual("jonny@mail.com");
        done();
      });
    });
  });

  // Test to create a post
  test("Create a post", (done) => {
    db.run("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", ["4", "Site back up", "Site maintenance complete"], (err) => {
      expect(err).toBeNull();
      db.get("SELECT * FROM posts WHERE title=?", ["Site back up"], (err, row) => {
        expect(err).toBeNull;
        expect(row.content).toEqual("Site maintenance complete");
        done();
      });
    });
  });

  // Test to create a comment
  test("Create a comment", (done) => {
    db.run("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", ["4", "2", "Site back up and running."], (err) => {
      expect(err).toBeNull();
      db.get("SELECT * FROM comments WHERE content=?", ["Site back up and running."], (err) => {
        expect(err).toBeNull;
        done();
      });
    });
  });

  // Test to make sure can NOT create a new user with an existing user name
  test("Can NOT create a user with an existing username", (done) => {
    db.run("INSERT INTO users (username, email) VALUES (?, ?)", ["jason@jtc", "jason123@mail.com"], (err) => {
      expect(err).toBeTruthy;
      console.log("Username already exists, please choose another.");
      done();
    });
  });

  // Test to delete a user
  test("Delete a user", (done) => {
    db.run("DELETE FROM users WHERE username=?", ["delete_me"], (err) => {
      expect(err).toBeNull;
      console.log("User deleted successfully.")
      db.get("SELECT FROM users WHERE username=?", ["delete_me"], (err) => {
        expect(err).toBeTruthy;
        console.log("User no longer exists.");
        done();
      });
    });
  });

});