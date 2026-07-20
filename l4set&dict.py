# Dictionary
# student = {
#     "name" : "Riya",
#     "age" : 22,
#     "is_adult" : "True",
#     "subject" : ["python","java"]
# }
# print(student)
# print(type(student))
# print(len(student))
# student["name"] = "Pritma"
# print(student)
# #null_dict = {}
# #print(null_dict)
# student["courses_take"] = {
#     "python" : 94,
#     "c++" : 98
# }
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("subject"))
# #print(type(student(subject)))  "" check this query run possible or not ""
# print(student.get("class"))
# #print(student["class"]) this normal access way to get taht key that does not exist gives us error so efficient way to access key and value using .get method.
# print(student.update(class))

# set
# marks = {12,34,56,78,"hello","hello",12,12,34,56,34,44,789}
# print(marks)
# print(type(marks))
# print(len(marks))
# set2 = {12,"bca","mca","hello","world","bsc",12,34 }

# #student = {}        this is the syntax & way  of creating empty dictionary
# #print(type(student))
# #student = set()     this is the syntax and way of creating empty set.
# #print(student)

# (marks.add("world"))
# (marks.remove(789))
# print(marks)
# print(marks.pop())
# print(marks)
# print(marks.union(set2))
# print(marks.intersection(set2))
# print(marks.clear())
# print(marks)

# practice questions: 1
# my_dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture","lists of fact and foigures"]
# }
# print(my_dict)

# practice 2 
# subject = {"python","java","c++","python","c++","javascript","java","python","java","c"}
# print(subject)
# print(type(subject))
# print(len(subject))

# practice 3
# result ={}
# mark1 = int(input("enter your marks of python :"))
# result.update({"python": mark1})
# mark1 = int(input("enter your marks of java :"))
# result.update({"java": mark1})
# mark1 = int(input("enter your marks of c++ :"))
# result.update({"c++": mark1})

# print(result)

# practice 4  store 9 & 9.0 as separate values 
"""
* ist way take 9 or 9.0 as a string one of them  the we store both as separate and uqniue value
* because 9 & 9.0 both values have diff. datatype but python treats automatically as same &
* we can't store this values separately simply.
"""
data = {"9",9.0}        # 1st way
print(data)
data = {"9.0",9}        # 2nd way
print(data)

# or we can  store both values as using tuples with their datatype definig
data = {("integer",9),("float",9.0)}        #3rd way 
print(data) 
 
