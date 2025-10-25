def is_divisible(n,x,y):
    return n % x == 0 and n % y ==0

def bmi(weight, height):
    height=height**2
    bmi = weight / height
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    return "Obese"

def find_multiples(integer, limit):
    return list(range(integer,limit+1,integer))

