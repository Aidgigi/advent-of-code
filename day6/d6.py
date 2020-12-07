def part2(groups):
    total = 0
    for group in groups:
        # Use dictionary to count occurrences of letters
        occurrences = {}
        for letter in group:
            if letter not in occurrences:
                occurrences[letter] = 0
            occurrences[letter] +=1

        # By splitting on new-line we get each persons answers.
        person_count = len(group.split('\n'))

        # Filter out letters that occur once per persons in group
        answered_by_all = [x == person_count for x in occurrences.values()]
        total += sum(answered_by_all)
    return total

g = [i for i in open('./day6.txt', 'r').read().split("\n\n")]
print(part2(g))
