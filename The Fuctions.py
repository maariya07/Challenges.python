# Challenge 1: Say Hello


 def say_hello():
    print ("hello world")


say_hello()
say_hello()
say_hello()



# Challenge 2: Welcome Message

 def welcome(name):
    print ("welcome to bashi Acedemy ," , name)


welcome("Ahmed!")
welcome("Hodan!")
welcome("Farah!")

# Challenge 3: Full Name

def full_name(first,last):
   print(first.upper() , last.upper())
   
   
   
full_name(first = "Ahmed" , last = "Yusuf")
full_name(first= "Hodan" , last = "Bile")
ful_name (first= "Nimo" , ast = " Farah")


# Challenge 4: Double It

def double(number):
   return number * 2
   
   
result1 = double(5)
print (result1)
result2 = double(10)
print (result2)
result3 = double(25)
print (result3)

# Challenge 5: Ticket Price

def ticket_price(age):

   if age < 12:
       price = 5
       return price 
   
   
   elif 12 <= age <= 17:
       price = 8
       return price
    
    
   elif age >= 18:
       price = 12 
       return price
    
    
   
    
result1 = ticket_price(10)
print (f"Age 10:$ {result1}")

result2 = ticket_price(15)
print (f" Age 15: ${result2}")

result3 = ticket_price(25)
print (f" Age 25: ${result3}")


# Challenge 6: Area Calculator

def area(length,width):
    area= length * width
    return area
    
    
result1 = area(5,4)
print (f" Room 1: {result1}")
result2 = area (10,3)
print (f" Room 2: {result2}")
