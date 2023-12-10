file = "day1.txt"

sum = 0

#otwieramy sobie plik
with open(file, "r") as f:
    # czytamy linia po lini
    for line in f:
        # tworzymy dwie zmienne(zerowane co linie) na pierwsza i ostatnia cyfre
        first_d = 0
        last_d = 0
        # Szukamy cyfry w linii, jak znajdziemy to zapisujemy
        # Mnożymy przez 10 no bo to cyfra dziesiatek
        # i konczymy petle
        for letter in line:
            if letter.isdigit():
                first_d = int(letter) * 10
                break
        # To samo robimy tylko od rylu bo szukamy teraz ostatniej
        for letter in reversed(line):
            if letter.isdigit():
                last_d += int(letter)
                break
        #dodajemy je do siebie w kazdej iteracji
        sum += first_d + last_d

print(sum)

