def step(num):
    res, cur = "", 0
    while cur < len(num):
        res += str(int(num[cur]) + int(num[cur+1]))
        cur += 2
    return int(res)
def isPalindromeDescendant(num):
    num = str(num)
    if len(num) > 1:
        if len(num) % 2 == 0:
            if num[:len(num)//2] == num[len(num)//2:][::-1]:
                return True
            return isPalindromeDescendant(step(num))
        else:
            if num[:len(num)//2] == num[len(num)//2+1:][::-1]:
                return True
            return isPalindromeDescendant(step(num))
    else:
        return False
print(isPalindromeDescendant(123312))
print(isPalindromeDescendant(11211230))
print(isPalindromeDescendant(13001120))
print(isPalindromeDescendant(23336014))
print(isPalindromeDescendant(11))