import smtplib
import random
prices = {
    "teddybear": 200,
    "bag": 150,
    "makeupkit": 300,
    "modelearings": 100,
    "facecream": 50,
    "chocolate": 20,
    "oreobiscuit": 10,
    "dryfruits": 250,
    "icecream": 30,
    "shoes": 400
}
GST_RATE = 0.18
def teddybear():
    print("You selected teddy bear mam")
    return "teddy bear", prices["teddybear"]
def bag():
    print("You selected bag")
    return "bag", prices["bag"]
def makeupkit():
    print("You selected makeup kit mam")
    return "makeup kit", prices["makeupkit"]
def modelearings():
    print("You selected model earrings mam")
    return "model earrings", prices["modelearings"]
def facecream():
    print("You selected face cream mam")
    return "face cream", prices["facecream"]
def chocolate():
    print("You selected chocolate mam")
    return "chocolate", prices["chocolate"]
def oreoBiscuit():
    print("You selected oreo biscuit mam")
    return "oreo biscuit", prices["oreobiscuit"]
def dryfruits():
    print("You selected dry fruits mam")
    return "dry fruits", prices["dryfruits"]
def icecream():
    print("You selected ice cream mam")
    return "ice cream", prices["icecream"]
def shoes():
    print("You selected shoes mam")
    return "shoes", prices["shoes"]
def main():
    selected_items = []
    total_price = 0
    try:
        while True:
            print("\n===== 5 Star Supermarket =====")
            print("1. teddy bear")
            print("2. bag")
            print("3. makeup kit")
            print("4. model earrings")
            print("5. face cream")
            print("6. chocolate")
            print("7. oreo biscuit")
            print("8. dry fruits")
            print("9. ice cream")
            print("10. shoes")
            print("0. Exit")
            user = int(input("Enter your choice: "))
            if user == 0:
                print("Exiting program.")
                break
            elif user == 1:
                item, price = teddybear()
            elif user == 2:
                item, price = bag()
            elif user == 3:
                item, price = makeupkit()
            elif user == 4:
                item, price = modelearings()
            elif user == 5:
                item, price = facecream()
            elif user == 6:
                item, price = chocolate()
            elif user == 7:
                item, price = oreoBiscuit()
            elif user == 8:
                item, price = dryfruits()
            elif user == 9:
                item, price = icecream()
            elif user == 10:
                item, price = shoes()
            else:
                print("Invalid input. Please enter a number from 0 to 10.")
                continue
            selected_items.append((item, price))
            total_price += price
            con = input("Do you want to continue? (yes/no): ")
            if con.lower() != "yes":
                break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"Error occurred: {e}")
    gst_amount = total_price * GST_RATE
    total_amount_with_gst = total_price + gst_amount
    print("\nSelected Items:")
    for item, price in selected_items:
        print(f"{item}: {price}")
    print(f"\nTotal Price: {total_price}")
    print(f"GST (18%): {gst_amount:.2f}")
    print(f"Total Amount with GST: {total_amount_with_gst:.2f}")
    return selected_items, total_amount_with_gst
def email_sending(selected_items, total_amount):
    try:
        receiver_mails = ["jasminesaferali@gmail.com"]
        for i in receiver_mails:
            otp_number = random.randint(1000, 9999) 
            print(i, otp_number)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("vengateshbalu16@gmail.com", "mcif tfjv akei gbsf")
            items_detail = "\n".join([f"{item}: {price}" for item, price in selected_items])
            message = f"Your bill mam,\nYour OTP number is {otp_number}\nSelected Items:\n{items_detail}\nTotal Amount with GST: {total_amount:.2f}"
            s.sendmail("vengateshbalu16@gmail.com", i, message)
            s.quit()
            print("Your bill is generated")
    except Exception as e:
        print(f"Your bill is not generated. Error: {e}")
if __name__ == "__main__":
    selected_items, total_amount_with_gst = main()
    email_sending(selected_items, total_amount_with_gst)
