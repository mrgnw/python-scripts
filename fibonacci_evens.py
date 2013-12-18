def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def evens(list):
    new_list = []
    for i in list:
        if is_even(i):
            new_list.append(i)
    return new_list

def fib_helper(n):
    if n == 0:
        return 0
    else:
        return fib_improved(n, 0, 1)


def fib_improved(n, p0, p1):
    if n == 1:
        return p1
    else:
        return fib_improved(n-1, p1, p0 + p1)


def fibs_under(x):
    fibs = []

    count = 2
    while fib_helper(count) < x:
        #print fib_helper(count)
        fibs.append(fib_helper(count))
        count += 1

    return fibs

#print fib_helper(18)

print sum(evens(fibs_under(4000000)))
