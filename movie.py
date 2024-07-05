import mysql.connector
import smtplib
import random

def main():
    while True:
        print("\n===== Movie Ticket Counter =====")
        print("1. Enter Movie Details")
        print("2. Insert Data into Database")
        print("3. Send Email")
        print("4. View Data")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            enter_movie_details()
        elif choice == '2':
            insert_data()
        elif choice == '3':
            email_sending()
        elif choice == '4':
            view_data()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter a number from 0 to 4.")

def enter_movie_details():
    film = input("Enter your movie name: ")
    ticket = input("Enter your ticket type: ")
    snacks = input("Enter your snacks: ")
    
    if film in ("star", "aranmanai", "leo", "karudan"):
        print("Yes, movie ticket counter")
    if ticket.lower() == "firstclass":
        print("Hi mam, it's a first class ticket. Enjoy your movie")
    if snacks.lower() == "popcorn":
        print("Enjoy your snacks mam")
    if film not in ("star", "aranmanai", "leo", "karudan") and ticket.lower() != "firstclass" and snacks.lower() != "popcorn":
        print("This is not the theater")

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="anush@1617",
        database="movie"
    )

def insert_data():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    
    sql = "INSERT INTO movie_list (aranmanai, leo, star, karudan) VALUES (%s, %s, %s, %s)"
    aranmanai = int(input("How many Aranmanai movie tickets do you want: "))
    leo = int(input("How many Leo movie tickets do you want: "))
    star = int(input("How many Star movie tickets do you want: "))
    karudan = int(input("How many Karudan movie tickets do you want: "))
    val = (aranmanai, leo, star, karudan)
    
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("Data saved successfully")
    mycursor.close()
    mydb.close()

def email_sending():
    try:
        receiver_mails = ["jasminesaferali@gmail.com"]
        for i in receiver_mails:
            otp_number = random.randint(1000, 9999)
            print(f"Sending email to {i} with OTP: {otp_number}")
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("vengateshbalu16@gmail.com", "mcif tfjv akei gbsf")
            message = f"Your voting was successful,\nYour OTP number is {otp_number}"
            s.sendmail("vengateshbalu16@gmail.com", i, message)
            s.quit()
            print("Mail sent successfully")
    except Exception as e:
        print(f"Mail not sent. Error: {e}")

def view_data():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM movie_list")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    main()

