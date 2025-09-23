def fixString(string):
    if len(string) < 2:
        return string
    cur = 0
    res = ""
    while cur < len(string) - 1:
        res += string[cur + 1]
        res += string[cur]
        cur += 2
    if len(string) % 2:
        res += string[-1]
    return res
print(fixString("123456"))
print(fixString("hTsii  s aimex dpus rtni.g"))
print(fixString("badce"))