def has_character_map(str1, str2):
    if len(str1) != len(str2):
        return False

    charmap = dict()
    for c1, c2 in zip(str1, str2):
        if c1 in charmap:
            if charmap[c1] != c2:
                return False
        else:
            charmap[c1] = c2

    return True

print(has_character_map('abc', 'def'))
# True
print(has_character_map('abca', 'defd'))
# True
print(has_character_map('aac', 'def'))
# False
print(has_character_map('abc', 'de'))
# False
