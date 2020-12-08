import re
input = [line.replace('\n', '') for line in open("./day7.txt", 'r').readlines()]
def get_conts(bag):
    cont_string = bag.split("contain ")[1]
    bag_dict = {}
    bag_list = [bag_dict.update({content.strip()[2:]: int(content.strip()[0])}) for content in re.split(" bags, | bag.| bags.| bag, ", cont_string) if (content != '.' and cont_string != "no other bags." and content != '')]
    return bag_dict

data = {}
[data.update({line.split(" bags contain")[0]: get_conts(line)}) for line in input]

def check_conts(bag):
    bag_conts = data[bag]
    print(bag_conts)
    if "shiny gold" in bag_conts:
        return True

    else:
        for b in bag_conts:
            check_conts(b)

"""count = 0
for d in data:
    if check_conts(d): count += 1
print(count)"""

for d in data: print(d)
