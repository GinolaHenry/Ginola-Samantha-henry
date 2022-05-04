#Author:Ginola Henry
#Date Created: 05/1/2022
#Course: ITT103
#Purpose: To calculate the sales commission base on the class.

def findprocessCommission():
  def Commission ():
    global commission
    commission = float (Sales_amt * Comm_rate)

  global Sales_amt, Sales_per_num, Class_num, Comm_rate
  Sales_per_num = int(input("Please enter the Sales person number"))
  Class_num = int(input ("Please enter the class number to which the sales person belongs"))
  Sales_amt = float(input ("Please enter their Sales amount"))

  if Class_num == 1:
    if Sales_amt < 1000 or Sales_amt == 1000:
      Comm_rate=float(0.06)
      Commission()
      print ("Sales Person number", Sales_per_num,"of class", Class_num, "have received a sales commission of", commission, "Congrats","!")        
    elif Sales_amt> 1000 and Sales_amt < 2000:
        Comm_rate=float(0.07)
        Commission()
        print ("Sales Person number", Sales_per_num, "of class", Class_num, "have received a sales commission of", commission, "Congrats","!")
    elif Sales_amt >2000 or Sales_amt == 2000:
          Comm_rate=float(0.1)
          Commission()
          print ("Sales Person number", Sales_per_num, "of class", Class_num, "have received a sales commission of", commission, "Congrats","!")

  if Class_num == 2:
    if Sales_amt < 1000:
      Comm_rate=float(0.04)
      Commission()
      print ("Sales Person number", Sales_per_num, "of class", Class_num, "have received a sales commission of", commission, "Congrats","!")
    elif Sales_amt == 1000 or Sales_amt > 1000:
        Comm_rate=float(0.06)
        Commission()
        print ("Sales Person number", Sales_per_num,"of class", Class_num, "have received a sales commission of", commission, "Congrats","!")

  if Class_num == 3:
    Comm_rate=float(45/100)
    Commission()
    print ("Sales Person number", Sales_per_num,"of class", Class_num, "have received a sales commission of", commission, "Congrats","!")
  elif Class_num <1 or Class_num>3: 
    print ("I am sorry, the number you have entered is not recognised,  please enter a valid number between 1 and 3, try again.")

count=int(2)
while count == 2:
  findprocessCommission()
  count=int(input("If you want to calculate another commission then please enter the number 2. Any other number will end the program."))