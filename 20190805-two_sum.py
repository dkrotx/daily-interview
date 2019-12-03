def two_sum(lst, k):
    expected = set()
    for item in lst:
        if item in expected:
            return True
        expected.add(k - item)

    return False

print two_sum([4,7,1,-3,2], 5)
# True


print two_sum([1,7,1,-3,2], 5)
# False


print two_sum([1,1], 2)
# True


print two_sum([10, -5, 5], 5)
# True
