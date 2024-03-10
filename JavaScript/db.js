const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("blog_app1.db");

db.run(`CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  email INTEGER UNIQUE
)`);

db.run(`CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  title TEXT,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)`);

db.run(`CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  post_id INTEGER,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (post_id) REFERENCES posts(id)
)`);

module.exports = db;