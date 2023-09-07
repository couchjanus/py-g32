# 
# convert_sql_to_csv.py
import csv
import sqlite3

conn = sqlite3.connect('blogger.db')
cursor = conn.cursor()
cursor.execute("select * from post;")

with open("blogger.csv", 'w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)
conn.close()
