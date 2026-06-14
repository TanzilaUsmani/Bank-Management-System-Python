import json
import random
import string
from pathlib import Path

class Bank:

    database='data.json'
    data=[]
    try: 
     if Path(database).exists():
       with open (database) as fs:
        data=json.loads(fs.read())
     else :
        print("No such file exist")   
    except Exception as err:
       print(f"print error{err}")

    @staticmethod
    def update():
      with open(Bank.database,"w")as fs:
         fs.write(json.dumps(Bank.data))

    def crateaccount(self):
        obj={
           "name":input("Enter name here"),
           "age":int(input("Enter Age here")),
           "email":input("Enter email here"),
           "pin":int(input("Enter pin here")),
            "accountNumber": random.randint(100000, 999999),
           "balance":0
        }
        if obj['age']<18 or len(str(obj['pin']))!=4:
         print("You can not create an account")
        else:
          print("Account is created")
          for i in obj:
           print(f"{i}:{obj[i]}")
        print("please note down your account number")
        Bank.data.append(obj)
        Bank.update()

    def depositemony(self):
       accnumber=int(input("Entre your account number"))
       pin=int(input("Enter your pin "))
       userdata=[i for i in Bank.data if i['accountNumber']==accnumber and i['pin']==pin] # Created  deep copy
       if userdata==False:
         print("Sory no data found")
       else:
         amount=int(input("Enter amount you want to deposite"))
         if amount>10000 or amount<0:
           print("You can;t desposite money")

         else:
           print(userdata)
           userdata[0]['balance'] += amount
           Bank.update()
           print("Amount deposite succesffuly")

    def withdraw(self):
       accnumber=int(input("Entre your account number"))
       pin=int(input("Enter your pin "))
       userdata=[i for i in Bank.data if i['accountNumber']==accnumber and i['pin']==pin] # Created  deep copy
       if userdata==False:
         print("Sory no data found")
       else:
         amount=int(input("Enter amount you want to withdrraw"))
         if amount>10000 or amount<0:
           print("You can;t desposite money")

         else:
           print(userdata)
           userdata[0]['balance'] -= amount
           Bank.update()
           print("Amount withdrwaw succesffuly")

    def showdeatils(self):
      accnumber=int(input("Entre your account number"))
      pin=int(input("Enter your pin "))   
      userdata=[i for i in Bank.data if i['accountNumber']==accnumber and i['pin']==pin]  
      for i in userdata[0]:
        print(f"{i}:{userdata[0][i]}")
    

user=Bank()
print("press 1 for creating an account")
print("press 2 for Deposite money ")
print("press 3 for withdarw money")
print("press 4 for for deatils")
print("press 5 for exit")


check=int(input("tell your response"))

if check==1:
   user.crateaccount()

if check==2:
   user.depositemony()

if check==3:
   user.withdraw()

if check==4:
   user.showdeatils()

elif check==5:
   print("Thank you for using Bank Management System")
   exit()

else:
   print("Invalid Choice")