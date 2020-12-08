with open("./day7.txt", "r") as file: input_text = file.read()
rules_raw, rules = (input_text.split("\n"), {})
for rule_raw in rules_raw[:-1]:
    subject, targets_raw = rule_raw.split(" bags contain ")
    #Process target
    targets = [target.strip(".").strip("bag").strip("bags").strip() for target in targets_raw.split(", ") if not target.startswith("n")]
    rules[subject] = {"children": [{"colour":target[2:],"amount":int(target[0])} for target in targets]}

def find_parents(rules, colour):
    parents = []
    for rule, child in rules.items():
        for c in child["children"]:
            if colour in c["colour"]:
                parents.append(rule)
    return parents

def count_parents(rules, colour, _counted=[]):
    count = 0
    n_count = 0
    for c in find_parents(rules, colour):
        if c in _counted: continue
        _counted.append(c)
        count += 1
        n_count += count_parents(rules, c, _counted)
    print(colour, find_parents(rules, colour))
    return count + n_count

print(count_parents(rules, "shiny gold"))

#mport json
#print(json.dumps(rules, indent=2))

# [adj] [colour] bags contain [amount] [adj] [colour] bags, [amount] [adj] [colour] bags.
# [adj] [colour] bags contain no other bags.

"""
{
    "colour": "",
    "contains": [{
        "colour": "",
        "amount": 0
    }]
}
"""
