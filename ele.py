import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="anush@1617",
    database="election_list"
    )
mycursor=mydb.cursor()
def   insert_data():
        sql="insert into vote_list_details(candidate_no,candidate_name,vote_commite_area,voter_id_number) values (%s,%s,%s,%s)"
        candidate_no=int(input("enter your candidate_no:"))
        candidate_name=input("enter your candidate_name :")
        vote_commite_area=input("enter your vote_commite_area:")
        voter_id_number=int(input("enter your voter_id_number:"))
        val=(candidate_no,candidate_name,vote_commite_area,voter_id_number)
        mycursor.execute(sql,val)
        mydb.commit()
        print("data saved successfully")
import smtplib
import random
def  email_sending():
    try:
        receiver_mails=["jasminesaferali@gmail.com"]
        for i in receiver_mails:
             otp_number=random.randint(0000,9999)
             print(i,otp_number)
             s=smtplib.SMTP('smtp.gmail.com',587)
             s.starttls()
             s.login("vengateshbalu16@gmail.com","mcif tfjv akei gbsf")
             message=f"your voted sucessfully,\nyour otp number is{otp_number}"
             s.sendmail("vengateshbalu16@gmail.com",i,message)
             s.quit()
             print("mail sent successfully")            
    except:
             print("mail not send")         
insert_data()
def  view_data():
    mycursor.execute("select * from vote_list_details")
    myresult=mycursor.fetchall()
    for i in myresult:
         print(i)
         email_sending()         
         insert_data()
view_data()
     





