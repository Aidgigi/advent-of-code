import re

file_data = open("./day4.txt", 'r').read()
data = [i for i in file_data.split('\n\n')]
data = [re.split("\n| ", i) for i in data]

new_dat = []

for row in data:
    new_dat.append([{'key': i.split(':')[0], 'value': i.split(':')[1]}  if i.split(':')[0] != '' else None for i in row])

for row in new_dat:
    if row[-1] == None:
        del row[-1]

num_inv = 0
for row in new_dat:
    failed = False
    n_row = [k['key'] for k in row]
    n_dict = {}
    for item in row:
        n_dict.update({item['key']: item['value']})

    print(n_dict)

    if len(n_row) <= 7:
        for attr in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if attr not in n_row:
                num_inv += 1
                failed = True
                break

    if not failed:
        if len(n_dict['byr']) != 4:
            num_inv += 1
            continue

        if not 1920 <= int(n_dict['byr']) <= 2020:
            num_inv += 1
            continue

        if not 2010 <= int(n_dict['iyr']) <= 2020:
            num_inv += 1
            continue

        if not 2020 <= int(n_dict['eyr']) <= 2030:
            num_inv += 1
            continue

        if "in" in n_dict['hgt']:
            if not 59 <= int(n_dict['hgt'].split('in')[0]) <= 76:
                num_inv += 1
                continue

        if "cm" in n_dict['hgt']:
            if not 150 <= int(n_dict['hgt'].split('cm')[0]) <= 193:
                num_inv += 1
                continue

        if "cm" not in n_dict['hgt'] and "in" not in n_dict['hgt']:
            num_inv += 1
            continue

        if n_dict['hcl'][0] != "#":
            num_inv += 1
            continue

        if len(n_dict['hcl'].split('#')[1]) != 6:
            num_inv += 1
            continue

        for letter in n_dict['hcl'][1:]:
            if letter.lower() not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                num_inv += 1
                break

        if n_dict['ecl'].lower() not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            num_inv += 1
            continue

        if len(n_dict['pid']) != 9:
            num_inv += 1
            continue


print(f"Found {len(data) - num_inv} valid passports.")
