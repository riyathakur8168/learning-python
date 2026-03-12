"""
num = input("enter a num:")
print(type(num))

c = int(str(123))
sum = c+10
print(sum)
a = float(input("enter a num :"))
print(int(float(a)))


num = int(input("enter a num:"))

if num%2==0:
    print("even")
else:
    print("odd")

num = int(input("enter a num:"))
 
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

for i in range(1,21):
    print(i)

for i in range(1,51,):
    if i%2!=0:   
         print(i)

sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)

num = int(input("enter a number:"))
for i in range(1,11):
    print(num,"*",i,"=25",num*i)

for i in range(20,0,-1):
    print(i)

num = int(input("enter a number:"))

count = 0
for i in range (1,num+1):
    if num% i == 0:
        count += 1

if count == 2:
    print("prime number")
else:
    print("not prime number")

num = int(input("enter a number:"))

fact = 1
for i in range(1,num+1):
    fact = fact * i

print(fact)

for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print() 
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print() 


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print() 

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print() 
"""
# num = [23,34,56,78,90]
# print(num[0])
# print(num[-1])
# print(len(num))

#for i in range(len(num)):
 #   print(num[i])

#for x in num:
 #   print()


#str = "hi im riya . i'm learning python from apna college."
# str1 = "$dollar price is ruppee 98."
# print(str + " " + str1)
# print(len(str))
# print(len(str1))
# str2 =" hello \n world."
# print(str2)
# str3 =" hello \t world."
# print(str3) 
# print(str1[0:12])
# print(str1[:12])
# print(str1[12:28])
# print(str1[12:len(str1)])
# print(str1[12:])
# print(str[-12:-1])
# print(str.endswith("ege."))
# print(str.endswith("er"))
# print(str.capitalize())
# print(str)
# str = print(str.capitalize())

# #print(str.replace("o","a"))
# #print(str.replace("python","java"))
# print(str.find("apna"))
# print(str.find("to"))
# print(str.count("m"))

marks = int(input("enter your marks:"))

if (marks>=90):
    print("grade A")
elif (marks>=80 and marks<90):
    print("grade B")
elif (marks>=70 and marks<80):
    print("grade C")
elif (marks>=60 and marks<70):
    print("grade D")
else :
    print("pass only")

print("end of code")






 




