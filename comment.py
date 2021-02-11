# a=int(input('enter a number:'))
# for i in range(a):
#     print(i**2)



# n=int(input('enter a number:'))
# if n%2==0:
#     if n>=2 and n<=5:
#         print('not weird')
#     elif n>=6 and n<=20:
#         print('weird')
#     elif n>20:
#         print('not weird')     
# else:
#     print('weird')              
             

# def a():
#     def b():
#         return('xyz')
    
#     res=b() + ' disc function'
#     return res

# x=a() 
# print(x)

# a=2020
# b=100
# print(a%b)





# def abc():
#     year=int(input('enter a year  :'))
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return 'leap year'
#             else:
#                 return 'not leap year'
#         else:
#             return 'Leap year'
#     else:
#         return 'Not leap year'    
# print(abc())     



# a=lambda x,y,z:x**3+y*z
# print(a(5,7,9))


# def a(n):
#     return lambda a,b:a**2+n+b
# c=a(3)    
# print(c(5,6))




# list1=[1,2,3,4,5,6]
# list2=[10,11,12,13,14,15]
# # square=list(map(abc,list1)) 
# square=list(map(lambda a,b:a+b,list1,list2))
# print(square)  
# print(type(square))

# for i in square:
#     print(i)




a=[1,2,3,'jkl',23]
a.remove(3)
print(a)