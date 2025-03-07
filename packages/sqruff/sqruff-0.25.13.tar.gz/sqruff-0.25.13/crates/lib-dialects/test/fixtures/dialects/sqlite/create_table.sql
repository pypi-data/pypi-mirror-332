CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL COLLATE NOCASE,
    email TEXT NOT NULL UNIQUE
);
