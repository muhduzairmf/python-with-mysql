# install mysql-connector by 'pip install mysql-connector'
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "python_mysql"
)

print(mydb)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE python_mysql")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])
# Will show the existing databases

# my_cursor.execute("CREATE TABLE customers (id INT PRIMARY KEY AUTO_INCREMENT,first_name VARCHAR(100),last_name VARCHAR(100),email VARCHAR(100) UNIQUE)")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])
# Will show the existing tables

# insertCommand = "INSERT INTO customers(first_name, last_name, email) VALUES(%s, %s, %s)"
# record1 = ("John", "Doe", "johndoe@email.com")
# my_cursor.execute(insertCommand, record1)

# many_customers = [
#     ('Ben', 'Smith', 'bensmith@email.com'),
#     ('Sara', 'Thompson', 'sara@email.com'),
#     ('Karen', 'Larsson', 'karenlarsson@email.com'),
# ]
# insert_command = "INSERT INTO customers(first_name, last_name, email) VALUES(%s, %s, %s)"
# for customer in many_customers:
#     my_cursor.execute(insert_command, customer)

# my_cursor.execute("SELECT * FROM customers")
# for record in my_cursor:
#     print(record)
# for record in my_cursor:
#     print(f"ID: {record[0]}")
#     print(f"First name: {record[1]}")
#     print(f"Last name: {record[2]}")
#     print(f"Email: {record[3]}")

# my_cursor.execute("UPDATE customers SET last_name = 'McThompson' WHERE id = 4")

# my_cursor.execute("DELETE FROM customers WHERE id = 4")

mydb.commit()
mydb.close()
