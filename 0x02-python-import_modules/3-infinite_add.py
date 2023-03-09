
import sys
count = 0
for i in sys.argv:
    count += i
    str = "{}"
print(str.format(count))