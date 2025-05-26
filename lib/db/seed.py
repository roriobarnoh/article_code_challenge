from connection import db_cursor, db_connection
from schema import articles, authors, magazines
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def seed_data():
    # Drop existing tables (optional for dev)
    db_cursor.execute("DROP TABLE IF EXISTS authors")
    db_cursor.execute("DROP TABLE IF EXISTS magazines")
    db_cursor.execute("DROP TABLE IF EXISTS articles")

    # Create tables
    db_cursor.execute(authors)
    db_cursor.execute(magazines)
    db_cursor.execute(articles)

    # Create and insert data
    # author1 = Author("Nancy")
    # author1.save()

    # author2 = Author("Brian")
    # author2.save()
    # author3 = Author("Alice")
    # author3.save()
    # author4 = Author("David")
    # author4.save()

    # magazine1 = Magazine("Tech Today", "Technology")
    # magazine1.save()

    # magazine2 = Magazine("Health Monthly", "Health")
    # magazine2.save()
    # magazine3 = Magazine("Travel Weekly", "Travel")
    # magazine3.save()
    # magazine4 = Magazine("Foodie", "Food")
    # magazine4.save()

    # article1 = Article("The Future of AI", "AI is evolving fast.", author1, magazine1)
    # article1.save()

    # article2 = Article("Healthy Eating", "Start your day with fruit.", author2, magazine2)
    # article2.save()
    # article3 = Article("Exploring Europe", "Top 10 places to visit in Europe.", author3, magazine3)
    # article3.save()
    # article4 = Article("Cooking Basics", "Learn to cook with these simple recipes.", author4, magazine4)
    # article4.save()

    # db_connection.commit()
    # db_connection.close()