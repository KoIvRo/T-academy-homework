def isNestable(a1, a2):
    if min(a1) > min(a2) and max(a1) < max(a2):
        return True
    return False
print(isNestable([1, 2, 3, 4], [0, 6]))
print(isNestable([3, 1], [4, 0]))
print(isNestable([9, 9, 8], [8, 9]))
print(isNestable([1, 2, 3, 4], [2, 3]))