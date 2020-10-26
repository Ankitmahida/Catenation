# Exercise 1
class calculate():
def __init__(self,C,H):
self.C=C
self.H=H
def formula(self,D):
return ((2*self.C*D)/self.H)**2
D=int(input("Enter the value of D"))
obj1=calculate(50,30)
Q = obj1.formula(D)
print(Q)


# Exercise 2
class Shape(object):
def __init__(self):
pass
def area(self):
 return 0

class Square(Shape):
def __init__(self, l):
Shape.__init__(self)
self.length = l

def area(self):
return self.length*self.length

Square= Square(3)
print (Square.area())

#Exercise 3
class calculate:
def threeSum(self, input_num):
input_num, result, i = sorted(input_num), [], 0
while i < len(input_num) - 2:
a, b = i + 1, len(input_num) - 1
while a < b:
if input_num[i] + input_num[a] + input_num[b] < 0:
a += 1
elif input_num[i] + input_num[a] + input_num[b] > 0:
b -= 1
else:
result.append([input_num[i], input_num[a], input_num[b]])
a, b = a + 1, b - 1
while a < b and input_num[a] == input_num[a - 1]:
a += 1
while j < k and input_num[b] == input_num[b + 1]:
b -= 1
i += 1
 while i < len(input_num) - 2 and input_num[i] == input_num[i - 1]:
i += 1
return result

print(calculate().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


# Exercise 4
    # output 1
    Output-File "/Users/gaurihatode/reverse_word.py", line 10, in <module>
    main()
  File "/Users/gaurihatode/reverse_word.py", line 9, in main
    print(b.x,b.y)
AttributeError: 'Derived_Test' object has no attribute 'x'
Reason- class Derived_Test doesn not have variable x defined in it. 
To use the oject of Class test the Derived_Test class should have Test.__init__(self).

    #output 2
    Output-File "/Users/gaurihatode/reverse_word.py", line 11
    main())
          ^
SyntaxError: unmatched ')'
Reason- extra paranthese at the calling of main function

    #Output 3
    Output-File "/Users/gaurihatode/reverse_word.py", line 6, in <module>
    class B(A):
  File "/Users/gaurihatode/reverse_word.py", line 16, in B
    main()
  File "/Users/gaurihatode/reverse_word.py", line 13, in main
    obj = B()
NameError: name 'B' is not defined
Reason- The class objects are defined at the class level no inside a method.

    #output 4
    Output-30


# Exercise 5
def get_sec(time_str):
    
    a, b, c = time_str.split(':')
    return int(a) * 3600 + int(b) * 60 + int(c)


print(get_sec('1:50:00'))
print(get_sec('1:20:00'))
print(get_sec('4:10:00'))


# Exercise 6
import math
class Person:
def _init_(self, initialAge):
if (initialAge < 0):
print('Age is not valid, setting age to 0')
self.age=0
else:
self.age=initialAge
def amIold(self):
if(self.age < 13):
print("You are young")
elif (self.age >=13 and self.age < 18):
print("You are a teenager")
else:
print('You are old')
def yearpasses(self):
self.age +=1

t = int(input("input your age   "))
for i in range(0,t):
age=int(input())
p=Person(age)
p.amIold()
for j in range(0,3):
p.yearpasses()
p.amIold()
print("")