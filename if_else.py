print(3+2) #5
print(10-3) #7
print(5*3) #15
print(10/2) #5

x = 10
y = 3
print(x+y)
print(x*y)

age = 22
#If-else statements 
#Execute some instructions if the condition it's correct
#We can catch with an else in case that the condition doesn't match
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Greater than: a > b
# Less than or equal to: a <= b
# Greater than or equal to: a >= b
if age < 100:
    if age < 21:
        print(f"You're a minor.")
    else:
        print(f"Don't worry you're super young!")
elif age == 100:
    print(f"Congratulations, you got to live a century!")
else:
    print(f"Sorry, you're getting old.")

#Exercise
x = 5
y = 8
if x > y:
    print("Hello")
elif x == 10:
    print("World")
else:
    print("Welcome")

x = "Hello"
y = "hello"

if x == y:
    print("Hey it's the same word")
else:
    print("They're different!")