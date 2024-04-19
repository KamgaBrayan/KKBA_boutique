import datetime
import os
import re


# creation de la boutique

MTC={"Nom":"Excellence En Mathematiques Tle C","Code Barre":"01","Prix":"6400","Stock":10}
MTD={"Nom":"Excellence En Mathematiques Tle D","Code Barre":"02","Prix":"6000","Stock":10}
MTA={"Nom":"Excellence En Mathematiques Tle A","Code Barre":"03","Prix":"5500","Stock":10}
Mathematiques=[MTC,MTD,MTA]
PTC={"Nom":"Physique Tle C","Code Barre":"04","Prix":"6600","Stock":10}
PTD={"Nom":"Physique Tle D","Code Barre":"05","Prix":"6600","Stock":10}  
Physique=[PTC,PTD]
CTC={"Nom":"Chimie Tle C","Code Barre":"06","Prix":"5000","Stock":10}
CTD={"Nom":"Chimie Tle D","Code Barre":"07","Prix":"5000","Stock":10}
Chimie=[CTC,CTD]
ITC={"Nom":"Informatique Tle C","Code Barre":"08","Prix":"4000","Stock":10}
ITD={"Nom":"Informatique Tle D","Code Barre":"09","Prix":"4000","Stock":10}
ITA={"Nom":"Informatique Tle A","Code Barre":"10","Prix":"3000","Stock":10}
Informatique=[ITD,ITC,ITA]
AT={"Nom":"Interaction In English Tle ","Code Barre":"11","Prix":"4000","Stock":10}
Anglais=[AT]
Articles=[Mathematiques,Physique,Chimie,Informatique,Anglais]

def in_low(a:list)->list:
    b=[]
    for element in a:
        b.append(element.lower())
    return b

def Reduction(Articles: list ,Name:str)->list:
     with open(f'./Clients/{Name}.txt','r') as file:
         ligne=file.readline()
         Chaine=" "
         while ligne !="":
             Chaine = Chaine + ligne
             ligne = file.readline()
         for A in Articles:
            for a in A:
                if(Chaine.count(a['Nom'])>=2):
                    print("Vous beneficiez d'une reduction de 2% sur les articles",a['Nom'])
                    a['Prix']=str(int(a['Prix'])*0.98)

                    
client=in_low(os.listdir('./Clients'))
visitors=in_low( os.listdir('./Visitors'))   
    
def Greetings(client:list,visitors:list)->str:
    #
    print("""
        **********WELCOME ON OUR E-BOOK SHOP***********
        Please enter your informations: 
        """)
    Name=input("-Name(Complete):\n")
    print("\nHello Dear ",Name.upper())
    #verify if the current person is already a visitor or a client
    # if it exists we say " Happy to have you back" else "Welcome! happy to have you as a customer"    
    if(client.count(f'{Name.lower()}.txt')!=0):
        print("Happy To Have You Back!\n")
        Reduction(Articles,Name.upper())
    elif (visitors.count(f'{Name.lower()}.txt')!=0):
        print("Happy To Have You Back!\n")
    else:
        print("WELCOME! Happy To Have You as a customer! Hope You'll be satified!\n")
    return Name.upper()


def Show(Articles:list,Name: str):
    print("       *****NOS PRODUITS*****")
    print(f"{'Code Barre':<20s}{'Nom':<70s}{'Prix':>10s}")
    print("-----------------------------------------------------------------------------------------------------------")
    for i in Articles:
        for j in i:
            print(f"{j['Code Barre']:<20s}{j['Nom']:<70s}{j['Prix']:>10s}")
            
def Command()->list:
        C=input("\nEnter your choice( you will enter the number corresponding to the item)\nEx:01,02,03\n")
        Q=input("\nEnter the quantity of each\nEx:1,4,10\n")
        Choice=re.split("[\, ,]+", C)
        Quantity=re.split("[\, ,]+", Q)
        if(len(Choice)!=len(Quantity)):
            Command()
        for c in range(len(Quantity)):
            if (Quantity[c].isnumeric == False or Choice[c].isnumeric == False) :
                print("Une Erreur est Survenue; Veillez reprendre votre commande! ")
                Command()
        return Choice,Quantity


def Bill(Articles:list,Name:str,Choice:list,Quantity:list):
    T=0
    try:
        with open(f'./Clients/{Name}.txt', "a") as file:
            file.write(f" E-BOOK SHOP:::   { str(datetime.datetime.now()) }")
            file.write(f"\n{'QUANTITE':<20s} {'ARTICLES':<50s} {'PRIX U':<20s} {'P Total':<20s}\n")
            for B in Articles:
                for j in B:
                    for i in range(len(Choice)):
                        if j['Code Barre']==Choice[i]:
                            T=int(j['Prix'])*int(Quantity[i])+T
                            file.write(f"{Quantity[i]:<20s} {j['Nom']:<50s} {j['Prix']:<20s} {int(j['Prix'])*int(Quantity[i]):<20d}\n")
            file.write(f"TOTAL A PAYER {T:>90d}\n")
            file.write("_____________________________________________________________________________________________________________________________________________")
    except:
        with open(f'./Clients/{Name}.txt', "w") as file:
            file.write(f" E-BOOK SHOP:::   { str(datetime.datetime.now()) }")
            file.write(f"\n{'QUANTITE':<20s} {'ARTICLES':<50s} {'PRIX U':<20s} {'P Total':<20s}\n")
            for B in Articles:
                for j in B:
                    for i in range(len(Choice)):
                        if j['Code Barre']==Choice[i]:
                            T=int(j['Prix'])*int(Quantity[i])+T
                            file.write(f"{Quantity[i]:<20s} {j['Nom']:<50s} {j['Prix']:<20s} {int(j['Prix'])*int(Quantity[i]):<20d}\n")
            file.write(f"TOTAL A PAYER {T:>90d}\n")
            file.write("_____________________________________________________________________________________________________________________________________________")

def Validation(Articles:list,Name:str,Choice:list,Quantity:list,client:list):
    print("Vous avez Choisi:\n")
    for B in Articles:
        for j in B:
            for i in range(len(Choice)):
                if j['Code Barre']==Choice[i]:
                    print(f"{Quantity[i]}- {j['Nom']:<50s}")
    print("Voulez valider la commande?")
    V=input("1- valider\n2- Annuler et Quitter\n3- Retour Menu Principal\n")
    if(V=='1'):
        Bill(Articles,Name,Choice,Quantity)
        print("Merci de nous avoir fait confiance!\n Vous serez toujours le bienvenu!")
        exit()
    if(V=='2'):
        if(client.count(f'{Name.lower()}.txt')!=0):
            exit()
        else:
            with open(f'./Visitors/{Name}.txt','w') as file:
                file.write(f" E-BOOK SHOP:::   { str(datetime.datetime.now()) }")
                file.write("_____________________________________________________________________________________________________________________________________________")
                exit()
    if(V=='3'):
        Menu_principal(Name)
        

def Menu_principal(Name:str):
    Show(Articles,Name)
    C,Q=Command()
    Validation(Articles,Name,C,Q,client)



Name=Greetings(client,visitors)
Menu_principal(Name)
    
    
    
    
    
