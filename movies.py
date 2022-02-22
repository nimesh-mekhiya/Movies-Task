"""Read CSV file and Store in the Database"""

from sqlite3 import connect
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="movies"
)
cursor = conn.cursor()

# Create Table
try:
    data = "CREATE TABLE IF NOT EXISTS moviesTable(ID INT(8),movie_name VARCHAR(255), movie_rating VARCHAR(255), movie_release VARCHAR(255), movie_duration VARCHAR(255), movie_desc VARCHAR(255))"
    cursor.execute(data)
    print("Table created Sucessfully!")
except Exception as e:
    print("Eror in Table creation", e)

# Read CSV with Insert into the Table
path = r'C:/Users/Nimesh Mekhiya/movie1.csv'
data = pd.read_csv(path, encoding='latin-1')
data = data.fillna('')

try:
    for i, row in data.iterrows():
        no = i
        name = row['movie_name']
        rating = row['movie_rating']
        release = row['movie_release']
        duration = row['movie_duration']
        desc = row['movie_desc']

        cursor.execute("INSERT INTO moviesTable (ID,movie_name, movie_rating, movie_release, movie_duration, movie_desc) VALUES (%s, %s, %s, %s, %s, %s)", (no,
                       row.movie_name, row.movie_rating, row.movie_release, row.movie_duration, row.movie_desc))

        conn.commit()
    print("Data Insert Successfully!")
except Exception as e:
    print(e)
