# *** average function
#  def average(): # we can write as if we want to take input from user
#     a = int(input("enter first number:"))
#     b = int(input("enter second number :"))
#     c = int(input("enter third number :"))
#     sum = a+b+c
#     avg = int(sum /3)
#     print(avg)
#     return avg

# average()
 
#  def average(a,b,c): # or we can pass parameters but input value stored in another variables and this 
#     x = int(input("enter first number:")) # input variabbles pass as a arguments in function call
#     y = int(input("enter second number :"))
#     z = int(input("enter third number :"))
#     sum = a+b+c
#     avg = int(sum /3)
#     print(avg)
#     return avg

# average(x,y,z)

# *** square function
# def square():
#     a = int(input("enter a number to do their square :"))
#     print( "square of ", a, "is",a**2)
#     return a**2

# square()

# *** check even& odd 
# def even_odd():
#     num = int(input("enter a number to check if it is even or odd :"))
#     if num % 2 == 0:
#         print(num,"is even number")
#     else:
#         print(num,"is odd number")
#     return num

# even_odd()

# *** return max. value from 3 numbers entered by user
# def max_value():
#     a = int(input("enter first number :"))
#     b = int(input("enter second number :"))
#     c = int(input("enter third number :"))
#     if a>b and a>c :
#         print(a,"is max value")
#     elif b>a and b>c:
#         print(b,"is max value")
#     else:
#         print(c,"is max value")
#     return max(a,b,c)

# max_value()

# def print_length(list):  #* length of list that are entered by us 
#     print("length of the list is :",len(list))
#     return len(list)

# print_length([12,24,35,46,7,4,5,78,98])

#* length of list that are entered by user "this list elemsnts considered as string because input take everything as a string"
# def print_len(list):
#     print("length of list is :",len(list))
#     return len(list)
# user_list = input("entered elements of list :").split()

# print_len(user_list)
# this is the integer list entered by user use map(int,input().split()) and  for float list use map(float,input(()))
# def print_len(list):
#     print("length of list is :",len(list))
#     print(type(list))
#     return len(list)
# user_list = list(map(int,input("entered elements of list :").split()))

# print_len(user_list)

# def print_el(list):
#     i = 0    # agre hum loop se print karvay ge list elements ko to vo simply print hojayge vo python list format me print nhi hoge
#     while i< len(list):
#         print(list[i],end= " ")
#         i +=1
# user_list = input("entered list elemsnts :").split()  

# print_el(user_list)

# def print_el(list): # esliy hum normal print karvayse print function se list taki list ki format me output aay
#     print(list)
#     return list
# user_list = list(map(float,input("enter list elements :").split()))

# print_el(user_list)

# def fact():
#     x = int(input("enter a number to find factorial:"))
#     fact = 1
#     for i in range(1,x+1):
#         fact = fact * i
#     print(fact)
#     return fact

# fact()

# def convert():
#     dollar = int(input("enter amount of dollar :"))
#     exchange_rate = 91.65
#     print("Indian rupee:",dollar * exchange_rate)

# convert()
def print_el(n,num):
    if n>num:
        return
    print(n)
    print_el(n+1,num)

num = int(input("enetr number :"))
print_el(1,num)