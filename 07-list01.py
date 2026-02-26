#a=["apple","orange",5,345.06,"Aakash",'Rohan'] #list[]
#print(a)
#a[0] = "grapes"
#print(a[0],a[1],a[2],a[3],a[4])

t=['a','b','c']
t.append('d')
print(t)

t1=['e','f']
t.extend(t1)
print(t)

alist=['zara','xyz',123,123,'accd']
b=alist.count('xyz')
print(b)

alist=[123,'xyz','zara','abc']
#alist.remove('xyz')
print(alist)

alist.pop()
print(alist)

alist.pop(2)
print(alist)

alist1=[123,'xyz','zara','abc','xyz']
alist1.reverse()
print(alist1)

#alist.sort(func)
#list.pop(index)
#list.remove(obj)
#list.insert(index,obj)
#list.append(obj)

alist.insert(3,2009)
print(alist)


