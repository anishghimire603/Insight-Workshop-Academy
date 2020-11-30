def case(s):
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    print("No. of Upper case characters : %s" % upper)
    print("No. of Lower case characters : %s" % lower)
case("The quick Brow Fox")
