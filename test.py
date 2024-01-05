#!/usr/bin/python3
# import dis
# import time

# st = time.perf_counter()
# def fact():
#     for i in range(20000):
#         z = i ** 2
#     return z
# end = time.perf_counter()
# fact()
# print(end - st)

# st = time.perf_counter()
# for i in range(20000):
#      z = i ** 2
# end = time.perf_counter()
# print(end - st)


from math import pi

def circle_area(r):
    return pi*(r**2)

#test function
radii = [2, 3, -3, 2 + 5j, True, "radius"]

message = "Area of circle with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius = r, area = A))