const sqlite3 = require("sqlite3").verbose();
const { userSchema, postSchema, commentSchema } = require("./schema")

const db = new sqlite3.Database("blog_app1.db");

db.run("PRAGMA foreign_keys = ON;");

db.run(userSchema);
db.run(postSchema);
db.run(commentSchema);

module.exports = db;