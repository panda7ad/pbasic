n=int(input("enter a number:"))
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)
print( f"the factorial is {factorial(n)}")

def t_to_F(c):
    return 5*(c-32)/9
c=int(input("Enter the Temperature in F :"))
print(f"The Temperature is {round(t_to_F(c),2)} in C")

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
n=int(input("Enter a Number :"))
print(sum(n))