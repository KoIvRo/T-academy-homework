def minutesToSeconds(time):
    m, s = map(int, time.split(":"))
    if s >= 60:
        return -1
    return m * 60 + s
print(minutesToSeconds("1:00"))
print(minutesToSeconds("13:56"))
print(minutesToSeconds("10:60"))