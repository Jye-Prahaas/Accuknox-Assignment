import sys
sys.stdout.reconfigure(encoding="utf-8")

import requests
import json

URL =  "https://openlibrary.org/search.json?title=atomic+habits"

response=requests.get(URL,timeout=10)

data=response.json()

print("Status:",response.status_code)

print("Data Type:",type(data))

print(data)

books=data["docs"]

print("First book:",books[0]["title"])


first_book=books[0]

# print("author_name:",first_book.get("author_name"))
# print("title:",first_book.get("title"))
# print("Year:",first_book.get(""))



for book in books[:5]:

    print("Author Name:",book.get("author_name"))
    print("Title:",book.get("title"))
    print("Year:",book.get("first_publish_year"))



import sqlite3

connection=sqlite3.connect("book_info.db")

cursor= connection.cursor()

cursor.execute(""" 
CREATE TABLE IF  NOT EXISTS book(
author_name TEXT,
title TEXT,
Year INTEGER )
""")

connection.commit()

for book in books[:5]:
     
    authors = book.get("author_name", [])
    title = book.get("title")
    year = book.get("first_publish_year")

    cursor.execute("""
    INSERT INTO book (author_name ,title ,Year)
    VALUES(?,?,?)""",

    (authors[0] if authors else "Unknown",title,year)


    )


    
connection.commit()

cursor.execute("SELECT author_name,title,year FROM book")
for row in cursor.fetchall():
      print(row)

connection.commit()



