#Purpose: Lab 12
#   Program Name:Object-Oriented Bank Account Program
#   Exercise:
#  1.	Complete the code for each of the functions in the BankAccount class and place this class inside its own module.
#  2.	Create a presentation tier module (in which will be your main function) and import the business tier module BankAccount class into it
#
#   Author: Kiara Lindsey
#   Date: December  2020

class BankAccount:
   def__init__(self,pin,balance):
        self.pin = pin
        self.balance =0
   def deposit(self,amount):
       self.amount = amount
       self.balance = input(self.balance +self.amount)
   def withdraw(self, amount):
       self.amount = amount
       if self.amount >self.balance):
           print("Insufficient Funds")
       else:
           self.balance = self.balance -self.amount
   def get_balance(self,pin):
       print("Account balance is: ",self.balance)
   def change_pin(self,oldpin,newpin):
        if oldpin = self.oldpin
            print("Enter new pin: ")
        else:
            self.newpin ="24681"
