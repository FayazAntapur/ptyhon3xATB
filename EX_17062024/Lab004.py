def test(*args, base):
    for i in args:
        print(i)
    print(base)


test(23, 45, 23, base="testing")
