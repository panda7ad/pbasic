d={} #empty dictionary
marks = {
     "adarsh":98,
     "pranshu":78,
     "pranav":87,
     "yuvi":13,
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"yuvi":78})
print(marks.get("yuvi"))
print(marks["yuvi"])
print(marks.get("yuvi2")) #gives none
print(marks["yuvi2"])    #return error
value=marks.popitem()
print(value)
print(marks)