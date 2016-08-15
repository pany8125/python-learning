def add_num(*args):
    result = 0
    for a in args:
        result+= a
    print(result)

add_num(3)
add_num(3,32)
add_num(32,432,543,645,3)