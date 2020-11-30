sentence = input("Input comma separated sequence of words: ")
words = [word for word in sentence.split(",")]
print(",".join(sorted(list(set(words)))))
