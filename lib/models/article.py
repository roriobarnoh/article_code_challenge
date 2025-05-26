from db.connection import db_connection, db_cursor
from db.schema import articles


class Article:
    all_articles = []
    def __init__(self, author_id, magazine_id, title, content):
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.title = title
        self.content = content
    
    def __repr__(self):
        return f"<Article(title={self.title}, author_id={self.author_id}, magazine_id={self.magazine_id})>"
    
    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        from .author import Author
        if Author.find_by_id(author_id):
            self._author_id = author_id
        else:
            raise ValueError(f"Author with id {author_id} does not exist.")
    @property
    def magazine_id(self):
        return self._magazine_id
    
    @magazine_id.setter
    def magazine_id(self, magazine_id):
        from .magazine import Magazine
        if Magazine.find_by_id(magazine_id):
            self._magazine_id = magazine_id
        else:
            raise ValueError(f"Magazine with id {magazine_id} does not exist.")

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string.")
    @property
    def content(self):
        return self._content
    @content.setter
    def content(self, content):
        if isinstance(content, str) and len(content) > 0:
            self._content = content
        else:
            raise ValueError("Content must be a non-empty string.")
    def save(self):
        db_cursor.execute(
            "INSERT INTO articles (author_id, magazine_id, title, content) VALUES (?, ?, ?, ?)",
            (self.author_id, self.magazine_id, self.title, self.content)
        )
        db_connection.commit()
        self.id = db_cursor.lastrowid
        type(self).all_articles[self.id] = self

    @classmethod
    def create_table(cls):
        db_cursor.execute(articles)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        db_cursor.execute("DROP TABLE IF EXISTS articles")
        db_connection.commit()

    @classmethod
    def create(cls, author_id, magazine_id, title, content):
        article = cls(author_id, magazine_id, title, content)
        article.save()
        return article
    

    def update(self):
        db_cursor.execute(
            "UPDATE articles SET author_id = ?, magazine_id = ?, title = ?, content = ? WHERE id = ?",
            (self.author_id, self.magazine_id, self.title, self.content, self.id)
        )
        db_connection.commit()

    def delete(self):
        db_cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
        db_connection.commit()
        del type(self).all_articles[self.id]
    @classmethod
    def instance_from_db(cls, row):
        article = cls.all_articles.get(row[0])
        if article:
            article.author_id = row[1]
            article.magazine_id = row[2]
            article.title = row[3]
            article.content = row[4]
        else:
            article = cls(row[1], row[2], row[3], row[4])
            article.id = row[0]
            cls.all_articles[article.id] = article
        return article
    @classmethod
    def find_by_id(cls, article_id):
        db_cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        row = db_cursor.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    @classmethod
    def find_by_title(cls, title):
        db_cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = db_cursor.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    
    @classmethod
    def find_by_author_id(cls, author_id):
        db_cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        rows = db_cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []
    
    @classmethod
    def find_by_magazine_id(cls, magazine_id):
        db_cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
        rows = db_cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []
    
    