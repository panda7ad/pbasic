def avg():
    n=int(input("Enter A number :"))
    for i in range(1, n+1):
        print(" "*  (n-i),end="")
        print("*"*  (2*i-1),end="")
        print("")
avg()
avg()
avg()
avg()

def goodday(name,ending):
    print(ending,name)
    print(name,ending)
    return("done")


a=goodday("harry","thanks")
print(a)
goodday("adarsh","thanks")
goodday("aditya","thanks")
goodday("adit","thanks")