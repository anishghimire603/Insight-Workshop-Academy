nums = [1, 2, 3, 4, 5]
print("Original list of integers:")
print(nums)
print("\nSquare: ")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube: ")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)
