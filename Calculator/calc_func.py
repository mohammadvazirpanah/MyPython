import math

def calculate():
        operation = int(input('''
    Please Type in the Math Operation You Would Like to Complete:\n
    1 For Addition
    2 For Subtraction
    3 For Multiplication
    4 For Division
    5 For Find Min & Max
    6 For Square root
    7 For Power
    8 Exit
    '''))
        return operation


# min & max
def min_fun ():
    a= int(input("Number:"))
    list1 =[] 
    for i in range (a):
        b= int(input(f"adade {i} om ra vared konid:"))
        list1.append(b) 
    print (list1)
    max1 = max(list1)
    min1 = min(list1)
    print ("min=",min1)
    print ("max=",max1)

# SUM
def sum_fun ():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    return(number_1 + number_2)

# SUBTRACT
def sub_fun ():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    return(number_1 - number_2)

# multiplication
def multi_fun ():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    return(number_1 * number_2)

# division
def div_fun ():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    return(number_1 / number_2)

# square root
def squ_fun():
    number = int(input('Enter your number: '))
    return(math.sqrt(number))

#power
def pow_fun():
    number_1 = int(input('Enter your base number: '))
    number_2 = int(input('Enter your exponent number: '))
    return(math.pow(number_1, number_2))
    




