tuple1 = ["p", "r", "o", "g", "r", "a", "m", "m", "e"]
print(tuple1)
tuple1 = tuple1[ :2] + tuple1[3: ]
print(tuple1)
listx = list(tuple1)
listx.remove("m")
tuple1 = tuple(listx)
print(tuple1)
