data = [i.replace('\n', '') for i in open("./day2.txt", 'r').readlines()]
data_pre = [{'low': int(row.split('-')[0]), 'high': int(row.split('-')[1].split(' ')[0]),
'letter': row.split(': ')[0].split(' ')[1], 'pass': row.split(': ')[1]} for row in data]

final_list = []
for row in data_pre:
    len_letters = 0
    for letter in row['pass']:
        if letter == row['letter']:
            len_letters += 1

    if len_letters >= row['low'] and len_letters <= row['high']:
        final_list.append(row)

print(f"Found {len(final_list)} passwords in accordance with the policy.")
