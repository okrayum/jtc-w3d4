user_schema = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                email INTEGER UNIQUE
)
'''

post_schema = '''CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                title TEXT,
                content TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
)
'''

comment_schema = '''CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                post_id INTEGER,
                content TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (post_id) REFERENCES posts(id)
)
'''