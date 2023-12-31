file = "day5/day5.txt"

flag = 1 # 1 -> open for new map, 0 -> new map forbidden
seeds = []
mapping = []

def remap():
    global seeds  # Use global keyword to modify the global variable
    print("calling remap")
    print("mapping:", mapping)
    print("seeds:", seeds)
    for index, seed in enumerate(seeds):
        print("checking seed:", seed)
        for i in range(len(mapping)):
            print(f"checking in mapping: {mapping[i]}")
            if seed >= mapping[i][0] and seed <= mapping[i][1]:
                print("seed before add:", seed)
                seeds[index] += mapping[i][2]
                print("seed after add:", seeds[index])

with open(file, "r") as f:
    for line in f:
        line = line.strip()

        split = line.split(":")
        print("Current split:", split)
        # One timer, just to get seeds, the rest uses are unnecessary
        if split[0] == "seeds":
            seeds_nr = split[1]
            seeds_nr = seeds_nr.split(" ")
            for nr in seeds_nr:
                if nr == "":
                    continue
                seeds.append(int(nr))
            continue
        # getting next lines
        # Current split might me:
        # 0 -> blank line
        # 2 -> new map indicator
        # 3 -> numbers map     
        # If we are now open for a new map then reset previous
        if flag == 1:
            mapping = []
        current_split = line.split(" ")
        n = len(current_split)
        if n == 1:
            print("Found a new line")
            if flag == 0:
                print("Before new line there was mapping, calculating...")
                remap()
            flag = 1
            continue
        elif n == 2:
            print("Setting flag to 0, (busy)")
            flag = 0
            continue
        elif n == 3:
            temp_mapping = [] # [0] -> start_range [1] -> end range, [2] -> how much to add

            length = int(current_split[2]) # how wide the range is (2)
            source_start = int(current_split[1])                  #(98)
            destination_start = int(current_split[0])             #(50)

            temp_mapping.append(source_start) # here we know where to star tchecking
            temp_mapping.append(source_start + length - 1) # here we know where to end checking
            temp_mapping.append(destination_start - source_start) # here we know how much to add/subtract from source numer to get destination

            mapping.append(temp_mapping)
            
print(seeds)
print(min(seeds))
        