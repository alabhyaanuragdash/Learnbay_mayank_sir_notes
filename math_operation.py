def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def power(x,y):
    return x**y

def floor_div(x,y):
    return x//y

def average(x,y):
    return (x+y)/2
    
def factorial(x):
    if x==1 or x==0:
        return 1
    elif x<0:
        print("enter valid no")
    else:
        return (x*factorial(x-1))
def max(x,y):
    if x>y:
        return x
    else:
        return y

def min(x,y):
    if x<y:
        return x
    else:
        return y

def cumulative_sum():
    sum=0
    for i in n:
        s=s+i
    return s