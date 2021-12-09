


# v   
# data_set = 1


# mean_squared_error = 0
# m = len(data_set)
# for i in range(1,m):
#     mean_squared_error += (y[i] -y_hat[i])**2
# mean_squared_error = mean_squared_error/m

# i=0
# for num in range(11):
#     i+=num
# print(i)

# sigma = 0
# for x in range(1, 11):
#     sigma += x*3
# print(sigma)

# # numbers = [1,2,3,4,5,6,7,8,9,10]
# # np.sum(3*numbers)

# sum=0
# for x in range(10,21):
#     sum += (2*x) + 10
# print(sum)

# sum=0
# for x in range(1,4):
#     sum += ((4* (x**2) + (2*x) + 6)**2)
# print(sum)

# sum=0
# for x in range(2,4):
#     sum += x * 5
# print(sum)
# print(5^2)

# y=0
# x=0
# m=0
# c=0

# y = -100
# x = -1.5
# c=-150

# y = (m*x) + c

# -100 = m*-1.5 +-150
# 50 = -1.5 * m
# m = -33.33

# d = 5
# print(d)



# example_route = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""

# # name tally variables
# depth = 0
# horizontal = 0
# aim = 0
# up = 0
# down = 0
# forward = 0   # add forward variable to distinguish direction from position
# # convert to list
# example_route = example_route.split("\n")
# # print(example_route)
# # iterate over those items for tally
# for command in example_route:
#     command = command.split()
#     # print(direction)
# # if statements by index    
# # remember to int()
#     direction = command[0] 
#     trajectory = command[1]
#     if direction == "up":
#         aim -= int(trajectory)
#         turtle.left(aim)
#     if direction == "down":
#         aim += int(trajectory)
#         turtle.right(aim)
#     if direction == "forward":
#         forward = int(trajectory)
#         horizontal += int(trajectory)
#         depth = depth + (aim * forward)
#         turtle.forward(trajectory)
# print(f"\n\nDepth = {depth}\nHorizontal = {horizontal}\n")
# product = depth * horizontal
# print(f"Product = {product}\n\n")
# import turtle
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     example_route = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""

#     # name tally variables
#     depth = 0
#     horizontal = 0
#     aim = 0
#     up = 0
#     down = 0
#     forward = 0   # add forward variable to distinguish direction from position
#     # convert to list
#     example_route = example_route.split("\n")
#     # print(example_route)
#     # iterate over those items for tally
#     for command in example_route:
#         command = command.split()
#         # print(direction)
#     # if statements by index    
#     # remember to int()
#         direction = command[0] 
#         trajectory = command[1]
#         if direction == "up":
#             aim -= int(trajectory)
#             turtle.left(aim)
#         if direction == "down":
#             aim += int(trajectory)
#             turtle.right(aim)
#         if direction == "forward":
#             forward = int(trajectory)
#             horizontal += int(trajectory)
#             depth = depth + (aim * forward)
#             turtle.forward(trajectory)
#     # print(f"\n\nDepth = {depth}\nHorizontal = {horizontal}\n")
#     product = depth * horizontal
#     # print(f"Product = {product}\n\n")
#     if abs(pos()) < 1:
#         break
# # end_fill()
# done()

# import turtle


# while True:
#     example_route = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""

    

#     turtle.forward(8)

# ghu = "hello"
# print(ghu)

import numpy as np
def binary_entropy(p1):
    return -1 * (p1*np.log2(p1) + (1-p1)*np.log2(1-p1))
# p1 = probability?
x = binary_entropy(.75)
y = binary_entropy(.89)
z = x-y
print(z)