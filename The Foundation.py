
#Challenge 1: Grocery Run

budget = 200
rice = 25
chicken = 40
bread = 8
milk = 6

total = rice + chicken + bread + milk
change = budget - total 

print (f" Budget: ${budget}")
print (f"Total: ${total}")
print (f"Change: ${change}")





#Challenge 2 Gym Mempership


fee = 50
budget = 320

mounths = budget // fee
remaining = fee % budget

print(f"Mounths: ${mounths}")
print(f" Remaining: ${remaining}")



#Challenge 3 Flight booking

flight = 500
fee = flight * .10
total = flight + fee

print (f"Fligh: ${flight}")
print (f"Fee: ${fee}")
print (f"Total: ${total}")


#Challenge 4 : Greeting Card


name = input("what is your name ?")
friend_name = input("what is your friend name ?")
massage = input ("Wishing you the best!")

print (f"To: {name} , From: {friend_name.upper()} , massage: {massage}")



#Challenge 5 : Name Tag


name = input ("What is your name ?")

print ("upper", name.upper())
print ("lower", name.lower())
print ("letters" , len(name.replace(" " )))
print ("first"، name [0])
print ("last", name[-1])




#Challenge 6: Pizza Split

total_bill = 85
friends= 6

each_pays = tota_bill / friends

print (f" total_bill : {total_bill}")
print (f" friends : {friends}")
print (f" each_pays : ${round(each_pays, 2)}")


#Natiijada 
total_bill : 85
friends : 6
Each_pays : 14.17




#Challenge 7: Username Generator


name= input ("what is your name ?")
birth_year = input ("what is your birth year ?")

user_name = name[:4].lower() + birth_year
print (f"username is : {user_name}")





#Challenge 8: Coffee Receipt


name= input("what is your name ?")
coffees = int(input("how many coffees do you want ?"))

coffee_price = 5
total = coffees * coffee_price

print(f" Customer : {name.upper()}")
print(f" Coffees : {coffees}")
print (f" Total : {total} ")




## Challenge 9: Contact Card

name= input (" what is your name ?")
phone_number = input (" what is your phone number ?")
email = input ("what is your email ?")

len(email)

print(f" Name : {name.capitalize()} ")
print(f" hone Number : {phone_number} ")
print(f" Email : {email} , {len(email)}")





# Challenge 10: Travel Profile

name = input ("what is your name ?")
destination = input ("where is your destination")
days = input ("How many days is your trip?")

note = f" Have A safe trip {name}, Enyoy your {days} days in {destination}"

print f" Traverel : {name}" 
print f"Destination : {destination}"
print f"Days : {days}"
