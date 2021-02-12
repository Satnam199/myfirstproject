# n=int(input('enter a number:'))
# a=int(input('enter number a :'))
# b=int(input('enter number b :'))
# sum=0
# while n>=sum:
#     print(sum)
#     a=b
#     b=sum
#     sum=a+b


a=int(input('enter a number:'))
flag=0

for i in range(2,a):
    if a%i==0:
        flag=1
if flag==0:
    print('prime number')        
else:
    print('non prime')    
        