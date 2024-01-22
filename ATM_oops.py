print("    <-:Welcome TO ATM :->")
class Atm:
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    print("""
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)
    user_input=input("    Choose Your Option:->")
    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('    Enter your pin :->')
    self.pin = user_pin
    user_balance = int(input("    Enter Your balance :->"))
    self.balance = user_balance
    print('    Pin created successfully')
    self.menu()

  def change_pin(self):
    old_pin = input('    Enter old pin :->')
    if old_pin == self.pin:
      new_pin = input('    Enter new pin :->')
      self.pin = new_pin
      print('    Pin change successful')
      self.menu()
    else:
      print('    You Pin is Invalid')
      self.menu()

  def check_balance(self):
    user_pin = input("    Enter your pin :->")
    if user_pin == self.pin:
      print('    Your balance is ',self.balance)
      self.menu()
    else:
      print('    Your Pin is Invalid')
      self.menu()

  def withdraw(self):
    user_pin = input("    Enter your pin :->")
    if user_pin == self.pin:
      amount = int(input("    Enter your amount :->"))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('    withdrawl successful.balance is',self.balance)
      else:
        print('    Your Account have less amount')
    else:
      print('    Your Pin is Invalid')
    self.menu()
obj=Atm()
obj.balance()
obj.change_pin()
obj.check_balance()
obj.create_pin()
obj.withdraw()





 

 









