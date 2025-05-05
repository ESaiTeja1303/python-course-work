data={
    1:{"username":"Sai Teja","password":"Teja123@","balance":50000,"transactions":[]},
    2:{"username":"Suresh","password":"Suresh123@","balance":20000,"transactions":[]},
    3:{"username":"Akash","password":"Akash123@","balance":40000,"transactions":[]},
    4:{"username":"Teddy","password":"Teddy123@","balance":150000,"transactions":[]},
    5:{"username":"Jack","password":"Jack123@","balance":0,"transactions":[]},
}



class ATM:
    loginstatus=False
    def __init__(self,name,pwd):
        for i in data.keys():
            if data[i]["username"]==name and data[i]["password"]==pwd:
                self.name=name
                self.__pwd=pwd
                ATM.loginstatus=True
                self.id=i
                print(f"Hello {self.name} Login Successful!!")
                break
        else:
            print("Incorrect username or Password,try again!")
    
    def check_balance(self):
        if ATM.loginstatus:
            print(f"\nHello {self.name}, \nAccount Balance: {data[self.id]["balance"]}")
        else:
            print("\nSession expired, login again!")
    
    def deposit(self,damt):
        if ATM.loginstatus:
            data[self.id]["balance"]+=damt
            print(f'\nHello {self.name},\n+{damt} deposited successfully')
            transaction=f'+{damt} deposited successfully'
            data[self.id]["transactions"].append(transaction)
        else:
            print("\nSession expired, login again!")

    def withdraw(self,wamt):
        if ATM.loginstatus:
            if wamt<=data[self.id]['balance']:
                data[self.id]["balance"]-=wamt
                print(f'\nHello {self.name},\n -{wamt} withdrawn successfully')
                transaction=f'-{wamt} withdrawn successfully'
                data[self.id]["transactions"].append(transaction)
            else:
                print(f'Hello {self.name}\nInsuffient balance')
        else:
            print("\nSession expired, login again!")

    def transactions(self):
        if ATM.loginstatus:
            if data[self.id]["transactions"]:
                print(f'========================Transaction History========================')
                for i in data[self.id]["transactions"]:
                    print(i)
                print(f'============================End====================================')
            else:
                print("No Transactions")
        else:
            print("\nSession expired, login again!")

u1=ATM("Sai Teja","Teja123@")
u1.check_balance()

u1.deposit(5000)

u1.check_balance()

u1.withdraw(10000)

u1.check_balance()

u1.transactions()


u2=ATM("Akash","Akash123@")
u2.transactions()
u2.check_balance()
u2.deposit(100)
u2.check_balance()
u2.transactions()


u3=ATM("Jack","Jack123@")
u3.withdraw(10)


        
