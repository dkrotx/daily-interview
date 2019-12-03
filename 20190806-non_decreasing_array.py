def check(lst):
    n = 0
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            n += 1

    return n <= 1

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False


print check([])
# True
print check([1])
# True
print check([1,2,3,4])
# True
print check([1,1,1,1])
# True


print check([1,0,1,1])
# True


print check([1,0,1,0])
# False
