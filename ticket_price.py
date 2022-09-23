height = int(input("What is your height in centimeters? "))

if height >= 120:
  print("You can ride the rollercoaster.")
  age = int(input("What is your current age? "))
  if age <12:
    print("Your price is $5 for a ticket.")
  elif age >= 18:
    print("Your price is $12 for a ticket.")
  else:
    print("Your price is $7 for a ticket.")
else:
  print("Sorry. You need to grow a little more before riding.")