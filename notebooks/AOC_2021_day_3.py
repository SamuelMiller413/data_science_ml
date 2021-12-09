# Diagnostic Report

# power consumption
# gamma=''
# epsilon=''
# # consumption=gamma*epsilon


sample = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

# # first bit column
# bit_0=5
# bit_1=7

# # first gamma rate is 10110 or (22 in decimal)
# #                       
# # epsilon is the opposite so its the least common:
# #                       01001 or (9 in decimal)

# # 5 positions
# #   5 lists (position_1, position_2, position_3, position_4, position_5)

# position_1=[] 
# position_2=[]
# position_3=[]
# position_4=[]
# position_5=[]

# position_list =[position_1,position_2,position_3,position_4,position_5]

# sample = sample.split("\n")

# for item in sample:
#     position_1.append(int(item[0]))
#     position_2.append(int(item[1]))
#     position_3.append(int(item[2]))
#     position_4.append(int(item[3]))
#     position_5.append(int(item[4]))
# for position in position_list:    
#     bit_0=0
#     bit_1=0
#     for bit in position:
#         if bit == 0:
#             bit_0+=1
#         else:
#             bit_1+=1

#     # print()
#     # print(f"0={bit_0}")
#     # print(f"1={bit_1}")
#     # print()
    
#     if bit_0>bit_1:
#         gamma += "0"
#         epsilon += "1"
#     else:
#         gamma += "1"
#         epsilon += "0"

# print(f"gamma = {gamma}")
# print(f"epsilon = {epsilon}")
# greek_list = [gamma,epsilon]

# factor_list=[]
# for input in greek_list:
#     decimal = 0
#     n = 1
#     for digit in input:
#         exp = len(input) - n
#         weight = 2 ** exp
#         decimal += (int(digit) * weight)
#         n+=1
#     factor_list.append(decimal) 
# gamma = factor_list[0]
# epsilon = factor_list[1]
# product = gamma * epsilon

# print(f"""\n
# gamma =     {gamma}
# epsilon =   {epsilon}
# ______________________
# product = {product}
# \n""")
# test = 2 ** (len(gamma) - 1)
# print(test)

# So, the gamma rate is the binary number 10110, or 22 in decimal.



# print("Position 1")
# print(f"0={bit_0}")
# print(f"1={bit_1}")
# print()

# print(f" 1= {position_1}")
# print(f" 2= {position_2}")
# print(f" 3= {position_3}")
# print(f" 4= {position_4}")
# print(f" 5= {position_5}")




    
# print(sample) √
# for bit in sample:
#     sample[bit]

# ______________________________________________________________________



# gamma=''
# epsilon=''
# gamma_mod = ''
# day_3_input = "AOC_2021_day_3.txt"
# with open(day_3_input, 'r') as puzzle_input:
#     readings = puzzle_input.read()



# # iterable = readings
# iterable = sample


# flag = "\nflag\n"


# # first bit column
# bit_0=0
# bit_1=0

# position_1=[] 
# position_2=[]
# position_3=[]
# position_4=[]
# position_5=[]
# position_6=[] 
# position_7=[]
# position_8=[]
# position_9=[]
# position_10=[]
# position_11=[]
# position_12=[]
# sample_list =[position_1,position_2,position_3,position_4,position_5]
# position_list =[position_1,position_2,position_3,position_4,position_5,position_6,position_7,position_8,position_9,position_10,position_11,position_12]

# iterable = iterable.split("\n")
# readings = readings.split("\n")
# sample = sample.split("\n")
# iterable_popped = iterable

# readings_popped = readings
# sample_popped = sample

# for item in iterable:
#     position_1.append(int(item[0]))
#     position_2.append(int(item[1]))
#     position_3.append(int(item[2]))
#     position_4.append(int(item[3]))
#     position_5.append(int(item[4]))
#     # position_6.append(int(item[5]))
#     # position_7.append(int(item[6]))
#     # position_8.append(int(item[7]))
#     # position_9.append(int(item[8]))
#     # position_10.append(int(item[9]))
#     # position_11.append(int(item[10]))
#     # position_12.append(int(item[11]))

# # generate position lists
# for position in sample_list:    
#     bit_0=0
#     bit_1=0
#     for bit in position:
#         if bit == 0:
#             bit_0+=1
#         else:
#             bit_1+=1
    
#     if bit_0>bit_1:
#         gamma += "0"
#         epsilon += "1"
#         gamma_mod += "0"

#     elif bit_0==bit_1:
#         gamma_mod +='3'    
#     else:
#         gamma += "1"
#         epsilon += "0"
#         gamma_mod +="1"
    

# # print(f"gamma = {gamma}")
# # print(f"epsilon = {epsilon}")
# greek_list = [gamma,epsilon]

# # popper
# pop_index = 0
# for item in gamma:
#     # gamma or epsilon
    
#     for bit in item:
#         # string of bits
#         loop_count = 0
#         while loop_count <= len(iterable_popped):
              
#             for bit_string in iterable_popped:
#                 target =bit_string[pop_index]
#                 if target == bit:
#                     loop_count += 1
#                 else:
#                     iterable_popped.remove(bit_string)
#                     loop_count += 1
#             # loop_count += 1
#         if len(iterable_popped) == 1:
#             break
#     pop_index+=1
    
#     print(flag)
#     print(iterable_popped)
#     print(flag)
# print(gamma)

# print(gamma_mod)

# # convert to binary
# factor_list=[]
# for input in greek_list:
#     decimal = 0
#     n = 1
#     for digit in input:
#         exp = len(input) - n
#         weight = 2 ** exp
#         decimal += (int(digit) * weight)
#         n+=1
#     factor_list.append(decimal) 
# gamma = factor_list[0]
# epsilon = factor_list[1]
# product = gamma * epsilon

# print(f"""\n
# gamma =     {gamma}
# epsilon =   {epsilon}
# ______________________
# product = {product}
# \n""")


# ____________________________________


gamma=''
epsilon=''
gamma_mod = ''
epsilon_mod = ''
greek_list=[]
day_3_input = "AOC_2021_day_3.txt"
with open(day_3_input, 'r') as puzzle_input:
    readings = puzzle_input.read()

iterable = readings


flag = "\nflag\n"


# first bit column
bit_0=0
bit_1=0

position_1=[] 
position_2=[]
position_3=[]
position_4=[]
position_5=[]
position_6=[] 
position_7=[]
position_8=[]
position_9=[]
position_10=[]
position_11=[]
position_12=[]
sample_list =[position_1,position_2,position_3,position_4,position_5]
position_list =[position_1,position_2,position_3,position_4,position_5,position_6,position_7,position_8,position_9,position_10,position_11,position_12]

iterable = iterable.split("\n")
readings = readings.split("\n")
sample = sample.split("\n")
iterable_popped = iterable

readings_popped = readings
sample_popped = sample
for item in iterable:
    position_1.append(int(item[0]))
    position_2.append(int(item[1]))
    position_3.append(int(item[2]))
    position_4.append(int(item[3]))
    position_5.append(int(item[4]))
    position_6.append(int(item[5]))
    position_7.append(int(item[6]))
    position_8.append(int(item[7]))
    position_9.append(int(item[8]))
    position_10.append(int(item[9]))
    position_11.append(int(item[10]))
    position_12.append(int(item[11]))
# generate position lists
for position in position_list:    
    bit_0=0
    bit_1=0
    for bit in position:
        if bit == 0:
            bit_0+=1
        else:
            bit_1+=1
    if bit_0>bit_1:
        gamma += "0"
        gamma_mod += "0"
    elif bit_0==bit_1:
        gamma_mod +='1'

    else:
        gamma += "1"
        gamma_mod +="1"
    

# print(f"gamma = {gamma}")
# print(f"epsilon = {epsilon}")
# print(gamma_mod)


# greek_list = [gamma,epsilon]

# popper
pop_index = 0

while len(iterable_popped) > 1:    
    
    loop_count = 0
    other_count = 0
    while loop_count <= len(iterable_popped) *100:
            
        for bit_string in iterable_popped:
            
            gamma_mod_tar = gamma_mod[pop_index]
            target =bit_string[pop_index]
            if gamma_mod_tar== 3:
                
                if target == 1:
                    loop_count += 14
                else: 
                    iterable_popped.remove(bit_string)
                
            else:
                if target == gamma_mod_tar:
                    loop_count += 1
                else:
                    iterable_popped.remove(bit_string)
                    loop_count += 1
        # loop_count += 1
        if len(iterable_popped) == 2:
            break
    position_1=[] 
    position_2=[]
    position_3=[]
    position_4=[]
    position_5=[]
    position_6=[] 
    position_7=[]
    position_8=[]
    position_9=[]
    position_10=[]
    position_11=[]
    position_12=[]
    sample_list =[position_1,position_2,position_3,position_4,position_5]
    position_list =[position_1,position_2,position_3,position_4,position_5,position_6,position_7,position_8,position_9,position_10,position_11,position_12]

    for item in iterable_popped:
        position_1.append(int(item[0]))
        position_2.append(int(item[1]))
        position_3.append(int(item[2]))
        position_4.append(int(item[3]))
        position_5.append(int(item[4]))
        position_6.append(int(item[5]))
        position_7.append(int(item[6]))
        position_8.append(int(item[7]))
        position_9.append(int(item[8]))
        position_10.append(int(item[9]))
        position_11.append(int(item[10]))
        position_12.append(int(item[11]))
    gamma=''
    epsilon=''
    gamma_mod = ''
    epsilon_mod = ''
    for position in position_list:    
        bit_0=0
        bit_1=0
        for bit in position:
            if bit == 0:
                bit_0+=1
            else:
                bit_1+=1
        if bit_0>bit_1:
            gamma += "0"
            gamma_mod += "0"
        elif bit_0==bit_1:
            gamma_mod +='1'   
        elif bit_0<bit_1:
            gamma += "1"
            gamma_mod +="1"
    
    pop_index+=1
    print(f"""gamma = {gamma_mod}
    ep = {epsilon_mod}""")
# print(flag)
# print(iterable_popped)
gamma_final = ''
for item in iterable_popped:
    gamma_final += item


greek_list.append(gamma_final)


print(gamma_mod)





gamma=''
epsilon=''
gamma_mod = ''
epsilon_mod = ''
day_3_input = "AOC_2021_day_3.txt"
with open(day_3_input, 'r') as puzzle_input:
    readings = puzzle_input.read()

iterable = readings


flag = "\nflag\n"


# first bit column
bit_0=0
bit_1=0

position_1=[] 
position_2=[]
position_3=[]
position_4=[]
position_5=[]
position_6=[] 
position_7=[]
position_8=[]
position_9=[]
position_10=[]
position_11=[]
position_12=[]
sample_list =[position_1,position_2,position_3,position_4,position_5]
position_list =[position_1,position_2,position_3,position_4,position_5,position_6,position_7,position_8,position_9,position_10,position_11,position_12]

iterable = iterable.split("\n")
readings = readings.split("\n")
# sample = sample.split("\n")
iterable_popped = iterable

iterable = readings  #djfbrv
readings_popped = readings
sample_popped = sample
for item in iterable:
    position_1.append(int(item[0]))
    position_2.append(int(item[1]))
    position_3.append(int(item[2]))
    position_4.append(int(item[3]))
    position_5.append(int(item[4]))
    position_6.append(int(item[5]))
    position_7.append(int(item[6]))
    position_8.append(int(item[7]))
    position_9.append(int(item[8]))
    position_10.append(int(item[9]))
    position_11.append(int(item[10]))
    position_12.append(int(item[11]))
# generate position lists
for position in position_list:    
    bit_0=0
    bit_1=0
    for bit in position:
        if bit == 0:
            bit_0+=1
        else:
            bit_1+=1
    if bit_0>bit_1:
        epsilon += "0"
        epsilon_mod += "0"
    elif bit_0==bit_1:
        epsilon_mod += "0"    
    else:
        epsilon += "1"
        epsilon_mod += "1"
    

# print(f"gamma = {gamma}")
# print(f"epsilon = {epsilon}")
# greek_list = [gamma,epsilon]

# popper
pop_index = 0
# for item in gamma_mod:
    # gamma or epsilon

while len(iterable_popped) > 1:    
    
    loop_count = 0
    other_count = 0
    while loop_count <= len(iterable_popped)*100:
            
        for bit_string in iterable_popped:
            epsilon_mod_tar = epsilon_mod[pop_index]
            target =bit_string[pop_index]
            if epsilon_mod_tar== 3:
                if target == 0:
                    loop_count += 1
                else: 
                    iterable_popped.remove(bit_string)
                
            else:    
                if target == epsilon_mod_tar:
                    loop_count += 1
                else:
                    iterable_popped.remove(bit_string)
                    loop_count += 1
        # loop_count += 1
        if len(iterable_popped) == 1:
            break
    position_1=[] 
    position_2=[]
    position_3=[]
    position_4=[]
    position_5=[]
    position_6=[] 
    position_7=[]
    position_8=[]
    position_9=[]
    position_10=[]
    position_11=[]
    position_12=[]
    sample_list =[position_1,position_2,position_3,position_4,position_5]
    position_list =[position_1,position_2,position_3,position_4,position_5,position_6,position_7,position_8,position_9,position_10,position_11,position_12]

    for item in iterable_popped:
        position_1.append(int(item[0]))
        position_2.append(int(item[1]))
        position_3.append(int(item[2]))
        position_4.append(int(item[3]))
        position_5.append(int(item[4]))
        position_6.append(int(item[5]))
        position_7.append(int(item[6]))
        position_8.append(int(item[7]))
        position_9.append(int(item[8]))
        position_10.append(int(item[9]))
        position_11.append(int(item[10]))
        position_12.append(int(item[11]))
    gamma=''
    epsilon=''
    gamma_mod = ''
    epsilon_mod = ''
    for position in position_list:    
        bit_0=0
        bit_1=0
        for bit in position:
            if bit == 0:
                bit_0+=1
            else:
                bit_1+=1
        if bit_0>bit_1:
            epsilon += "0"
            epsilon_mod += '0'
        elif bit_0==bit_1:
            epsilon_mod +='0'    
        else:
            epsilon += "1"
            epsilon_mod += '1'
    
    pop_index+=1
    print(f"""gamma = {gamma_mod}
    ep = {epsilon_mod}""")

epsilon_final = ''
for item in iterable_popped:
    epsilon_final += item
# gamma_final = '101001110100'
# epsilon_final = '010110110110'
greek_list = [gamma_final]
greek_list.append(epsilon_final)
# print(iterable_popped)
# print(flag)
# print(epsilon_mod)
print(greek_list)


# convert to binary
factor_list=[]
for input in greek_list:
    decimal = 0
    n = 1
    for digit in input:
        exp = len(input) - n
        weight = 2 ** exp
        decimal += (int(digit) * weight)
        n+=1
    factor_list.append(decimal) 
gamma = factor_list[0]
epsilon = factor_list[1]    
product = gamma * epsilon
print(greek_list)
print(f"""\n
gamma =     {gamma}
epsilon =   {epsilon}
______________________
product = {product}
\n""")
