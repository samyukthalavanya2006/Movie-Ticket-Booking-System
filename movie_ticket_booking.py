import mysql.connector
import random

# DATABASE CONNECTION
db_name = input("Enter Database Name: ")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567"
)

if mydb.is_connected():
    print("Database Connected Successfully")

mycursor = mydb.cursor()

# CREATE DATABASE
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
print("Database Created Successfully")

# USE DATABASE
mycursor.execute(f"USE {db_name}")

# CREATE TABLES
mycursor.execute("""
CREATE TABLE IF NOT EXISTS theatre(
    Customer_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(100),
    Phone_No VARCHAR(15),
    No_Tickets INT,
    Sex VARCHAR(10),
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Email_ID VARCHAR(100),
    Mode_Payment VARCHAR(50)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS gold_4dx(
    Customer_ID INT,
    Movie_Name VARCHAR(100),
    Amount INT
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS imax(
    Customer_ID INT,
    Movie_Name VARCHAR(100),
    Amount INT
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS silver(
    Customer_ID INT,
    Movie_Name VARCHAR(100),
    Amount INT
)
""")

print("\n")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("        SAMYUKTHA THEATRE BOOKING")
print("        YOUR SAFETY IS OUR PRIORITY")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# SHOW DETAILS
choice = input("\nDo you want to check show details? (yes/no): ")

if choice.lower() == "yes":

    print("\n============== SHOW DETAILS ==============")
    print("a. Morning Show")
    print("b. Noon Show")
    print("c. Night Show")

    show = input("Enter your choice: ")

    if show == 'a':
        print("\nTime: 9:00 AM")
        print("Screen 1 : Avatar")
        print("Screen 2 : Aquaman")

    elif show == 'b':
        print("\nTime: 1:00 PM")
        print("Screen 1 : After")
        print("Screen 2 : Lucy")

    elif show == 'c':
        print("\nTime: 10:00 PM")
        print("Screen 1 : TVD")
        print("Screen 2 : Baywatch")

# CUSTOMER DETAILS
print("\n========== CUSTOMER DETAILS ==========")

movie_name = input("Enter Movie Name: ")
phone = input("Enter Phone Number: ")
tickets = int(input("Enter Number of Tickets: "))
sex = input("Enter Gender: ")
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
email = input("Enter Email ID: ")
payment = input("Enter Payment Mode: ")

# GENERATE CUSTOMER ID
customer_id = random.randint(1000, 9999)

print(f"\nYour Customer ID is: {customer_id}")

# INSERT CUSTOMER DETAILS
insert_query = """
INSERT INTO theatre
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

values = (
    customer_id,
    movie_name,
    phone,
    tickets,
    sex,
    fname,
    lname,
    email,
    payment
)

mycursor.execute(insert_query, values)
mydb.commit()

# TICKET BOOKING
print("\n========== TICKET BOOKING ==========")

print("1. GOLD 4DX")
print("   Ticket Price : Rs.1500")

print("2. IMAX")
print("   Ticket Price : Rs.850")

print("3. SILVER")
print("   Ticket Price : Rs.500")

ticket_choice = int(input("\nEnter your choice: "))

# GOLD 4DX
if ticket_choice == 1:

    print("\nWELCOME TO GOLD 4DX BOOKING")

    no_tickets = int(input("Enter Number of Tickets: "))

    total = no_tickets * 1500

    print("Total Bill:", total)

    otp = input("Enter Payment OTP: ")

    snacks = input("Complimentary Snacks (chips/popcorn/no): ")
    drinks = input("Complimentary Drinks (coke/pepsi/no): ")

    query = """
    INSERT INTO gold_4dx
    VALUES (%s,%s,%s)
    """

    mycursor.execute(query, (customer_id, movie_name, total))
    mydb.commit()

# IMAX
elif ticket_choice == 2:

    print("\nWELCOME TO IMAX BOOKING")

    no_tickets = int(input("Enter Number of Tickets: "))

    total = no_tickets * 850

    print("Total Bill:", total)

    otp = input("Enter Payment OTP: ")

    snacks = input("Complimentary Snacks (chips/popcorn/no): ")
    drinks = input("Complimentary Drinks (coke/pepsi/no): ")

    query = """
    INSERT INTO imax
    VALUES (%s,%s,%s)
    """

    mycursor.execute(query, (customer_id, movie_name, total))
    mydb.commit()

# SILVER
elif ticket_choice == 3:

    print("\nWELCOME TO SILVER BOOKING")

    no_tickets = int(input("Enter Number of Tickets: "))

    total = no_tickets * 500

    print("Total Bill:", total)

    otp = input("Enter Payment OTP: ")

    query = """
    INSERT INTO silver
    VALUES (%s,%s,%s)
    """

    mycursor.execute(query, (customer_id, movie_name, total))
    mydb.commit()

print("\n====================================")
print("       TICKET BOOKED SUCCESSFULLY")
print("        ENJOY YOUR MOVIE")
print("====================================")

print("\nThanks For Visiting")
