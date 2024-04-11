from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

# ? Note that engine doesnt create db automatically with mysql so i have to create it with this steps
import mysql.connector

# Connect to MySQL server (replace 'username' and 'password' with your MySQL username and password)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a new database (replace 'db_name' with your desired database name)
cursor.execute("CREATE DATABASE IF NOT EXISTS mysqlorm")

class Author(Base):
    __tablename__ = 'authors'

    id = Column("id",Integer, primary_key=True)
    name = Column("name",String(255))
    nationality = Column("nationality",String(255))

    def __init__(self, id, name, nationality):
        self.id = id
        self.name = name
        self.nationality = nationality

    def __repr__(self):
        return f"Author({self.id}, {self.name}, {self.nationality})"

class Book(Base):
    __tablename__ = 'books'

    id = Column("id",Integer, primary_key=True)
    title = Column("title",String(255))
    publication_date = Column("publication_date",DateTime)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

    def __init__(self, id, title, publication_date, author_id):
        self.id = id
        self.title = title
        self.publication_date = publication_date
        self.author_id = author_id

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.publication_date}, {self.author_id})"

Author.books = relationship("Book", back_populates="author")

engine = create_engine('mysql+mysqlconnector://root:@localhost/mysqlorm', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(id=1, name="Mark Twain", nationality="American")
author2 = Author(id=2, name="Leo Tolstoy", nationality="Russian")
session.add(author1)
session.add(author2)
session.commit()

book1 = Book(id=1, title="The Adventures of Tom Sawyer", publication_date=datetime(1876, 1, 1), author_id=author1.id)
book2 = Book(id=2, title="War and Peace", publication_date=datetime(1869, 1, 1), author_id=author2.id)
session.add(book1)
session.add(book2)
session.commit()

# Querying all authors and their books
authors = session.query(Author).all()
for author in authors:
    print(author.name)
    for book in author.books:
        print(f" - {book.title}")

session.close()
#PuTTY, Konsole, Terminator, Terminal and iTerm2.