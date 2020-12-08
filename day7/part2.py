with open("./day7.txt", "r") as file: input_text = file.read()
rules_raw, rules = (input_text.split("\n"), {})
for rule_raw in rules_raw[:-1]:
    subject, targets_raw = rule_raw.split(" bags contain ")
    #Process target
    targets = [target.strip(".").strip("bag").strip("bags").strip() for target in targets_raw.split(", ") if not target.startswith("n")]
    rules[subject] = {"children": [{"colour":target[2:],"amount":int(target[0])} for target in targets]}
def find_children(rules, colour):
    return rules[colour]["children"]

def count_children(rules, colour):
    count = 0
    n_count = 0
    for c in find_children(rules, colour):
        count += 1 * c["amount"]
        n_count += count_children(rules, c["colour"]) * c["amount"]
    return count + n_count

print(count_children(rules, "shiny gold"))

# Higher than 26044




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
