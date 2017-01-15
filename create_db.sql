-- create_db.sql
CREATE TABLE items (
	id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
	name TEXT NOT NULL,
	group_name TEXT
);

CREATE TABLE draw_histories (
    draw_histories_id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
	itemid INTEGER,
	time DATETIME DEFAULT (datetime('now', 'localtime')),
	FOREIGN KEY (itemid) REFERENCES items(id)
);