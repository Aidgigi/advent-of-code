with open("./day6.txt") as file: input_text = file.read()
group_responses, group_counts = ([[y for y in x.split("\n")] for x in input_text.split("\n\n")], [])
for x in group_responses:
    used, count, person_count, res_count = ([],0,0, {})
    for chars in x:
        person_count += 1
        for char in chars:
            if char in used:
                res_count[char] += 1
                continue
            used.append(char)
            res_count[char] = 1
    group_counts.append(sum([1 if y == person_count else 0 for y in res_count.values()]))
print(sum(group_counts))
