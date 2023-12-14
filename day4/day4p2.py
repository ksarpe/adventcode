file = "day4/day4p2.txt"

cards = [1 for i in range(186)]


with open(file, "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        wall_split = line.split("|")
        my_numbers = wall_split[1].split(" ")
        for number in my_numbers:
            if number == "" or number == " ":
                my_numbers.remove(number)
        card_wins = wall_split[0].split(":")
        winning_numbers = card_wins[1].split(" ")
        for number in winning_numbers:
            if number == "" or number == " ":
                winning_numbers.remove(number)
        card_sum = 0

        for number in winning_numbers:
            if number in my_numbers:
                card_sum += 1

        for _ in range(cards[i]): # depending on the previous cards amount
            for card in range(card_sum):
                cards[card + 1 + i] += 1

copy_sum = 0

for copy in cards:
    copy_sum += copy

print(copy_sum)