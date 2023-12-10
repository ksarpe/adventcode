d = {"red": 12, "green": 13, "blue": 14}

def get_balls(hand):
    r = g = b = ""
    hand = hand.strip()
    colors = hand.split(",")
    for ball in colors:
        if ball[-1] == "e": # reading from reverse to make it easier
            for char in ball:
                if char.isdigit():
                    b += char
                else:
                    break
        if ball[-1] == "n": 
            for char in ball:
                if char.isdigit():
                    g += char
                else:
                    break
        if ball[-1] == "d":
            for char in ball:
                if char.isdigit():
                    r += char
                else:
                    break
            
    if r == "":
        r = 0
    if g == "":
        g = 0 
    if b == "":
        b = 0
    return int(r), int(g), int(b)

power_sum = 0

with open("day2p2.txt", "r") as f:
    for line in f:
        max_r = max_g = max_b = 0

        game_balls = line.split(":")
        hands = game_balls[1].split(";")

        for hand in hands:
            hand = hand.replace(" ", "")
            red, green, blue = get_balls(hand) # will get balls in one hand by elf, needed for further calculations
            if red > max_r:
                max_r = red
            if green > max_g:
                max_g = green
            if blue > max_b:
                max_b = blue
        
        power_sum += max_r * max_g * max_b

print(power_sum)