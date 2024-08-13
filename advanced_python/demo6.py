


class Account:
    bank_name = 'SBI'
    def set_value(self,account,number,balance):
        self.acc_name = account
        self.acc_number = number
        self.balance = balance
    def choose(self):
        self.choice = int(input('1.withdraw\n2.deposit\nEnter a choice:'))
        if(self.choice == 1):
            self.withdraw = int(input("enter the amount to withdraw"))
        if(self.choice == 2):
            self.deposit = int(input("enter the amount to deposit"))

    def withdraw_balance(self):
        if(self.withdraw<self.balance):
            self.balance -= self.withdraw
            print("Your account ",Account.bank_name,self.acc_number,"is debited Rs ",
                  self.withdraw,"and new balance is ",self.balance)
        else:
            print("Insufficient Balance")
    def deposit_balance(self):
        self.balance += self.deposit
        print("Your account ",Account.bank_name,self.acc_number,"is credited Rs ",
              self.deposit,"and new balance is ",self.balance)

object1 = Account()
object1.set_value('arya',1234,1000)
object1.choose()
if(object1.choice==1):
    object1.withdraw_balance()
if(object1.choice==2):
    object1.deposit_balance()
