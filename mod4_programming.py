# 11.1
import zoo

zoo.hours()

# 11.2
import zoo as menagerie

menagerie.hours()

# 16.8
import sqlalchemy
from sqlalchemy import text

engine = sqlalchemy.create_engine('sqlite://')

with engine.connect() as conn:
    conn.execute(text('''
    CREATE TABLE books (
        title VARCHAR(20) PRIMARY KEY,
        author VARCHAR(30)
        year INT
    '''))
