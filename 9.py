def change_sring(str):
    return str[-1: ] + str[1:-1] + str[ :1]
print(change_sring('python'))