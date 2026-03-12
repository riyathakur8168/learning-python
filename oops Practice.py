# create class and constructor and simply create object the class of the object
# class Car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
    
# c1 = Car("fortuner","40lakh")
# c2 = Car('scorpio',"15lakh")

# print(c1.brand,c1.price)
# print(c2.brand,c2.price)

# class Employee:
#     CompanyName = "Averiq"  #company name is class variable this is same for all the objects of the Employee class
#     def __init__(self,name,salary): # name & salary are instance variable this is diffrent for all the objects of the Employee class
#         self.name = name
#         self.salary = salary
    
# E1 = Employee("Jatin","2.5lakhs")
# E2 = Employee("Yogesh","50000")

# print(E1.CompanyName,E1.name,E1.salary)
# print(E2.name,E2.salary)

# class Calculator:
#     def add(self,a,b):
#         self.a = a
#         self.b = b
#         return a+b
#     def sub(self,a,b):
#         self.a = a
#         self.b = b
#         return a-b
#     def mul(self,a,b):
#         self.a = a
#         self.b = b
#         return a*b
#     def div(self,a,b):
#         self.a = a
#         self.b = b
#         return a/b
    
# A = Calculator()
# print(A.add(10,5))
# print(A.sub(10,5))
# print(A.mul(10,5))
# print(A.div(10,5))

# class Student:
#     def __init__(self,Sname,Smarks):
#         self.Sname = Sname
#         self.Smarks = Smarks

#     def avgerage(self):
#         total = s1.Smarks + s2.Smarks + s3.Smarks
#         avg = total/3
#         print(avg) 
# s1=Student("arjun",98)
# s2=Student("raj",97)
# s3=Student("pritam",67)

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.__balance = balance

#     def deposit(self,ammount):
#         if ammount > 0:
#             self.__balance += ammount
#             print("deposited:",ammount)
#         else:
#             print("please enter positive ammount")

#     def withdraw(self,amount):
#         if amount < self.__balance:
#             self.__balance -=amount
#             print("withdrawn",amount)
#         else:
#             print("insufficient balance in your account.")   

#     def show_balnce(self):
#         print("balance left in your account :",self.__balance)

# c1 = BankAccount("Jatin",200000)
# # print(c1.balance)
# c1.deposit(20000)
# c1.deposit(-200)
# c1.withdraw(5000)
# c1.withdraw(2500000)
# c1.show_balnce()

# class Employee:
#     company_name = "google"
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     def show_details(self):
#         print("Employee name and his/her salary is:",self.name,self.salary)

#     @classmethod
#     def change_company(cls,new_company):
#         cls.company_name = new_company
    
#     @staticmethod
#     def is_valid_salary(amount):
#         return amount > 0
#         # if amount > 0:
#         #     print("true salary")
#         # else:
#         #     print("False")

# e1 = Employee("Jatin",230000)
# e1.show_details()
# Employee.change_company("averiq")
# print(Employee.is_valid_salary(-200))

# class Product:
#     totalProducts = 0
#     def __init__(self, name, price):
#         if Product.is_valid_price(price) > 0:
#             self.name = name
#             self.price = price
#             Product.totalProducts += 1
#         else:
#             print("invalid product price")

#     def __str__(self):
#         return f" {self.name} costs {self.price}"

#     @staticmethod
#     def is_valid_price(price):
#         return price > 0

#     @classmethod
#     def get_totalProducts(cls):
#         return cls.totalProducts

# class Cart:
#     def __init__(self):
#         self.products = []
#     def add_product(self,product):
#         self.products.append(product)

#     def total_bill(self):
#         total = 0                
#         for item in self.products:
#             total += item.price
#             return total
        
#     def show_cart(self):
#         for item in self.products:
#              print(item)

    
# p1 = Product("laptop",50000)
# p2 = Product("MobilePhone",20200)
# p3 = Product("Bluetooth",-10)
# cart = Cart()
# cart.add_product(p1)
# cart.add_product(p2)
# cart.show_cart()

# print(cart.total_bill())

# class Car:
#     def __init__(self,speed):
#         if speed > 0:
#             self.__speed = speed
#         else:
#             print("invalid speed")
#             self.__speed = 0
    
#     def set_speed(self,speed):
#         if speed > 0:
#             self.__speed = speed
#         # else:
#             # print("Invalid speed")
        
#     def get_speed(self):
#         return self.__speed

# c1 = Car(-100)
# print(c1.get_speed())
# # c2 = Car(-20)
# # c2.set_speed(-20)
# # print(c2.get_speed())

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
    
#     def get_balance(self):
#         return self.__balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid amount")
#             self.__balance = self.get_balance()

#     def withdraw(self,amount):
#         if self.__balance > amount:
#             self.__balance -= amount
#         else:
#             print("not enough balance in your account")

# c1 = BankAccount(20000)
# c1.deposit(500)
# print(c1.get_balance())
# c1.deposit(-500)
# print(c1.get_balance())
# c1.withdraw(21000)

class Student:
    def __init__(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid marks")
            self.__marks = -1

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("your marks is :",self.__marks)
        else:
            print("invalid marks")
            # self.__marks = -1

    def get_marks(self):
        return self.__marks

    def grade(self,):
        if self.__marks >= 90:
            print("grade A")
        elif self.__marks >= 75 and self.__marks < 90:
            print("grade B")
        elif self.__marks >= 50 and self.__marks < 75:
            print("grade c")
        else:
            print("Fail")
s1 = Student(95)
print(s1.get_marks())
s1.grade()
s2 = Student(-90)
print(s2.get_marks())