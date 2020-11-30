array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]
print("Given Arrays:")
print(array1)
print(array2)
result = list(filter(lambda x: x in array1, array2))
print ("\nIntersection of two given arrays: ",result)