totals = 0
for family in [i.split('\n') for i in open('./day6.txt', 'r').read().split("\n\n")]:
    found_letters = set("abcdefghijklmnopqrstuvwxyz")
    for member in family: found_letters = found_letters & set(member)
    totals += len(set(found_letters))
print(totals)
