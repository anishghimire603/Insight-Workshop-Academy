def adding_string(str):
  length = len(str)

  if length > 2:
    if str[-3: ] == 'ing':
      str += 'ly'
    else:
      str += 'ing'

  return str
print(adding_string('ab'))
print(adding_string('abc'))
print(adding_string('string'))
