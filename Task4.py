# Exercise 1
def string_reverse(str1):
rstr2 = ''
index = len(str1)
while index > 0:
rstr1 += str1[ index - 1 ]
index = index - 1
return rstr2
print(string_reverse('1234abcd'))

# Exercise 2
def count_case(A):
lower=0
Upper=0
for i in s:
if ( i.islower() ):
lower += 1
else:
Upper += 1
print("No. of lower case characters:", lower)
print("No. of Upper case characters:", Upper)


s = input("enter the string:")
count_case(A)

# Exercise 3
def unique_element(e):
x = []
for i in e:
if i not in x:
x.append(i)
return x

print(unique_element([5,5,6,7,8,8,9,9,10]))

# Exercise 4
def sort_list(A):
items= [n for n in h.split('-')]
items.sort()
print('-'.join(items))

A = input("enter hyphen seaparated values:")
sort_list(h)

# Exercise 5
def capital(x,y):
x=x.upper()
print(x)

y=y.upper()
print(y)

capital("hello world","practice makes perfect")

# Exercise 6
def calculate_sum(x,y) :
A = int(x) + int(y)
print(A)


J = input("enter num1: ")
K = input("enter num2: ")

calculate_sum(J, K)


# Exercise 7
def compare_strings_len(x,y):
if len(x) != len(y):
A= max(x, y, key=len)
print("The max lenght string is  ", A)
elif len(x) == len(y):
print(x)
print(y)

compare_strings_len("Today is Thursday","Tommorow is Friday")

# Exercise 8
def square_num(M):
for i in range(1, 20):
i = i**2
M.append(i)
print(tuple(M))

M=[]
square_num(M)

# Exercise 9
def show_Numbers(limit):
for i in range(0, limit):
if i % 2 == 0 :
print(i, "EVEN")
elif i % 2 != 0:
print(i, "ODD")
        
limit =int(input("Limit is:"))
show_Numbers(limit)  

# Exercise 10
i = range(1,21)
a = list(filter(lambda x: a % 2 == 0, i))
print(a)


# Exercise 11
a=[]
a = [i for i in range(1,11)]

square_even = list(map(lambda i: i**2, (filter(lambda i: i%2==0, a ))))
print(square_even)

# Exercise 12
try:
x=5/0
print(x)

except:
print("Can not compute")


# Exercise 13
from functools import reduce

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
add = lambda x, y: x+y
newlist = reduce(add, lists)

print(newlist)

# Exercise 14
def foo():
try:
return 1
finally:
return 2

k = foo()
print(k)


# Output:2
def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')

a()
