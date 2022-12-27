# #https://adventofcode.com/

import time

# --- Day 1: Calorie Counting ---
# Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

# To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

# The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

# For example, suppose the Elves finish writing their items' Calories and end up with the following list:

# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# This list represents the Calories of the food carried by five Elves:

# The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
# The second Elf is carrying one food item with 4000 Calories.
# The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
# The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
# The fifth Elf is carrying one food item with 10000 Calories.
# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

# To play, please identify yourself via one of these services:


CurrentElf = 0 
currentelfx = 0 

Elfs = {}

with open('data1.txt') as f:
   for line in f:
    info = line.strip()
    if CurrentElf in Elfs:
        Elfs[CurrentElf].append(info)
    else:
        Elfs[CurrentElf] = [info]

    if info == '':
        CurrentElf += 1
        continue
    print(info)
    # if CurrentElf in Elfs:
    #     Elfs[CurrentElf].append(int(info[0]))
    
        

print(Elfs)        
for i in range(len(Elfs)):
    for k in range(len(Elfs[i])):
        if Elfs[i][k] == '':
            Elfs[i][k] = 0
        Elfs[i][k] = int(Elfs[i][k])
    

   
print(Elfs)        


currentelelfx = []
totalcalofelfs = {}
totalx =0
z=0
for i in range(len(Elfs)):
    for k in range(len(Elfs[i])):
        totalx += Elfs[i][k]
    totalcalofelfs[z] = totalx
    z+=1
    totalx=0

print(totalcalofelfs)
# time.sleep(5)


# def get_max_calories(a:list[str]):
#     maxl = 0
#     try:
#         for i  in range(len(a)):
#             if a[i] == '':
#                 a[i] = 0
#             if int(a[i]) > maxl:
#                 maxl = int(a[i])
#                 elfnumx = i
#     except IndexError:
#         return a[0]
#     return maxl
                

Maxelf = {}

# for i in range(len(totalcalofelfs)):
#     if totalcalofelfs
    
    
    
print('\n')
print(totalcalofelfs[1])
print('\n')
# time.sleep(5)


# print(totalcalofelfs[0])
max_cals=0

for i in range(len(totalcalofelfs)):     
    if totalcalofelfs[i] > max_cals:
        max_cals=totalcalofelfs[i]
        elfnum = i+1

    
print(max_cals)

# max = 0
# for i in range(len(max_cals)):
#     if max_cals[i] > max:
#         max = max_cals[i]

print('\n')    
print('your max calories is:')
print(max_cals)
print('\n')
# for i in range(len(Maxelf)):
#     if Maxelf[i] == max:
#         elfnum = i
print(f'they are elf #{elfnum}')
    


# test passed 
# max cal is 72511 
# elf # 186