from db.connection import db_connection, db_cursor
from db.schema import magazines

class Magazine:
    def __init__(self, name, category):
        self.id = None
        self.name = name
        self.category = category

    def __repr__(self):
        return f"<Magazine(name={self.name}, category={self.category})>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

    @classmethod
    def create_table(cls):
        db_cursor.execute(magazines)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        db_cursor.execute("DROP TABLE IF EXISTS magazines")
        db_connection.commit()

    def save(self):
        db_cursor.execute(
            "INSERT INTO magazines (name, category) VALUES (?, ?)",
            (self.name, self.category)
        )
        db_connection.commit()
        self.id = db_cursor.lastrowid

    @classmethod
    def create(cls, name, category):
        magazine = cls(name, category)
        magazine.save()
        return magazine

    def update(self):
        db_cursor.execute(
            "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
            (self.name, self.category, self.id)
        )
        db_connection.commit()

    def delete(self):
        db_cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
        db_connection.commit()
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        magazine = cls(row[1], row[2])
        magazine.id = row[0]
        return magazine

    @classmethod
    def find_by_id(cls, magazine_id):
        db_cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        row = db_cursor.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    @classmethod
    def find_by_name(cls, name):
        db_cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = db_cursor.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    @classmethod
    def find_by_category(cls, category):
        db_cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        rows = db_cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []