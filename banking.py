import csv

class Customer:
    def __init__(self, email, first_name,last_name, password, id, checking, saving):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.email = email
        self.password = password
        self.checking = checking 
        self.saving = saving
        
    def create_account(self):
        u = input(" Do you have an account ? answer Y or N ")
        if u == "Y":
            return f" Enter your Email {self.email} and password {self.password} "
        else:
            return f"Enter your first name {self.first_name} and last name {self.last_name} , and your email {self.email} and your password {self.password}"
        

    def checking_account(self):
        if self.checking == True:
            print("Customer has an account")
        else:
            print(" you need to Make a new Account")
    
    def saving_account(self):
        
        if self.saving == True:
            return f" you have a saving account  :{self.id}"
        else:
            return " you don't have saving account"
        
    def both_saving_checking(self):
        if self.checking == True and self.saving == True:
            return " Customer have both checking and saving account" # make sure 1 for each
        elif self.checking == False and self.saving == True:
            return " Customer just have a saving account "
        elif self.checking == True and self.saving == False:
            return "Customer has an account "
        else:
            return "Customer does not have an account "
        
    def login(self):
        if self.create_account  == False : 
           u = input(f"Enter yor email {self.email} and password {self.password} to log in ")
           if u in self.checking_account():
               return " Log in Successfully "
           else:
               return " Try again , Incorrect Email or Password "
    
    def logout(self):
        if self.create_account  ==  True :
            print("log out Successfully ")
            quit()
    

            
print(Customer.create_account())
# print(Customer.saving_account())
# print(Customer.checking_account())

