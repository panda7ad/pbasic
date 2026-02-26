def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("ENTER A:-"))
b=int(input("ENTER B:-"))
print("GCD OF  A AND B IS :-",gcd(a,b))