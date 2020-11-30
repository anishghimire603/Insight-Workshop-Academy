def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2, 4, 5, 10, 5, 8, 10, 5]
print(Remove(duplicate))