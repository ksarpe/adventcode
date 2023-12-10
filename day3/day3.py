import string

file = "day3.txt"

content = []
symbols = [char for char in string.printable if not char.isalnum() and char != '.']

with open(file, "r") as f:
    for line in f:
        content.append(line.strip())
parts_sum = 0

def is_adjacent(start, end, line): #np 4, 4, 0
    powers = end - start # for example 0
    length = end - start + 1 # if starts in 0 and end in 2 then length is 3, simple as fuck
    number = 0

    # Get this considered number
    for x in range(powers + 1):
        digit = int(content[line][end - x])
        number += digit * pow(10, x)
    # Check wether number has any neighbours, diagonal included
    # firstly check top-left corner to top-right corner
    for i in range(length + 2): # above + corners
        if line == 0: # If its first line so we dont have anything above
            break       
        if start == 0 and i == 0: # if we start from the left 
            continue              # then we dont have left corner so hop to the next one     
        if end == (len(content) - 1) and i == (length+1): # finish if we will go too far away
            break
        if content[line-1][start - 1 + i] in symbols: # -1 to not start above but from corner
            return True, number
    
    # If it doesnt return anything then check left side
    if start != 0:
        if content[line][start-1] in symbols:
            return True, number
    
    # Same for the right side
    if end != len(content[line]) - 1:
        if content[line][end+1] in symbols:
            return True, number
    
    #and similarly for the bottom line
    for i in range(length + 2): # below + corners
        if line == len(content) - 1: # If its last line so we dont have anything below
            break       
        if start == 0 and i == 0: # if we start from the left 
            continue              # then we dont have left corner so hop to the next one      
        if end == len(content)-1 and i == (length+1): # finish if we will go too far away
            break   
        if content[line+1][start - 1 + i] in symbols: # -1 to not start above but from corner
            return True, number
    
    #If we didnt find anything just return false
    return False, number
        

    
for i in range(len(content)):
    start = -1
    end = -1
    for x, char in enumerate(content[i]):
        if char.isdigit():
            if start == -1:
                start = x
                continue
            else:
                end = x
                if x != len(content[i]) - 1:
                    continue
        if end == -1:
            end = start
        if start != (-1) and end != (-1):
            adj, number = is_adjacent(start, end, i)
            if adj:              
                parts_sum += number
        start = -1
        end = -1

print(parts_sum)    


