import csv
import os

class BankSystem:
   

    def __init__(self, first_name,last_name, password, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.password = password
        # self.checking = False # assume its false
        # self.saving = False
        
    def create_account(self):
        u = input(" Do you have an account ? answer Y or N ")
        if u == "Y":
            return f" Enter your Email {self.email} and password {self.password} "
        else:
            return f"Enter your first name {self.first_name} and last name {self.last_name} , and your email {self.email} and your password {self.password}"
        

    
######### not sure where to put this 

    def both_saving_checking(self):
        if self.checking  and self.saving :
            return " Customer have both checking and saving account" # make sure 1 for each
        elif  not self.checking and self.saving :
            return " Customer just have a saving account "
        elif self.checking and not self.saving :
            return "Customer has an account "
        else:
            return "Customer does not have an account "
        
    # u=input(" Welcome to the Bank Application if you want to create a new account type : new or type else")
    # if u == "new":
    #     create_account()
    # else:
    #     i=input("if you want to check your account type: check or for your saving account type :saving")
    #     if i=="check":
    #        checking_account()
    #     elif i=="saving":
    #         saving_account()
    #     else:
    #         print("start again ")
    
class Customer:
    def __init__(self, first_name, last_name, password):
        self.first_name=first_name
        self.last_name=last_name
        self.password = password
        self.create_account = False # assume its false
        self.active = True


    def login(self):
        u = input(f"Do you want to create a new account type : new or to log in type : login ")
        if u=="new" or u=="NEW":
            return f"Enter your First name {self.first_name} and Last Name : {self.last_name} and password {self.password} "
        if u=="login" or u=="LOGIN" : 
           u = input(f"Enter your id and {self.id} and password {self.password} to log in ")
        if self.id in csv: 
            return " Log in Successfully "
        else:
               return " Try again , Incorrect Name or Password "
    
    def logout(self):
        try:
            u=input(" for logout type : quit")
            if self.id in csv :
                print("log out Successfully ")
                quit()
        except:
            return "Error"
    
    def info(self):
        if self.active == True:
            return f" first name : {self.first_name} last name : {self.last_name} id :{self.id} your account is active :{self.active}"
        else:
             return f" first name : {self.first_name} last name : {self.last_name} id :{self.id} , account is not active :{self.active}"
    # load data from csv file 


fieldnames = ["id" , "first_name" ,"last_name" ,"password","checking" , "savings", "active" ,"overdraft_count"]
if not os.path.exists("./bank.csv"):
            with open("./bank.csv", 'w', newline='') as csvfile:
                try:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in fieldnames:
                        writer.writerow(row)
                except csv.Error as e:
                    print(e)

# 4.0 If Exists - ReadFile / Rows:
try: 
    with open("bank.csv", "r") as file:
        contents = csv.DictReader(file)
        for row in contents:
            print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
            for prop in fieldnames:
                print(row[prop]) # will print the value of each individual property
except csv.Error as e:
    print(e)


class checking_account(BankSystem):
    def __init__(self):
        super().__init__(id, self.password)
        self.checking=False

    
    def checking_account(self):

        if self.id and self.password in csv : # check if id and password match 
            return f"Customer has an account id :{self.id} , and your checking is :{self.checking}"
        elif self.checking == False:
            return " you don't have a checking account "
        elif type(self.checking) == str:
                self.checking = int(self.checking)
                return self.checking
        else:
            print(" you dont have a checking account , you need to Make a new Account")
    



class saving_acccount(BankSystem):
    def __init__(self):
        super().__init__(id, self.password)
        self.saving=False

    def saving_account(self):
        
        if self.id and self.password in csv : # in csv
            return f" you have a saving account  :{self.id} and your saving is : {self.saving}"
        elif self.saving==False:
            return "you dont have a saving account"
        elif type(self.saving) == str:
                self.saving = int(self.saving)
                return self.saving
        else:
            return " you don't have saving account"
        
        



# print(Customer.create_account())
# print(Customer.saving_account())
# print(Customer.checking_account())

