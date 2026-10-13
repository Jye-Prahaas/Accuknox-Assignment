import numpy as np
import pandas as pd

df=pd.read_csv("customers-1000.csv")
print(df.head())

names=df["First Name"]
mails=df["Email"]


import sqlite3

connection=sqlite3.connect("Personal_info.db")

cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS info(
Name TEXT,
Email TEXT
)
""")

connection.commit()

for index,row in df.head(10).iterrows():
    names=row["First Name"]
    mails=row["Email"]

    print(names)
    print(mails)


    cursor.execute("""INSERT INTO info(Name,Email)
    VALUES(?,?)""",
    (names,mails)
    )

connection.commit()

cursor.execute("SELECT Name ,Email FROM info")
for row in cursor.fetchall():
    print(row)




