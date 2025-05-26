authors = """
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL
        );
"""
magazines = """
    CREATE TABLE IF BOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        category VARCHAR
        );
"""
articles = """
CREATE TABLE IF NOT EXISTS articles(
    id INTEGER PRIMARY KEY,
    author_id INTEGER NOT NULL,
    magazine_id INTEGER NOT NULL,
    title VARCHAR NOT NULL,
    content VARCHAR NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (magazine_id) REFERENCES mgazines(id)
    );
"""