from db.connection import db_connection, db_cursor
from db.schema import authors
class Author:
    all_authors = []

    def __init__(self, name):
        self.id = None
        self.name = name

    def __repr__(self):
        return f"<Author(name={self.name})>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @classmethod
    def create_table(cls):
        db_cursor.execute(authors)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        db_cursor.execute("DROP TABLE IF EXISTS authors")
        db_connection.commit()
    def save(self):
        db_cursor.execute(
            "INSERT INTO authors (name) VALUES (?)",
            (self.name,)
        )
        db_connection.commit()
        Author.all_authors.append(self)

    @classmethod
    def create(cls, name):
        author = cls(name)
        author.save()
        return author
    
    def update(self, name):
        self.name = name
        db_cursor.execute(
            "UPDATE authors SET name = ? WHERE id = ?",
            (self.name, self.id)
        )
        db_connection.commit()

    def delete(self):
        db_cursor.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        db_connection.commit()
        del type(self).all_authors[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        author = cls.all_authors.get(row[0])
        if author:
            author.author_id = row[1]
            author.magazine_id = row[2]
            author.title = row[3]
            author.content = row[4]
        else:
            author = cls(row[1], row[2], row[3], row[4])
            author.id = row[0]
            cls.all_authors[author.id] = author
        return author   
        
    @classmethod
    def get_all(cls):
        db_cursor.execute("SELECT * FROM authors")
        rows = db_cursor.fetchall()
        cls.all_authors = [cls.instance_from_db(row) for row in rows]
        return cls.all_authors
    @classmethod
    def find_by_id(cls, author_id):
        db_cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = db_cursor.fetchone()
        if row:
            return cls(row[1])  # Assuming the second column is 'name'
        return None
    
    @classmethod
    def find_by_name(cls, name):
        db_cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = db_cursor.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    