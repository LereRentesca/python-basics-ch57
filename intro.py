print("Hello World!")
print(2)
print(5+3)

#this is a comment
#print("Hello World!")

#Creating Variables
name = "Giancarlo"
last_name = "Renteria"
age = 41
total = 12.34
found = False
middle_name = 'Esteban'

print(name + " " + middle_name + " " + last_name) #Luis Renteria

#The type() function helps us to know the data type of the variable
print(type(name))
print(type(age))
print(type(found))

#Casting 
#Helps us to convert different data types
#str() 
#int()
second_age = "22"
print("My name is " + name + " and I'm " + str(age) + " years old.") #Luis I'm 21 years old.
print(age - int(second_age))