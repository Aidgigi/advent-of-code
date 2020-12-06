data = [i.replace('\n', '') for i in open("./day2.txt", 'r').readlines()]
data_pre = [{'ind1': int(row.split('-')[0]), 'ind2': int(row.split('-')[1].split(' ')[0]),
'letter': row.split(': ')[0].split(' ')[1], 'pass': row.split(': ')[1]} for row in data]

final_list = []

for row in data_pre:
    if row['pass'][row['ind1'] - 1] == row['letter'] and not row['pass'][row['ind2'] - 1] == row['letter']:
        final_list.append(row)

    if row['pass'][row['ind2'] - 1] == row['letter'] and not row['pass'][row['ind1'] - 1] == row['letter']:
        final_list.append(row)

print(f"Found {len(final_list)} passwords in accordance with the policy.")
