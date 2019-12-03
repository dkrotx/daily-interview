def mirror_number(n):
    res = 0
    while n > 0:
        res *= 10
        digit = n % 10
        n //= 10
        res += digit

    return res

def is_palindrome(n):
    mirror = mirror_number(n)
    while n > 0 and mirror > 0:
        digit_1, digit_2 = n % 10, mirror % 10
        if digit_1 != digit_2:
            return False
        n //= 10
        mirror //= 10

    return n == 0 and mirror == 0

print is_palindrome(1234321)
# True
print is_palindrome(1234322)
# False


print is_palindrome(123)
# False


print is_palindrome(10)
# False


print is_palindrome(1)
# True
print is_palindrome(0)
# True
