file = "day5/day5p2.txt"

flag = 1 # 1 -> open for new map, 0 -> new map forbidden
seeds = []
mapping = []

def remap():
    global seeds  # Use global keyword to modify the global variable
    for index, seed in enumerate(seeds):
        for i in range(len(mapping)):
            if seed >= mapping[i][0] and seed <= mapping[i][1]:
                seeds[index] += mapping[i][2]

def get_seeds(seeds_list):
    global seeds

    for seed in seeds_list:
        if seed == "":
            seeds_list.remove(seed)

    current_seed = 0

    for i, seed in enumerate(seed_list):
        if (i+1) % 2 != 0:
            current_seed = int(seed)
        else:
            seeds.append(current_seed)
            seeds.append(current_seed + int(seed) - 1)
    print(seeds)

with open(file, "r") as f:
    for line in f:
        line = line.strip()

        split = line.split(":")
        # One timer, just to get seeds, the rest uses are unnecessary
        if split[0] == "seeds":
            seed_list = split[1].split(" ")
            get_seeds(seed_list)

        if flag == 1:
            mapping = []
        current_split = line.split(" ")
        n = len(current_split)
        if n == 1:
            if flag == 0:
                remap()
            flag = 1
            continue
        elif n == 2:
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
        