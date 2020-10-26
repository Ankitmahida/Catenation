# Exercise 1
try:
name = 'Ankit'
except:
print("Try again")

# Exercise 2
while True:
try:
Email = input("Enter the Email: ")
s=open(Email, 'r')
print(s.read())
break
except:
print('File Email is incorrect')

# Exercise 3
while True:
try:
x =input("Please enter an integer: ")
if len(x)>4 or len(x)<4:
raise ValueError
except:
print("Please length is too short/logn!!! Please provide only four digits")
else:
print("Number is accepted")

# Exercise 4
print('Enter correct userEmail and Password')
count=0
while count < 3:
username = input('Enter username: ')
password = input('Enter password: ')
if password=='A12345' and username=='A@gmail.com':
print('Access granted')
break
else:
print("Retype youe username or password")
count += 1
        
print("Exceed the limits")
        
# Exercise 6
x=open("demo.txt", "r", encoding="cp1252")
z=x.read()
words=z.split()
for i in words:
    if len(i) % 2 == 0:
        print(i)
