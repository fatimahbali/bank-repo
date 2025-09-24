import csv
import os



class BankSystem:

    id = '100012'
    password =""
    accounts = []
    curr_customer = None
    checking = None
    saving = None

    def __init__(self):
        pass

# load data from csv file 
    def load_data(self):
        fieldnames = ["id" , "first_name" ,"last_name" ,"password","checking" , "savings", "active" ,"overdraft_count"]
        # if not os.path.exists("./bank.csv"):
        #             with open("./bank.csv", 'w', newline='') as csvfile:
                        
        #                     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #                     writer.writeheader()
        #                     # for row in fieldnames:
        #                     #     writer.writerow(row)
                    
# 4.0 If Exists - ReadFile / Rows:
        try: 
            with open("bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    # print(row, "line 104") # will print dictionary 
                    for prop in fieldnames:
                        pass
                        # print(row[prop], "line 106") # will print the value of each individual property
        except csv.Error as e:
            print(e)

    @classmethod
    def create_account(cls):
            u = input(" Do you want to create an account ? answer Y or N  : ").strip()
            if u == "Y" or  u == "Y".lower() :
                s = input("Do you want a saving account type : saving or checking account type : checking or both :").strip()
                
                with open("bank.csv", "r") as file:
                        contents = csv.DictReader(file)
                        # for row in contents:
                        #     idd=int(row["id"])
                        #     if row["id"].isdigit(): # make sure its number not str
                        #             return idd
                    
                        userId = cls.id
                        cls.id=str(int(cls.id)+1)
                        # print(cls.id)
                        # print(f"user id line51 {cls.id}")
                        # for row in contents:
                            # if row[0] == id and row[3] == password :
                        first_name= input("Enter your first name: ").strip()
                        last_name= input("Enter your last name: ").strip()
                        password = input("Enter your password : ").strip()
                        #checking = 0
                        #savings=0
                        active= True
                        overdraft_count=0 ######## make sure id is save
                        # userId = str(int(max(id))+1) ###### cheak it because its string in csv
                        new_acc = (f" ID: {cls.id} , First name: {first_name}, Last name : {last_name} , password : {password} , is it active ? : {active}, overdraft_count: {overdraft_count}")
                        return cls.accounts.append(new_acc)
                
                

                if s =="SAVING" or s=="Saving".lower():
                    savings = 0
                    checking = None
                    return cls.saving_account() #اعدل الاسم
                    
                  
            
                elif s =="CHECKING" or s =="checking".lower():
                    checking = 0
                    savings = None
                    return cls.checking_account()

                else:
                    checking = 0
                    savings = 0
                    return cls.both_saving_checking()# both saving & checking

                
                    
            else:
                quit()
                 
            
    @classmethod
    def loadAccounts(cls):  ######  
        # from load data load the accounts  
        print("***** Loading the accounts from the csv file *****")
        
        if not os.path.exists("bank.csv"):
            print(" bank.csv does not exist ")

        try: 
            with open("bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    cls.accounts.append(row)
                print(f"the accounts list is : {cls.accounts}")
                return cls.accounts
            
                # print(row[prop], "line 106") # will print the value of each individual property

        except csv.Error as e:
            print("Error loading the accounts : {e}")
      

       

            
        
    @classmethod
    def login(cls):
            print("login function in bank class running!!! line 25")
            user_id = input(f"Enter your ID :").strip()
            password = input(f"Enter your password :").strip()

            # for acct in BankSystem.accounts:
            #     print(acct)
            try:
                with open("bank.csv", "r") as file:
                    contents = csv.DictReader(file)
                    for row in contents:
                        if row["id"] == user_id and row["password"]== password:
                                print(f"Login Successfully !!! welcome {row['first_name']}  {row['last_name']}")
                                cls.curr_customer = row # put the current customer as logged in customer 
                        # else:
                    print("Invalid ID or Password , try again ")
                
            except Exception as e:
                 print(f" error occurred :{e}")

            # if u=="new" or u=="NEW":
            #     return f"Enter your First name {self.first_name} and Last Name : {self.last_name} and password {self.password} "
            # if u=="login" or u=="LOGIN" : 
            #    u = input(f"Enter your id and {self.id} and password {self.password} to log in ")
            # if self.id in csv: 
            #     return " Log in Successfully "
            # else:
            #        return " Try again , Incorrect Name or Password "
    @classmethod
    def logout(cls):
        if cls.curr_customer:
            print(f"{cls.curr_customer['first_name']} {cls.curr_customer['last_name']} has logged out successfully !")
            cls.curr_customer=None # return it to none = empty
        else:
             print(" no user has logged in yet")
    
    @classmethod
    def saving_account(cls):
        if not cls.curr_customer:
            print("you must Log in to access , try again ")
            return
         
        sav = cls.curr_customer
        sav_up=sav.get("saving") # to bring the key saving 

        if sav_up =="False" or sav_up is False:
            print(" you dont have a saving account ")
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
        sav_up=sav.get("saving") # to bring the key saving 

        c = cls.curr_customer
        checking = c.get("checking") # to bring the key checking

        is_checking = checking not in [None , "", False, "False"] # if it has an account not falsy value 
        is_saving=sav_up not in [None , "", False, "False"] # if it has an account not falsy value 

        if is_checking and is_saving :
            print(f" your saving amount is:  ${sav_up} and your checking amount is : ${checking}")
        elif is_checking: # if cheaking == true       
            print(f"you have a checking account with the amount : ${checking}")
        elif is_saving: # if saving == true
             print(f"you have a saving account with the amount : ${sav_up}")
        else:
            print("unfortunately you dont have saving or checking account ")
         
              
    
class Customer:
    def __init__(self, first_name, last_name, password):
        self.first_name=first_name
        self.last_name=last_name
        self.password = password
        self.id = id
        # self.create_account = False # assume its false
        self.active = True

    
    def info(self):
        if self.active == True:
            return f" first name : {self.first_name} last name : {self.last_name} id :{self.id} , your password : {self.password} , your account is active :{self.active}"
        else:
             return f" first name : {self.first_name} last name : {self.last_name} id :{self.id} ,your password : {self.password} , account is not active :{self.active}"
    
class operation:

    @classmethod
    def Withdraw(cls):
        # should login to Withdraw
        if  not BankSystem.curr_customer: # it said its not accessd -> add Banksys    
            print(" you must log in first ")
            return 
        acc=input(" from which account you want to make the withdraw (1) saving or (2) checking :").lower()
        if acc not in ["saving", "checking"]:
            return "Error , invalid account"
        
        a=input(" type the money amount you want to make the withdraw with : ").strip()
        balance= int(BankSystem.curr_customer[acc])# convert it to int to make calculation
        
        if balance >= a: # if account has enough money
            new_b= balance - a
            BankSystem.curr_customer[acc] = str(new_b) # convert it again to string for the csv
            cls.update_acc(BankSystem.curr_customer["id"], acc, new_b)
            print(f"An amount has been withdrawn {a} from account : {acc} and the current balance is:{new_b}")
        else:
            print("not enough money , it will turn it to negative")
        


        # if its have the money to make Withdraw
        #Withdraw from saving 
        # withdraw from checking

    @classmethod
    def update_acc(cls,id, column, new_v):
        updated=[]

        with open("bank.csv", "r") as file:
            contents = csv.DictReader(file)
            for row in contents:
                if row["id"] == id:
                    row[column] = str(new_v) # convert it to str
                    updated.append(row)
        
    # if not os.path.exists("./bank.csv"):        
        fieldnames = ["id" , "first_name" ,"last_name" ,"password","checking" , "savings", "active" ,"overdraft_count"]

        with open("./bank.csv", 'w', newline='') as csvfile:
                    
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated) # updated the values in csv

    def Deposit(cls):
        if  not BankSystem.curr_customer: # it said its not accessd -> add Banksys    
            print(" you must log in first ") # if it not logged in
            return 
        
        acc=input(" from which account you want to make the withdraw (1) saving or (2) checking :").lower()
        if acc not in ["saving", "checking"]:

            return "Error , invalid account"
        
        a=input(" type the money amount you want to make the Deposit with : ").strip()
        balance= int(BankSystem.curr_customer[acc])# convert it to int to make calculation
        new_b= balance + a
        BankSystem.curr_customer[acc] = str(new_b) # convert it again to string for the csv
        print(f"An amount has been Deposit {a} from account : {acc} and the current balance is:{new_b}")

    def Transfer(cls):
        if  not BankSystem.curr_customer: # it said its not accessd -> add Banksys    
            print(" you must log in first ")
            return 
        print("****Transefer types:****")
        print("(1) from saving account to the checking account")
        print("(2) from checking account to the saving account")
        print("(3) from your account to another customer account")
        
        c = input(" choose the transfer type : 1 or 2 or 3 : ").strip()
        if c not in ["1", "2", "3"]:
            return "Invalid choice "
        
        a=input(" type the money amount you want to make the Transfer with : ").strip()
        if a<=0:
            return "Enter a valid amount"
        
        if c ==  "1":
            if int(BankSystem.curr_customer["saving"]) >= a :
                BankSystem.curr_customer["saving"] =  str(int(BankSystem.curr_customer["saving"] )- a)
                BankSystem.curr_customer["checking"]  = str(int(BankSystem.curr_customer["checking"] )+ a)
                print(f"Done Transfering operation with the amount : {a} from saving account to checking account")
                
                # updated the data
                cls.update_acc(id , "saving", BankSystem.curr_customer["saving"])
                cls.update_acc(id , "checking", BankSystem.curr_customer["checking"])
            else:
                 print("not enough balance to transfere")

        elif c ==  "2":
            if int(BankSystem.curr_customer["checking"]) >= a :
                BankSystem.curr_customer["checking"] =  str(int(BankSystem.curr_customer["checking"] )- a)
                BankSystem.curr_customer["saving"]  = str(int(BankSystem.curr_customer["saving"] )+ a)
                print(f"Done Transfering operation with the amount : {a} from checking account to saving account")
                
                cls.update_acc(id , "checking", BankSystem.curr_customer["checking"])
                cls.update_acc(id , "saving", BankSystem.curr_customer["saving"])
            else:
                print("not enough balance to transfere")
        elif c =="3":
            ac=input("from which account you want to make the transfere ? saving or checking ").strip()
            if  ac not in ["saving", "checking"]:
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
                        row[ac] = str(int(row[ac])) # convert it to str
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
            print(f"Done Transfering {a} from your account to user account with number {second_id} ")




# class checking_account(BankSystem):
#     def __init__(self):
#         super().__init__(id, self.password)
#         self.checking=False

    
#     def checking_account(self):

#         if self.id and self.password in csv : # check if id and password match 
#             return f"Customer has an account id :{self.id} , and your checking is :{self.checking}"
#         elif self.checking == False:
#             return " you don't have a checking account "
#         elif type(self.checking) == str:
#                 self.checking = int(self.checking)
#                 return self.checking
#         else:
#             print(" you dont have a checking account , you need to Make a new Account")
    



# class saving_acccount(BankSystem):
#     def __init__(self):
#         super().__init__(id, self.password)
#         self.saving=False

#     def saving_account(self):
        
#         if self.id and self.password in csv : # in csv
#             return f" you have a saving account  :{self.id} and your saving is : {self.saving}"
#         elif self.saving==False:
#             return "you dont have a saving account"
#         elif type(self.saving) == str:
#                 self.saving = int(self.saving)
#                 return self.saving
#         else:
#             return " you don't have saving account"
        
        

def init():
    print("****Hi! Welcome to the ACM bank!!!****")
    # BankSystem.loadAccounts()
    BankSystem()
    main_menu_choice = None
    main_menu_options = ["1", "2", "3", "q"]
    while not main_menu_choice or  main_menu_choice not in main_menu_options:
        main_menu_choice = input("Would you like to (1) login or (2) create an account? or (3) to logout or type 'q' to quit. ")
        print(main_menu_choice)

    if main_menu_choice == "1":
        BankSystem.login()
    if main_menu_choice == "2":
        # print("user chose number 2")
        BankSystem.create_account()
        print(BankSystem.accounts)
        # not working 
    if main_menu_choice == "3":
        print("user chose number 3")
        BankSystem.logout()


def init2():
     main_menu_choice2 = None
     main_menu2 = ["1", "2", "3", "q"]
     while not main_menu_choice2 or main_menu_choice2 not in main_menu2:
        main_menu_choice2 = input(" Hi ! what operation Do you want to make ?  (1) Withdraw  or (2) Deposit or (3) Transfer ")
        print(main_menu_choice2)

        if main_menu_choice2 == "1":
            operation.Withdraw()
        if main_menu_choice2 == "2":
             operation.Deposit()
        if main_menu_choice2 == "3":
            pass           
         

init()
init2()

             