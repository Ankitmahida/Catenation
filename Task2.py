# Exercise 1 
Value = int(input("Enter a number:", ))
if Value % 3 == 0:
     print("ConsultAdd")
if Value % 5 == 0:
     print("C")
if Value % 3 == 0 and 5 == 0:
     print("Consultadd Python Training")


# Exercise 2
value = int(input("Enter the value 1 for ADDITION, 2 for SUBTRACTION, 3 for DIVISION, 4 for MULTIPLICATION, 5 for AVERAGE"))
if value==1 or value==2 or value==3 or value==4:
    firstvalue = int(input("Enter the first no."))
    secondvalue = int(input("Enter the second no."))
    if value==1:
        print(firstvalue+secondvalue)
    if value==2:
        print(firstvalue-secondvalue)
    if value==3:
        print(firstvalue*secondvalue)
    if value==4:
        print(firstvalue/secondvalue)
elif value==5:
    newfirstvalue = int(input("Enter the first1 no."))
    newsecondvalue = int(input("Enter the second2 no."))
    avg = (newfirstvalue+newsecondvalue)/2
    print(avg)
elif value<0:
    print("NEGATIVE")



# Exercise 3
a = 10
b = 20
c = 30
avg = (a+b+c) / 3
print("avg:",avg)
if ( avg > a) and (avg > b) and (avg > c):
    print("Avg is higher than a,b,c:")
elif(avg > a) and (avg > b):
    print("avg is higher than a,b,c:")
elif(avg > a) and (avg > c):
    print("avg is higher than a,c:") 
elif(avg > b) and (avg > c):
    print("avg is higher than b,c:")
elif(avg > a):
    print("avg is just higher than a:")
elif(avg > b):
    print("avg is just higher than b:")
elif(avg > c):
    print("avg is just higher than c:")



# Exercise 4

while True:
    x = int(input("Enter the VALUE, (-1) TO EXIT"))
    if x<0:
        print("Its over")
        break
    else:
        print("Good Going")
        continue

# Exercise 5
for i in range(2000,3201):
    if i%5!=0:
        if i%7==0:
            print(i)



# Exercise 6
  # 1. TypeError: 'int' object is not iterable
  # 2. 0
      #error
      #1
     #error
    #2
  #3. IndentationError: expected an indented block


# Exercise 7
for value in range(6):
    if value == 3 or value == 6:
        continue
    else:
        print(value)


# Exercise 8
String="Consul12"
print("Expected Output: ", String)
l=d=0

for i in range(len(String)):
    if(String[i].isalpha()):
        l=l+1

    elif(String[i].isdigit()):
        d=d+1
    else:
        pass

print("Letters in String: ", l)
print("Digits in String: ", d)


# Exercise 9

while True :
    guess=int(input("Guess the Lucky Number: "))
    x="Yes"
    y="No"
    if guess == 99 :
        print("You guessed it right")
        break
    if guess != 99 :
        ask=str(input("Try again? Yes/No: "))
        if ask == x :
            continue
        if ask == y :
            break
        else :
            continue   

print("Game Over!")


# Exercise 10
counter = 0
import random
while counter<1:
    x=int(input("Enter the guessing number between 1-50"))
    y=random.randint(1,50)
    counter+=1
    if x==y:
        print("Good Guess)")
    else:
        print("Try again!")

print("5 Guess finished")



# Exercise 11
counter = 0
import random
while counter<1:
    x=int(input("Enter the guessing number between 1-50"))
    y=random.randint(1,50)
    counter+=1
    if x==y:
        print("Good Guess)")
        break
    else:
        print("Try again!")
    print("sorry that was not very successful")

print("5 guess completed")

