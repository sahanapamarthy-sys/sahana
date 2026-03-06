def say_goodbye(name): 
    print("Hello,", name)   

def area_circle(radius): 
    area = 3.14 * (radius**2)
    print(area)

def subtract(a,b): 
    return a-b 
def multiply(a,b):
    return a * b 
def divide(a,b):
    return a/b

readings = [15, 14, 17, 20, 23, 28, 20]
def weather():
    minimum = min(readings)
    maximum = max(readings)
    return (minimum,maximum)

week = {"Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday" : 4, "Friday" : 5, "Saturday" : 6, "Sunday" :7}

def weekend_number(day): 
    if week[day] == 6 or week[day] == 7: 
        return True 
    else:
        return False  


def decal_trip(distance,fuel_used):
    fuel = distance / fuel_used
    return fuel

def secret_code(number):
    num_str = str(number)
    return int(num_str[-1] + num_str[:-1])

def hacked_computer(x,y): 
    value = 1 
    for i in range (y): 
        value = value * x 
    return value 

num = [1,2,3,4,5,6,7,8,9,10]

def min_list(num): 
    small = num[0]
    for numbers in num: 
        if numbers < small: 
            small = numbers 
    return small 

def max_list(num):
    largest = num[0]   
    
    for number in num:
        if number > largest: 
            largest = number
            
    return largest

def min_while(num):
    smallest = num[0]  
    i = 1     
    
    while i < len(num):
        if num[i] < smallest:
            smallest = num[i]
        i += 1
    return smallest


def max_while(num):
    largest = num[0]  
    i = 1             
    
    while i < len(num):
        if num[i] > largest:
            largest = num[i]
        i += 1
    
    return largest

def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
        
    return total

#my favorite code 
def hacked_computer(x,y): 
    value = 1 
    for i in range (y): 
        value = value * x 
    return value 
result = (hacked_computer(3,3))

print("The result of Oski Stole Your Power (5.1) with x = 3 and y = 3 is", result)