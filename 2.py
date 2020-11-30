def s(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2: ]
print(s('Python'))
print(s('Py'))
print(s('w'))
