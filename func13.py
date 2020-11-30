subject_marks = [('Red', 5), ('Blue', 10), ('Green', 15), ('Yellow', 12)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print("\nSorting the list of tuples:")
print(subject_marks)
