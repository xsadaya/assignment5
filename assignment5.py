# Program Name: assignment5.py
# Course: IT3883
# Sadaya Preston
# Assignment 5
# 04/22/2026
# Purpose: This program creates a SQLite database and
# stores temperature data and calculates average
# temperatures for sunday and thurday

import sqlite3

# create andconnect to database
conn = sqlite3.connect("temperature.db")

# create cursor object
cursor = conn.cursor()

# creating the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS TemperatureData (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)
""")

# open the input file and read data
with open("Assignment5input.txt", "r") as file:
    for line in file:

        # split each line into parts
        parts = line.strip().split()

        # store values into variables
        day = parts[0]
        temp = float(parts[1])

        # insert values into database
        cursor.execute("""
        INSERT INTO TemperatureData (Day_Of_Week, Temperature_Value)
        VALUES (?, ?)
        """, (day, temp))

# save changes
conn.commit()

# calculate sunday average
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM TemperatureData
WHERE Day_Of_Week = 'Sunday'
""")

sunday_avg = cursor.fetchone()[0]

# calculate thursday average
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM TemperatureData
WHERE Day_Of_Week = 'Thursday'
""")

thursday_avg = cursor.fetchone()[0]

# print results
print(f"Average Sunday Temperature: {sunday_avg:.2f}")
print(f"Average Thursday Temperature: {thursday_avg:.2f}")

# close database connection
conn.close()
