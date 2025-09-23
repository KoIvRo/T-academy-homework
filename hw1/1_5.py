def countK(num: int, count = 0) -> int:
    if count == 0 and (len(set(str(num))) == 1 or 1000 > num or num > 10000):
        return -1
    if count >= 7:
        return -1
    if num == 6174:
        return count
    num_up = int("".join(sorted(str(num))))
    num_down = int("".join(sorted(str(num)))[::-1])
    return countK(max(num_up, num_down) - min(num_up, num_down), count + 1)

print(countK(3524))
print(countK(6621))
print(countK(6554))
print(countK(1234))