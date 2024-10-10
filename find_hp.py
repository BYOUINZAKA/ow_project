import sys
import math

max_percent=int(sys.argv[1])
hp=int(sys.argv[2])

for i in range(max_percent):
    val = float(hp)*(i/max_percent)
    if math.floor(val) == val:
        print(f"{i}/{max_percent}: \t{val}")