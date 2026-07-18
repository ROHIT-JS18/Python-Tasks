# write a program to check whether a number is an armstrong nuber or not 

'''n = int(input("Enter a number :- "))
a = str(n)
sum =0 
while(n>0):
    r = n%10
    sum = sum + n**len(a)
    n = n/10

if (sum==n):
    print('This is an armstrong number')
else :
    print("This is not an armstrong number")
'''

# decimal to binary 

decimal_number = int(input('Enter a number:- '))
binary_number = 0
i = 0
while(decimal_number!=0):
    remainder = decimal_number%2
    binary_number = binary_number + remainder*(10**i)
    decimal_number = decimal_number/2
    i = i+1
print('The binary Number is ', binary_number)