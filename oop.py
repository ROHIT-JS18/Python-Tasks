
# # '''class ABC():
# #     def __init__(self,var):
# #         self.var = var
# #     def display(self):
# #         print('var is = ', self.var)
# #     def add_2(self):
# #         self.var += 2
# #         self.display()

# # obj = ABC(10)
# # obj.add_2()
# # obj.display()
# # '''

# # # Write a program that has a class Person storing names and date of birth (DOB) of a person. The program should subtract the dob from today's date to 
# # # find out whether a person is eligile to vote or not 
# # # '''
# # # import datetime
# # # class Person():

# # #     def __init__(self,name,dob):
# # #         self.name = name 
# # #         self.dob = dob
# # #     def check(self):
# # #         Today = datetime.date.today()
# # #         age = Today.year - self.dob.year
# # #         if Today < datetime.date(Today.year , self.dob.month , self.dob.day):
# # #             age -= 1
# # #         if age >= 18 :
# # #             print('Vote')
# # #         else:
# # #             print('You cant vote')

# # # rohit = Person('Rohit',datetime.date(2006,9,18))
# # # rohit.check()

# # # '''

# # #  Write a program that has a class Numbers with values stored in a list .
# # # Write a class method to find the largest value \
# # # 

# # class Numbers():

# #     def __init__(self):
# #         self.list = []

# #     def check_Max(self):
# #         max = ''
# #         for i in self.list:
# #             if(i>max):
# #                 max = i
# #         print('Maximum is ' ,max)
    
# #     def insert_element(self):
# #         value = input('Enter value:-> ')
# #         self.list.append(value)

# # n = Numbers()
# # ch ='y'
# # while(ch == 'y'):
# #     n.insert_element()
# #     ch = input('Do yu want to enter more elements??')

# # n.check_Max() 


# class student:
#     My_scool = 'NMIET'

#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def change_school(cls,name):
#         cls.My_scool = name
#         return cls.My_scool

# a = student('ROHIT')
# print(a.change_school('PCCOE'))
# print(a.change_school('jspm'))
# print(a.change_school('COEP'))
        


class Square:
    def __init__(self, side):
        self.__side = side
    @property
    def area(self):
        return self.__side * self.__side
    
s = Square(2)
print(s.area)