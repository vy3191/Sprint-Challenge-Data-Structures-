import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


#Try 1 --->  1.13496 seconds in my laptop
# duplicates = [name for name in names_1 if name in names_2]


#Try 2 ---> 0.0059828 seconds in my machine

#1)Loop trough the name_1 list  
# 2)store the names in the dictionary as keys 
# 3) loop through the second list 
# 4) if name in a second list found in the dictionary then push it to the dictionary.
duplicate_dict = {}
for name in names_1:
    duplicate_dict[name] = True
for name in names_2:
    if name in duplicate_dict:
        duplicates.append(name)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
