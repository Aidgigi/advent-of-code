totals = 0
for family in [i.split('\n') for i in open('./day6.txt', 'r').read().split("\n\n")]:
    found_letters = []
    for member in family: [found_letters.append(letter) for letter in member if letter not in found_letters]
    totals += len(found_letters)
print(totals)
