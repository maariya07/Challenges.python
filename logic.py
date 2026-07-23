# Challenge 1: Can You Vote?

age = int (input("How old are you "))
if ( age >= 18 ):
    print (f"You Can Vote ")
else:
   years_left = 18 - age 
   print (f" You can't vote yet.{years_left} More years ")

# Challenge 2: Ticket Price

age = int(input(" How old are you.?"))
print (f"age: {age}")

if age < 12:
    print (f"Ticket: $5")
    
elif 12 <= age <=17:
    print ("Ticket: $8")
    
else:
    print("Ticket: $12")



# Challenge 3: Parking Fee

hours= int (input("How many hours did they park?"))
print(f"Hours: {hours}")

if hours < 2:
    print (f" Fee: $5")
   
elif 2 <= hours <= 3:
    print(f"Fee: $10")
    
else:
    print(f"Fee: $20")


# Challenge 4: Speed Check

speed_limit = int(input(" What is your speed limit.?"))
print (f"Speed Limit: {speed_limit}")

your_speed = int(input("What is your speed .?"))
print (f" Your Speed: {your_speed}")


if your_speed > speed_limit:
   over_by = your_speed - speed_limit
   print(f"Over by: {over_by}km/h")
   fine = (over_by // 10)*50
   print(f" Fine: ${fine}")
   
else:
    print(" No Fine")

# Challenge 5: Countdown

number= int(input("Enter Number"))
count = number
while count > 0:

    print (count)
    count = count -1
print ("Go!")


# Challenge 6: Grade Checker

score = int(input("Enter Your Score"))
print (f"Score: {score}")

if score >= 90:
   print ("Grade: A")
   
elif 80 <= score <=89:
    print ("Grade: B")
    
elif 70 <= score <= 79:
    print ("Grade: C")
   
elif 60 <= score <= 69:
    print("Grade: D")
    
else:
    print ("Grade:F")


# Challenge 7: Even or Odd

number= int (input(" Enter a Number"))
print (f" Number {number}")

if number % 2==0:
    print (f"{number} Is Even")
    print ("Even Numbers:")
else:
    print (f"{number} Is odd")
    
    
for i in range (2, number +1,2):
    print (i)


# Challenge 8: Discount Day

day= input("What day of the week is it.?")
print (f" {day} ")
price = int (input(" What is the price"))
print (f"${price}")


if day == "Monday" or day == "Friday":
    discount = price * 0.20
    final = price - discount
    print (f" Discount : 20% ")
    print (f" Final: {final}")
    
    
elif day == "Wednesday":
    discount = price * 0.10
    final = price - discount
    print (f"Discount: 10%")
    print (f"Final: {final} ")
    
    
else:
    final = price
    print (f" discount: 0%")
    print (f" Final: {final}")

# Challenge 9: Star Printer

number = int (input(" Enter a Number"))
print ("*" * number)


# Challenge 10: Flight Check-in

passenger_name = input(" Enter Your Name.")
age = int(input(" Enter Your age. "))
bag_weight = int (input(" Enter Your Bag weight."))

print (f" Passener: {passenger_name.upper()}")

if age >= 18 and bag_weight < 23:
  print("BOARDING PASS")
  print(f"Status: Status:Checked in")
  
elif age < 18 and bag_weight <23:
    print ("Age rule failed.")
    
elif age >= 18 and bag_weight >= 23:
    print ("Bag weight rule failed.")
    
    
else:
     print("Age rule failed.")
     print ("Bag weight rule failed.")
