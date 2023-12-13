file = "day4/day4.txt"

sum = 0

with open(file, "r") as f:
    for line in f:
        line = line.strip()
        wall_split = line.split("|")
        my_numbers = wall_split[1].split(" ")
        for number in my_numbers:
            if number == "" or number == " ":
                my_numbers.remove(number)
        # At this point numbers to check are correctly prepared
        # Let's start with the winning numbers
        card_wins = wall_split[0].split(":")
        winning_numbers = card_wins[1].split(" ")

        for number in winning_numbers:
            if number == "" or number == " ":
                winning_numbers.remove(number)
        
        card_sum = 0 

        for number in winning_numbers:
            if number in my_numbers:
                if card_sum == 0:
                    card_sum = 1
                else:
                    card_sum = card_sum * 2
        
        sum += card_sum

print(sum)