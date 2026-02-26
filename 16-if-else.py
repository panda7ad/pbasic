a=int(input("Enter a number 1 : "))
b=int(input("Enter a number 2 : "))
c=int(input("Enter a number 3 : "))
d=int(input("Enter a number 4 : "))
if( a>b and a>c and a>d):
    print("The greatest number is",a)
elif( b>a and b>c and b>d):
  print("The greatest number is",b)
elif( c>b and c>a and c>d):
  print("The greatest number is",c)
elif( d>b and d>c and d>a):
    print("The greatest number is",d)