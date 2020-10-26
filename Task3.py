# Exercise 1
A=[1,2,3,"Ankit",6J,7,8,9,10,2.3u]
print(A)

#Exercise 2
A=[1, 2, 3, 4, 5]
print(A[:])
print(A[1:3])
print(A[1:])
print(A[::3])

# Exercise 3
sum = 0
multiply=1
A=[10,20,30,40,70,80,90,112,334,556,897]
for i in range(len(A)):
    sum+=A[i]
    multiply=multiply*A[i]

print(sum)
print(multiply)


#Exercise 4
A=[10,30,50,67,2,67,12,54,5,7,89]
print(max(A))
print(min(A))


# Exercise 5
A= [12,5,34,6,75,9,66,73]
B=[i for i in A if i%2!=0]
print(B)


# Exercise 6
A=[]
for i in range(1,31):
  A.append(i*i)
print(A[:5])
print(A[-5:])


# Exercise 7
A=[1,3,5,7,9,10]
B=[2,4,6,8]
A[-1:]=B
print(A)



#Exercise 8
A={1:10, 2:20}
B={3:30, 4:40}
A.update(B)
print(A)


# Exercise 9
A={}
for i in range(1,6):
    A[i]=i*i

print(A)


# Exercise 10
x=input("enter the no:")
print(x)
list1=x.split(" ")
print(list1)
print(tuple(list1))

#Exercise 13
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
print(x[::-1])
print(x[5][5][0])


# Exercise 14
X=range(0,1000)
Y=Xrange(10000)

# Exercise 16
for i in range(1,101):
if i%2==0 and i%3==0:
print(i)


# Exercise 17
string_val=input("Enter a string:")
string_rev=string_val[::-1]
for letter in string_rev:
if letter in 'aeiou':
print(letter)
print("index is",string_rev.index(letter))

# Exercise 18
string_it="hello my name is abcde"
list_words=[i for i in string_it.split()]
print(list_words)
list_evenlen=[i for i in list_words if len(i)%2==0]
print(list_evenlen)

# Exercise 19
x=[1,2,3,4,5,6,7,8,9,-1]
y=[]
for i in x:
for T in x:
if i+T==8:
print(i,T)


# Exercise 20
even_list=[]
odd_list=[]
while True:
number=int(input("enter the no in range of 1-50"))
if number%2==0:
even_list.append(number)
if len(even_list)==5:
break
else:
odd_list.append(number)
if len(odd_list)==5:
break
 
print(even_list)
print("Sum of even list is", sum(even_list))
print("Max o list is", max(even_list))

print(odd_list)
print("Sume of odd list is", sum(odd_list))
print("Max o list is", max(odd_list))


# Exercise 21
string_ex="12abcbacbaba344ab"
string_result = ''.join([i for i in string_ex if not i.isdigit()])

print(string_result)
all_freq = {} 

  
for i in string_result: 
if i in all_freq: 
all_freq[i] += 1
else: 
all_freq[i] = 1
print(str(all_freq))


# Exercise 22
A= (1,2,3,4,5,6,7,8,9,10)
B=[]
for i in A:
if i%2==0:
B.append(i)

C=tuple(B)
print(C)










