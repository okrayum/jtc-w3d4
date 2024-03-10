const userSchema = `
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  email INTEGER UNIQUE
)
`;

const postSchema = `
CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  title TEXT,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
`;

const commentSchema = `
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  post_id INTEGER,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (post_id) REFERENCES posts(id)
)
`;

module.exports = { userSchema, postSchema, commentSchema };