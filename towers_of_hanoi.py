# Prints all the individual moves necessary to
# transfer n blocks from tower t1 to tower t2.
def pm(n, t1, t2):
    if n == 1:
        print(t1, "->", t2)
        return
    t3 = 6 - t1 - t2
    if n == 2:
        print(t1, "->", t3)
        print(t1, "->", t2)
        print(t3, "->", t2)
        return
    pm(n - 1, t1, t3)
    print(t1, "->", t2)
    pm(n - 1, t3, t2)
    
# Prints all the individual moves necessary to
# transfer n blocks from tower 1 to tower 3.
def print_moves(n):
        pm(n, 1, 3)

print_moves(4)
# print_moves(2)
# 1 -> 2
# 1 -> 3
# 2 -> 3

# print_moves(3)
# 1 -> 3
# 1 -> 2
# 3 -> 2
# 1 -> 3
# 2 -> 1
# 2 -> 3
# 1 -> 3
