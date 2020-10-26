# Exercise 1
x=[3,6,7,14,21,28]
y=[i for i in x if i % 3 != 0 and i % 7 == 0]
print(y)

# Exercise 2
lista=[2,4,6,8,10,12,14]
listb=list(map(lambda x: x*x, lista))
print(listb)

# Exercise 3
x="Hello tO the World"
uppercase=[char for char in x if char.isupper()]
print(uppercase)

# Exercise 4
student=['smith','Jaya','Rayyan']
capital=['CSE','Networking','Operating System']
dict1=dict(zip(student,capital))
print(dict1)


# Exercise 6
def reverse(s): 
str = "" 
for i in s: 
str = i + str
return str

s="Consultadd Training"
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s))

# Exercise 7
def uppercase_decorator(function):
def wrapper():
func = function()
make_uppercase = func.upper()
return make_uppercase
return wrapper
