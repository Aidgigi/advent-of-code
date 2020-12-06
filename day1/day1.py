expenses_list = open('./day1.txt', 'r').readlines()
expenses_list = [int(i.replace('\n', '')) for i in expenses_list]
print(expenses_list)

for expense in expenses_list:
    for expense2 in expenses_list:
        for expense3 in expenses_list:
            if expense + expense2 + expense3 == 2020:
                print(f"{expense} -- {expense2} -- {expense3}")
