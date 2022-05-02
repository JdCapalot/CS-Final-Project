Shirts = ['Long sleeve', 'short sleeve', 'Dress shirts']
Pants = ['Shorts', 'Jeans', 'Sweats']
Hats = ['Fitted caps', 'Beanie', 'Baseball caps', 'Top hats']

print ("Hello! Welcome to our store, what would you like to buy today?")
print ("Here are the options:")
print ("1. Shirts for 15 dollars")
print ("2. Pants for 20 dollars")
print ("3. Hats for 10 dollars")

choose = input("> ")

if choose == '1':
   print("Choose from", ", ".join(Shirts) + "." "Type Long, Short or Dress.")
   Long = 15
   Short = 15
   Dress = 15
selection = input("> ")
if selection == "Long":
   print(" How Many?")
   Quantity = int(input( ))
   print( "You Owe", Long* Quantity ,"Dollars")

if selection == "Short":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Short * Quantity, "Dollars")
if selection == "Long":
   print(" How Many?")
   Quantity = int(input( ))
   print( "You Owe", Dress * Quantity,"Dollars")

if choose == '2':
   print("Choose from", ", ".join(Pants) + "." "Type Shorts, Jeans,or Sweats")
   Shorts = 20
   Jeans = 20
   Sweats = 20
selection = input("> ")
if selection == "Shorts":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Shorts * Quantity, "Dollars")

if selection == "Jeans":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Jeans * Quantity, "Dollars")

if selection == "Sweats":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Sweats * Quantity, "Dollars")

if choose == '3':
   print("Choose from", ", ".join(Hats) + "." "Type Fitted, Beanie, Baseball or Top")
   Fitted = 10
   Beanie = 10
   Baseball = 10
   Top = 10
selection = input("> ")
if selection == "Fitted":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Fitted * Quantity, "Dollars")

if selection == "Beanie":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Beanie * Quantity, "Dollars")

if selection == "Baseball":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Baseball * Quantity, "Dollars")

if selection == "Top":
   print(" How Many?")
   Quantity = int(input())
   print("You Owe", Top * Quantity, "Dollars")

else:
   print ("Thank you for shopping :) ")
