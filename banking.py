import csv
import os


class BankSystem:

    # id = '100012'
    password =""
    accounts = []
    curr_customer = None
    checking = None
    saving = None

    def __init__(self):
        pass

    @classmethod
    def create_account(cls):
            u = input(" Do you want to create an account ? answer Y or N  : ").strip()
            if u == "Y" or  u == "Y".lower() :
                s = input("Do you want a saving account (type : saving ) or checking account (type : checking ) or both :").strip()
                
                first_name= input("Enter your first name: ").strip()
                last_name= input("Enter your last name: ").strip()
                password = input("Enter your password : ").strip()
              
                active= True
                overdraft_count=0 
                fieldnames = ["id", "first_name", "last_name", "password", "active", "overdraft_count", "savings", "checking"]
                # updating the id 
                with open("./bank.csv", 'r', newline='') as csvfile:
                    r = csv.DictReader(csvfile, fieldnames=fieldnames)
                    max_id=100012
                    for row in r:
                        if row["id"].isdigit(): # make sure its number for calculation
                            max_id=max(max_id, int(row["id"]))
                    cls.id=str(max_id + 1)
                    
                customer_dict = {
                        "id" : cls.id,
                        "first_name" :first_name,
                        "last_name" :last_name,
                        "password": password,
                        "checking": False, #default
                        "savings" : False,
                        "active" :active ,
                        "overdraft_count" :overdraft_count
                    }
                
                cls.curr_customer = customer_dict
                cls.accounts.append(cls.curr_customer)

               
                if s =="SAVINGS" or s=="Savings".lower():
                    cls.savings = 0
                    cls.checking = False
                    return cls.saving_account() 
                
                elif s =="CHECKING" or s =="checking".lower():
                    cls.checking = 0
                    cls.savings = False
                    return cls.checking_account()
                
                elif s=="both" or s=="BOTH".lower():
                    cls.checking = 0
                    cls.savings = 0
                    cls.curr_customer["checking"] = "0"
                    cls.curr_customer["savings"] = "0"
                    return cls.both_saving_checking()
                
                else:
                    cls.checking = 0
                    cls.savings = 0
                    return cls.both_saving_checking()# both saving & checking

                
                    
            else:
                quit()
                 
            
    @classmethod
    def loadAccounts(cls):  
        # from load data load the accounts  
        print("***** Loading the accounts from the csv file *****")
        
        if not os.path.exists("bank.csv"):
            print(" bank.csv does not exist ")

        try: 
            with open("bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    cls.accounts.append(row)
                #print(f"the accounts list is : {cls.accounts}")
                return cls.accounts

        except csv.Error as e:
            print(f"Error loading the accounts : {e}")
      
    @classmethod
    def login(cls):
            # print("login function in bank class running!!! line 25")
            user_id = input(f"Enter your ID :").strip()
            password = input(f"Enter your password :").strip()
            try:
                with open("bank.csv", "r") as file:
                    contents = csv.DictReader(file)
                    for row in contents:
                        if row["id"] == user_id and row["password"]== password:
                                print(f"Login Successfully !!! welcome {row['first_name']} {row['last_name']}")
                                #Todo: transform the text into dictionary
                                customer_dict = {
                                "id" : row["id"],
                                "first_name" :row["first_name"],
                                "last_name" :row["last_name"],
                                "password": row["password"],
                                "checking": row["checking"],
                                "savings" : row["savings"],
                                "active" :row["active"] ,
                                "overdraft_count" :row["overdraft_count"]
                            }

                                cls.curr_customer = customer_dict
                                return 
                    print("Invalid ID or Password , try again ")
                
            except Exception as e:
                 print(f" error occurred :{e}")

    @classmethod
    def logout(cls):
        if cls.curr_customer:
            print(f"{cls.curr_customer['first_name']} {cls.curr_customer['last_name']} has logged out successfully !")
            cls.curr_customer=None # return it to none = empty
        else:
             print(" no user has logged in yet")
    
    @classmethod
    def saving_account(cls):
        if not cls.curr_customer: # if its not log in
            print("you must Log in to access , try again ")
            return
         
        sav = cls.curr_customer
        sav_up=sav.get("savings") # to bring the key saving 
        print(f" your savings account is : ${sav_up}") 
        if sav_up =="False" or sav_up is False:
            print(" you dont have a savings account ")
            return
        
        print(f" your savings account is : ${sav_up}") 

    @classmethod
    def checking_account(cls):
         if not cls.curr_customer:
              print(" No user logged in right now")
              return 
         c = cls.curr_customer
         checking = c.get("checking") # to bring the key checking
         if checking == "False" or checking is False:
            print(" you dont have a checking account ")
            return 
         print(f" Your checking amount is : ${checking}")

    @classmethod
    def both_saving_checking(cls):
        if not cls.curr_customer:
              print("you must Log in to access")
              return 
        sav = cls.curr_customer
        sav_up=sav.get("savings") # to bring the key saving 

        c = cls.curr_customer
        checking = c.get("checking") # to bring the key checking

        is_checking = checking not in [None , "", False, "False"] # if it has an account not falsey value 
        is_saving=sav_up not in [None , "", False, "False"] # if it has an account not falsey value 

        if is_checking and is_saving :
            print(f" your saving amount is: ${sav_up} and your checking amount is : ${checking}")
        elif is_checking: # if cheaking == true       
            print(f"you have a checking account with the amount : ${checking}")
        elif is_saving: # if saving == true
             print(f"you have a saving account with the amount : ${sav_up}")
        else:
            print("unfortunately you dont have saving or checking account ")
         
              
    
class Customer:
    curr_customer=False
    def __init__(self,id, first_name, last_name, password,savings, checking, active=True):

        self.first_name=first_name
        self.last_name=last_name
        self.password = password
        self.id = id
        self.active = active
        self.savings=savings
        self.checking=checking
    
    # @classmethod
    def info(self):
        if str(self.active).lower() =="False":
            print(f"Customer Info : ID: {self.id}, Name : {self.first_name}{self.last_name}, password :{self.password} , saving:{self.savings}, checking:{self.checking} Active: {self.active}")
        else:
            print(f"Customer Info : ID: {self.id}, Name : {self.first_name}{self.last_name}, password :{self.password} ,saving:{self.savings}, checking:{self.checking}, Active: {self.active}")

class operation:

    @classmethod
    def Withdraw(cls):
        # should login to Withdraw
        acc=input(" from which account you want to make the withdraw (1) savings or (2) checking :").lower()
        if acc=="1" or acc == "savings":
            acc="savings"

        elif acc == "2" or acc =="checking":
            acc = "checking"
        else:
            return "Invalid account type"
    
            # print(BankSystem.curr_customer)
        
        a=input(" type the money amount you want to make the withdraw with : ").strip()
        # print(a)
        print( a.isnumeric() is True)
        if a.isnumeric() is True:
            a= int(a)
        op=overdraftProtection(BankSystem.curr_customer)
        success = op.withdraw(acc, a)

        if success:
            cls.update_acc(BankSystem.curr_customer["id"], acc, BankSystem.curr_customer[acc])
        else:
            print("Withdrawal faild")
        
        balance = int(BankSystem.curr_customer[acc])# convert it to int to make calculation
        
        if balance >= a: # if account has enough money
            new_b= balance - a
            BankSystem.curr_customer[acc] = str(new_b) # convert it again to string for the csv
            cls.update_acc(BankSystem.curr_customer["id"], acc, str(new_b))
            print(f"An amount has been withdrawn {a} from account : {acc} and the current balance is:{new_b}")
        else:
            new_b= balance - a
            BankSystem.curr_customer[acc] = str(new_b) # convert it again to string for the csv
            cls.update_acc(BankSystem.curr_customer["id"], acc, str(new_b))
            print(f"you withdraw {a} from {acc} with new balance {new_b} Negative")
        
    @classmethod
    def update_acc(cls,id, column, new_v):
        updated=[]
        for user in BankSystem.accounts:
            if user["id"] == id:
                user[column] = new_v
                # updated overdraft
                user["overdraft_count"] =BankSystem.curr_customer.get("overdraft_count", "0")
                user["active"] = BankSystem.curr_customer.get("active", "True")
            updated.append(user)


        fieldnames = ["id", "first_name", "last_name", "password", "checking", "savings", "active", "overdraft_count"]
        with open("./bank.csv", 'w', newline='') as csvfile:
                    
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(BankSystem.accounts) # updated the values in csv

    @classmethod
    def Deposit(cls):
        if  not BankSystem.curr_customer: # it said its not logged in  
            print(" you must log in first ") 
            return 
        
        acc=input(" from which account you want to make the withdraw (1) savings or (2) checking :").lower()
        if acc not in ["savings", "checking"]:

            return "Error , invalid account"
        
        a=int(input(" type the money amount you want to make the Deposit with : ").strip())
        balance= int(BankSystem.curr_customer[acc])# convert it to int to make calculation
        new_b= balance + a
        BankSystem.curr_customer[acc] = str(new_b) # convert it again to string for the csv
        cls.update_acc(BankSystem.curr_customer["id"], acc, str(new_b))
        print(f"An amount has been Deposit {a} and the current balance is: ${new_b}")

    @classmethod
    def Transfer(cls):
        if  not BankSystem.curr_customer: # it said its not accessd -> add Banksys    
            print(" you must log in first ")
            return 
        print("****Transefer types:****")
        print("(1) from savings account to the checking account")
        print("(2) from checking account to the savings account")
        print("(3) from your account to another customer account")
        
        c = input(" choose the transfer type : 1 or 2 or 3 : ").strip()
        if c not in ["1", "2", "3"]:
            return "Invalid choice "
        
        a=int(input(" type the money amount you want to make the Transfer with : ").strip())
        if a<=0:
            return "Enter a valid amount"
        id = BankSystem.curr_customer["id"]
        if c ==  "1":
            if int(BankSystem.curr_customer["savings"]) >= a :
                
                BankSystem.curr_customer["savings"] =  str(int(BankSystem.curr_customer["savings"] ) - a)
                BankSystem.curr_customer["checking"]  = str(int(BankSystem.curr_customer["checking"] ) + a)
                BankSystem.saving_account()
                print(f"Done Transfering operation with the amount : {a} from savings account to checking account")
                
                # updated the data
                cls.update_acc(id , "savings", BankSystem.curr_customer["savings"])
                cls.update_acc(id , "checking", BankSystem.curr_customer["checking"])
            else:
                 print("not enough balance to transfere")

        elif c ==  "2":
            if int(BankSystem.curr_customer["checking"]) >= a :
                BankSystem.curr_customer["checking"] =  str(int(BankSystem.curr_customer["checking"] )- a)
                BankSystem.curr_customer["savings"]  = str(int(BankSystem.curr_customer["savings"] )+ a)
                print(f"Done Transfering operation with the amount : {a} from checking account to savings account")
                id=BankSystem.curr_customer["id"]
                cls.update_acc(id , "checking", BankSystem.curr_customer["checking"])
                cls.update_acc(id , "savings", BankSystem.curr_customer["savings"])
            else:
                print("not enough balance to transfere")
        elif c =="3":
            ac=input("from which account you want to make the transfere ? savings or checking ").strip()
            if  ac not in ["savings", "checking"]:
                print("Incorrect account ")
                return 
            second_id=input("Enter the id for the user account you want to make the transaction to : ")
            second=False
            updated=[]
            with open("bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    if row["id"] == second_id:
                        second = True 
                        if row[ac] not in [None, "", "False",False ]:
                            row[ac]= str(int(row[ac])+a) # convert it to str
                        else:
                            row[ac] = str(a)
                    updated.append(row)
            if not second:
                return "No User Found"
                            
            BankSystem.curr_customer[ac] =  str(int(BankSystem.curr_customer[ac] )- a)
            cls.update_acc(id , ac, BankSystem.curr_customer[ac])
            
            #updated data
            fieldnames = ["id" , "first_name" ,"last_name" ,"password","checking" , "savings", "active" ,"overdraft_count"]

            with open("./bank.csv", 'w', newline='') as csvfile:
                    
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated) # updated the values in csv
            print(f"Done Transfering ${a} from your account to user account with number {second_id} ")


class overdraftProtection:
    overdraft_fee = 35
    max_withdraw = 100
    max_negative_balance = -100
    max_overdrafts = 2

    def __init__(self, customer):
        self.customer=customer

    # if account is deactivated 
    def withdraw(self, acc_type, a):
        if self.customer.get("active") in ["False", False]:
            print("Your account is deactivated. Please deposit funds to reactivate.")
            return False
        # if it is more than 100 
        if a > self.max_withdraw:
            print(f"Cannot withdraw more than ${self.max_withdraw} at once.")
            return False

        # initialize overdraft_count 
        overdraft_count = int(self.customer.get("overdraft_count", "0") or "0")
        balance = int(self.customer.get(acc_type, "0")) # get account balance first
        new_b = balance - a # updated

        # if it is less than 100 -> denied
        if new_b < self.max_negative_balance:
            print(f"Cannot overdraft because ${self.max_negative_balance} Withdrawal denied.")
            return False
        
        # if account balance -> in negative discount 35 , updated overdraft
        if new_b < 0:
            new_b = new_b - self.overdraft_fee
            overdraft_count += 1
            print(f"Overdraft fee of ${self.overdraft_fee} applied.")
            print(f"Overdraft count: {overdraft_count}")
            self.customer["overdraft_count"] = str(overdraft_count)
            # if its more than 2  draws stop the account
            if overdraft_count >= self.max_overdrafts:
                self.customer["active"] = "False"
                print("Account deactivated due to exceeding overdraft limit.")

        self.customer[acc_type] = str(new_b)
        # print(f"Withdrawal successful. New {acc_type} balance: ${new_b}")
        return True

        
    def deposit(self, acc_type, a):
            # cal new balance
            balance = int(self.customer.get(acc_type, "0"))
            new_b = balance + a
            self.customer[acc_type] = str(new_b)
            print(f"Deposit successful new {acc_type} balance is : {new_b}")
            self.check_reactive()

    
    def check_reactive(self):

        checking=int(self.customer.get("checking", "0"))
        savings =int(self.customer.get("savings", "0"))
        total=checking + savings # calc total of 2 accounts
        #activate again
        if total >= 0 and self.customer.get("active") in ["False", False]:
            self.customer["active"] = "True"
            self.customer["overdraft_count"] = "0"
            print("Account reactivated because of sufficient balance.")


def init():
    print("****Welcome to the ACM bank!!!****")
    # BankSystem.loadAccounts()
    main_menu_choice = None
    main_menu_options = ["1", "2", "3", "q"]
    while not main_menu_choice or  main_menu_choice not in main_menu_options:
        main_menu_choice = input("Would you like to (1)login or (2)create an account? or (3)logout or type 'q' to quit. ").strip()
        print(main_menu_choice)

    if main_menu_choice == "1":
        BankSystem.login()
        if not BankSystem.curr_customer:
            print("login failed")
            return

    if main_menu_choice == "2":
        # print("user choose number 2")
        BankSystem.create_account()
        print(BankSystem.accounts)
        # not working 
    if main_menu_choice == "3":
        # print("user chose number 3")
        BankSystem.logout()
    if main_menu_choice == "q":
        print("Good bye")
        quit()
       



def init2():
     main_menu_choice2 = None
     main_menu2 = ["1", "2", "3", "q", "4", "5"]
     while not main_menu_choice2 or main_menu_choice2 not in main_menu2:
        main_menu_choice2 = input("**what operation Do you want to make ?(1) Withdraw  or (2) Deposit or (3) Transfer (4) log out (5)account Info: ").strip()
        print(main_menu_choice2)

        if main_menu_choice2 == "1":
            operation.Withdraw()
            print("Customer status:", BankSystem.curr_customer)

        if main_menu_choice2 == "2":
            operation.Deposit()
            print("Customer status:", BankSystem.curr_customer)

        if main_menu_choice2 == "3":
           operation.Transfer()  
        
        if main_menu_choice2 == "4":
           BankSystem.logout()  
        
        if main_menu_choice2 == "5":
            c= Customer(
            id=BankSystem.curr_customer["id"],
            first_name=BankSystem.curr_customer["first_name"],
            last_name=BankSystem.curr_customer["last_name"],
            password=BankSystem.curr_customer["password"],
            savings=BankSystem.curr_customer["savings"],
            checking=BankSystem.curr_customer["checking"],
            active=BankSystem.curr_customer["active"],)
            c.info()
         

init()
init2()


             