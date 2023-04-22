import csv
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def create_table():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS measurements (
                id INT AUTO_INCREMENT PRIMARY KEY,
                waist INT NOT NULL,
                age INT NOT NULL,
                height INT NOT NULL,
                weight INT NOT NULL,
                UNIQUE KEY unique_index (waist, age, height, weight)
            )
        """)

        conn.commit()
        print("Table created successfully")

    except mysql.connector.Error as error:
        print("Error creating table: {}".format(error))

    finally:
        cursor.close()
        conn.close()

def insert_data():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        with open('data/measurements.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                cursor.execute("""
                    INSERT IGNORE INTO measurements (waist, age, height, weight) 
                    VALUES (%s, %s, %s, %s)
                """, (row[' Waist (cm)'], row[' Age'], row['Height (cm)'], row[' Weight (kgs)']))


        conn.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print("Error inserting data: {}".format(error))

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_table()
    insert_data()
