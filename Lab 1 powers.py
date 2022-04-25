#Kiara Lindsey
#08/30/20
#Table of Powers - Calculates a number squared or cubed
#display title
print ("Table of Powers")
print ('\n')
#Allow input
start_x = int(input("Start Number: "))
stop_x = int(input("Stop Number:  "))
x = start_x
print('\n')
# Error message for start integer that's larger than the stop integer
while start_x > stop_x:
    print ("Start integer must be less than stop integer.")
    start_x = int(input("Enter a lower integer: ")) #gives user a chance to enter lower integer
#formatting  for columns use \t for spacing
print("Number \t\t\t","Squared\t\t\t", "Cubed") #headings
print("====== \t\t\t","====== \t\t\t", "======")
 #for loop(s) for calculating squared and cubed values
for x in  range (int(start_x)):
  squared= print(x ** 2)
for x in range (int(start_x)):
 cubed=print(x ** 3)
for x in  range (int(stop_x)):   #formatting the values kept brionging up errors
  squared= print(x ** 2)
for x in range (int(stop_x)):
 cubed=print(x**3)
