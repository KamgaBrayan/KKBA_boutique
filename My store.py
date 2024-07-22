import datetime
import os
import re

# creation of the shop

MTC = {"Name": "Understanding Mathematics", "Barcode": "01", "Price": "6400", "Stock": 10}
MTD = {"Name": "Applied Mathematics", "Barcode": "02", "Price": "6000", "Stock": 10}
MTA = {"Name": "Mastery in pure Mathematics", "Barcode": "03", "Price": "5500", "Stock": 10}
Mathematics = [MTC, MTD, MTA]
PTC = {"Name": "Newlook in Physics", "Barcode": "04", "Price": "6600", "Stock": 10}
PTD = {"Name": "Nelcon and Parker Physics", "Barcode": "05", "Price": "6600", "Stock": 10}
Physics = [PTC, PTD]
CTC = {"Name": "Understanding Chemistry", "Barcode": "06", "Price": "5000", "Stock": 10}
CTD = {"Name": "Organic Chemistry", "Barcode": "07", "Price": "5000", "Stock": 10}
Chemistry = [CTC, CTD]
ITC = {"Name": "Mastery in Computer Science", "Barcode": "08", "Price": "4000", "Stock": 10}
ITD = {"Name": "Programming - Computer Science", "Barcode": "09", "Price": "4000", "Stock": 10}
ITA = {"Name": "Computer Architecture", "Barcode": "10", "Price": "3000", "Stock": 10}
ComputerScience = [ITD, ITC, ITA]
AT = {"Name": "Interaction in English Tle", "Barcode": "11", "Price": "4000", "Stock": 10}
English = [AT]
Items = [Mathematics, Physics, Chemistry, ComputerScience, English]

def to_lowercase(a: list) -> list:
    b = []
    for element in a:
        b.append(element.lower())
    return b

def Discount(Items: list, Name: str) -> list:
    with open(f'./Clients/{Name}.txt', 'r') as file:
        line = file.readline()
        text = ""
        while line != "":
            text = text + line
            line = file.readline()
        for A in Items:
            for a in A:
                if (text.count(a['Name']) >= 2):
                    print("You get a 2% discount on the items", a['Name'])
                    a['Price'] = str(int(a['Price']) * 0.98)

client = to_lowercase(os.listdir('./Clients'))
visitors = to_lowercase(os.listdir('./Visitors'))

def Greetings(client: list, visitors: list) -> str:
    print("""
        **********WELCOME TO OUR E-BOOK SHOP***********
        Please enter your information: 
        """)
    Name = input("-Full Name:\n")
    print("\nHello Dear", Name.upper())
    # verify if the current person is already a visitor or a client
    # if they exist, we say "Happy to have you back" else "Welcome! happy to have you as a customer"
    if (client.count(f'{Name.lower()}.txt') != 0):
        print("Happy To Have You Back!\n")
        Discount(Items, Name.upper())
    elif (visitors.count(f'{Name.lower()}.txt') != 0):
        print("Happy To Have You Back!\n")
    else:
        print("WELCOME! Happy To Have You as a customer! Hope You'll be satisfied!\n")
    return Name.upper()

def Show(Items: list, Name: str):
    print("       *****OUR PRODUCTS*****")
    print(f"{'Barcode':<20s}{'Name':<70s}{'Price':>10s}")
    print("-----------------------------------------------------------------------------------------------------------")
    for i in Items:
        for j in i:
            print(f"{j['Barcode']:<20s}{j['Name']:<70s}{j['Price']:>10s}")

def Order() -> list:
    C = input("\nEnter your choice (you will enter the number corresponding to the item)\nEx: 01, 02, 03\n")
    Q = input("\nEnter the quantity of each\nEx: 1, 4, 10\n")
    Choice = re.split("[\, ,]+", C)
    Quantity = re.split("[\, ,]+", Q)
    if (len(Choice) != len(Quantity)):
        Order()
    for c in range(len(Quantity)):
        if (Quantity[c].isnumeric() == False or Choice[c].isnumeric() == False):
            print("An error occurred; please restart your order!")
            Order()
    return Choice, Quantity

def Bill(Items: list, Name: str, Choice: list, Quantity: list):
    T = 0
    try:
        with open(f'./Clients/{Name}.txt', "a") as file:
            file.write(f"E-BOOK SHOP:::   {str(datetime.datetime.now())}")
            file.write(f"\n{'QUANTITY':<20s} {'ITEMS':<50s} {'UNIT PRICE':<20s} {'TOTAL PRICE':<20s}\n")
            for B in Items:
                for j in B:
                    for i in range(len(Choice)):
                        if j['Barcode'] == Choice[i]:
                            T = int(j['Price']) * int(Quantity[i]) + T
                            file.write(f"{Quantity[i]:<20s} {j['Name']:<50s} {j['Price']:<20s} {int(j['Price']) * int(Quantity[i]):<20d}\n")
            file.write(f"TOTAL AMOUNT DUE {T:>90d}\n")
            file.write("_____________________________________________________________________________________________________________________________________________")
    except:
        with open(f'./Clients/{Name}.txt', "w") as file:
            file.write(f"E-BOOK SHOP:::   {str(datetime.datetime.now())}")
            file.write(f"\n{'QUANTITY':<20s} {'ITEMS':<50s} {'UNIT PRICE':<20s} {'TOTAL PRICE':<20s}\n")
            for B in Items:
                for j in B:
                    for i in range(len(Choice)):
                        if j['Barcode'] == Choice[i]:
                            T = int(j['Price']) * int(Quantity[i]) + T
                            file.write(f"{Quantity[i]:<20s} {j['Name']:<50s} {j['Price']:<20s} {int(j['Price']) * int(Quantity[i]):<20d}\n")
            file.write(f"TOTAL AMOUNT DUE {T:>90d}\n")
            file.write("_____________________________________________________________________________________________________________________________________________")

def Validation(Items: list, Name: str, Choice: list, Quantity: list, client: list):
    print("You have chosen:\n")
    for B in Items:
        for j in B:
            for i in range(len(Choice)):
                if j['Barcode'] == Choice[i]:
                    print(f"{Quantity[i]}- {j['Name']:<50s}")
    print("Do you want to confirm the order?")
    V = input("1- Confirm\n2- Cancel and Exit\n3- Return to Main Menu\n")
    if (V == '1'):
        Bill(Items, Name, Choice, Quantity)
        print("Thank you for your trust!\n You will always be welcome!")
        exit()
    if (V == '2'):
        if (client.count(f'{Name.lower()}.txt') != 0):
            exit()
        else:
            with open(f'./Visitors/{Name}.txt', 'w') as file:
                file.write(f"E-BOOK SHOP:::   {str(datetime.datetime.now())}")
                file.write("_____________________________________________________________________________________________________________________________________________")
                exit()
    if (V == '3'):
        main_menu(Name)

def main_menu(Name: str):
    Show(Items, Name)
    C, Q = Order()
    Validation(Items, Name, C, Q, client)

Name = Greetings(client, visitors)
main_menu(Name)
