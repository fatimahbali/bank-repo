import unittest
from banking import BankSystem

class Test(unittest.TestCase):
    
    def setUp(self):

        BankSystem.accounts=[] # empty list
        BankSystem.curr_customer=None

        test_cus={
                "id":"100014",
                "first_name":"Amirah",
                "last_name":"All",
                "password":"a123",
                "checking":"False",
                "savings":"100",
                "active":"True",
                "overdraft_count":"1"
        } 
        #add accounts
        BankSystem.accounts.append(test_cus.copy())
        BankSystem.curr_customer =test_cus.copy()
       
    
    def test_create(self):
        self.assertIsNotNone(BankSystem.curr_customer)
        self.assertEqual(BankSystem.curr_customer["first_name"], "Amirah")
        


    def test_login(self):
        BankSystem.curr_customer=None
        f=False
        

        for a in BankSystem.accounts:
            if a["id"] == "100014" and a["password"] =="a123":
                f=True
        self.assertTrue(f, "Login should succeed with correct id and password")

    
    def test_deposit(self): 
        
        self.assertIsNotNone(BankSystem.curr_customer)
        ac_type= "savings"
        deposit_amount = 150
        
        balance=int(BankSystem.curr_customer[ac_type])
        n_balance= balance+deposit_amount

        BankSystem.curr_customer[ac_type] = str(n_balance)
        print(f" Befor deposit:{balance} , after deposit: {n_balance}")
        self.assertEqual(BankSystem.curr_customer[ac_type], str(n_balance))

if __name__ == "__main__":
    unittest.main()

