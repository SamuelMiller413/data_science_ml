# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

# ------------------------------------- Water
#              up
#      ,@,    /    
#    (######)  -->  forward  >>
#             \
#              down
# 
#  _     _     _     _     _     _     _
# / \/^\/ \/^\/ \/^\/ \/^\/ \/^\/ \/^\/ \
# 
#                       up !decreases depth!
# down and up affect your depth
#                       down !increses depth!
#
#       example route:
            # forward 5             horizontal = 0
            # down 5                depth = 0
            # forward 8
            # up 3                  Target:
            # down 8                    h = 15
            # forward 2                 d = 10
#                                       product = 150
# 
# 
# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.

# create list from directions
    # goal extract to:      1. direction
    #                       2. numbers
# keep a tally. 
#     dictionary? updated by            key=direction   value=number? 
#                                   dict.get(key) + number
            # or
#       tally up, down, and forward     
#           depth = down - up       forward = forward
#              with if statements               

# example_route = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""

# # name tally variables
# depth = 0
# horizontal = 0

# up = 0
# down = 0


# # convert to list
# example_route = example_route.split("\n")
# print(example_route)

# # iterate over those items for tally
# for item in example_route:
#     item = item.split()
#     print(item)

# # if statements by index    
# # remember to int()

#     if item[0] == "up":
#         depth -= int(item[1])
#     if item[0] == "down":
#         depth += int(item[1])
#     if item[0] == "forward":
#         horizontal += int(item[1])
# print(f"\n\nDepth = {depth}\nForward = {horizontal}\n\n")

# # WORKS!!  √



# # ______________________    Puzzle 1:    ______________________

# link txt to variable
day_2_input = "AOC_2021_day_2.txt"
with open(day_2_input, 'r') as puzzle_input:
    route = puzzle_input.read()
depth = 0
horizontal = 0
product = depth * horizontal
up = 0
down = 0
route = route.split("\n")
# print(route)
for direction in route:
    direction = direction.split()
    # print(direction)
    if direction[0] == "up":
        depth -= int(direction[1])
    if direction[0] == "down":
        depth += int(direction[1])
    if direction[0] == "forward":
        horizontal += int(direction[1])
print(f"\n\nDepth = {depth}\nHorizontal = {horizontal}\n")
product = depth * horizontal
print(f"Product = {product}\n\n")



# ______________________    Puzzle 2:    ______________________
#                       Instructions/Test

# for puzzle 2:
# new variable: 'aim'

# up/down change 'aim' (angle of trajectory). 'forward'
# propels the submarine by a product of (aim * forward),
# depth = depth + (aim * forward)
#    -> be mindful of the above formula should the aim be + or -

example_route = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# name tally variables
depth = 0
horizontal = 0
aim = 0
up = 0
down = 0
forward = 0   # add forward variable to distinguish direction from position
# convert to list
example_route = example_route.split("\n")
# print(example_route)
# iterate over those items for tally
for command in example_route:
    command = command.split()
    # print(direction)
# if statements by index    
# remember to int()
    direction = command[0] 
    trajectory = command[1]
    if direction == "up":
        aim -= int(trajectory)
    if direction == "down":
        aim += int(trajectory)
    if direction == "forward":
        forward = int(trajectory)
        horizontal += int(trajectory)
        depth = depth + (aim * forward)
print(f"\n\nDepth = {depth}\nHorizontal = {horizontal}\n")
product = depth * horizontal
print(f"Product = {product}\n\n")


# works!!  √

# ______________________    Puzzle 2:    ______________________
#                          Application

# link txt to variable
day_2_input = "AOC_2021_day_2.txt"
with open(day_2_input, 'r') as puzzle_input:
    route = puzzle_input.read()
# tally variables
depth = 0
horizontal = 0
aim = 0
# trajectory variables
up = 0
down = 0
forward = 0   
# convert to list
route = route.split("\n")
# iterate over those items for tally
for command in route:
    command = command.split()
# if statements by index    
    direction = command[0] 
    trajectory = command[1]
    if direction == "up":
        aim -= int(trajectory)
    if direction == "down":
        aim += int(trajectory)
    if direction == "forward":
        forward = int(trajectory)
        horizontal += int(trajectory)
        depth = depth + (aim * forward)
print(f"\n\nDepth = {depth}\nHorizontal = {horizontal}\n")
product = depth * horizontal
print(f"Product = {product}\n\n")
