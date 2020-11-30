def test_range(n):
    if n in range(2, 12):
        print("%s is in the range" %str(n))
    else:
        print("%s is outside the given range" %str(n))
test_range(13)
