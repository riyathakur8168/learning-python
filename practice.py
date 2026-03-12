# "task 1 : reverse a tring"
# name = input("enter your name :")
# reversed_string = name[::-1]
# print(reversed_string)

# s = input("enter a string:")
# rev =" "
# for ch in s:
#     rev = ch + rev
# print(rev)

# task 2 : count number of vowels and constants in a string
# s = input("enter a string :")
# vowels = 0
# constants = 0
# for ch in s:
#     if ch.lower() in "aeiou":
#         vowels+=1
#     elif ch.isalpha():
#         constants+=1

# print("vowels :",vowels)
# print("constants:",constants)

# task 3 : count number of words in string
# s = input("enter a string :")
# words = s.split()
# print(words) # print string  words in list format ignore apce and number 
# print(len(words))

# task 4: check string palindrone or not
# s = input("enter a string:")
# reversed_string = s[::-1]
# if s==reversed_string:
#     print("plaindrome")
# else:
#     print("not palindrome")

# tak 5 : sum  of list entered by user using function
# def list_sum(list):
#     sum = 0
#     for el in list:
#         sum += el
#     print(sum)
#     return sum
# user_list = list(map(int,input("enter list numbers :").split()))

# list_sum(user_list)

# task 6 : find largest number from the list using function
# def list_max(list):
#     max = list[0]
#     for n in list:
#         if n > max:
#             max = n
#     print(max)
#     return max
# user_list = list(map(int,input("eneter list elements:").split()))

# list_max(user_list)

# task 7 : find even and odd from list and return even in another list and odd in another list using function 
# def even_odd(list):
#     list1 =[]
#     list2 = []
#     for n in list:
#         if n%2==0:
#             list1.append(n)
#         else:
#             list2.append(n)
#     print(list1)
#     print(list2)
#     return(list1)
#     return list2
# user_list = list(map(int,input("enter list numbers :").split()))

# even_odd(user_list)
# task 8 : calculate average of the number list entered by user.
# def list_avg(list):
#     total = 0
#     for el in list:
#         total += el
#     print(total)
#     average = total/len(list)
#     print(average)
#     return average
# user_list = list(map(int,input("enter list elements :").split()))

# list_avg(user_list)

# task 9 : dictionary practice - take 3 students from the user  and store them in dictionary and print the name and calculate average of the marks

# def student_info():
#     students = {}
#     for i in range(3):
#         name = input("enter student name :")
#         marks = int(input("enter your marks:"))
#         students[name] = marks 
    
#     print("students name :")
#     for name in students:
#         print(name)
#     total = 0
#     for i in students.values():
#         total += i 
#         average = total/len(students)
#     print(average)
#     return average

# student_info()

#task 9 : take list from user and remove  duplicates from list using set
# num = list(map(int,input("enter list elements:").split()))
# print(num)
# set1 = set(num)
# print(set1)

#task 10 : take 2 list from user and find common elements from both list using set
# list1 = list(map(int,input("enter list elements:").split()))
# list2 = list(map(int,input("enter list elements:").split()))

# set1 = set(list1)
# set2 = set(list2)

# print(set1.intersection(set2))

# #task 11 : take 2 list from user and find union of both list using set
# list1 = list(map(int,input("enter list elements:").split()))
# list2 = list(map(int,input("enter list elements:").split()))

# set1 = set(list1)
# set2 = set(list2)

# print(set1.union(set2)) 

#task 12 : take 2 list from user and find difference of both list using set
list1 = list(map(int,input("enter list elements:").split()))
list2 = list(map(int,input("enter list elements:").split()))

set1 = set(list1)
set2 = set(list2)

print(set1.difference(set2)) 


