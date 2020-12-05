CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	first_name TEXT,
	last_name TEXT,
	email TEXT,
	phone TEXT,
	admin INTEGER DEFAULT 0
);

CREATE TABLE lessons (
	id SERIAL PRIMARY KEY,
	name TEXT,
	spots INTEGER,
	date DATE,
	start TIME,
	duration INTEGER
);

CREATE TABLE sign_ups (
	id SERIAL PRIMARY KEY,
	lesson_id INTEGER REFERENCES lessons(id),
	user_id INTEGER REFERENCES users(id),
	reserve INTEGER DEFAULT 0
);

CREATE TABLE feedback (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users(id) DEFAULT 0,
	message TEXT
);