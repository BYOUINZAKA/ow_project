def demage(h, d):
    if d >= 30:
        return h + h * (7.0 / 3.0)
    elif d > 20:
        return h + h * (100.0 / (240 - 7 * d) - 1)
    else:
        return h

print(demage(21, 30))
print(demage(70, 20))