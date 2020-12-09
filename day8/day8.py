instructions = [line.replace('\n', '') for line in open("./day8.txt", 'r').readlines() if line != '']

cur_ind = 0
ind_ran = []
accum = 0

def process(accum, index, instructions):
    instruction = instructions[index]
    ins, val = instruction.split(" ")
    if ins == 'jmp': index += int(val)

    if ins == 'acc':
        accum += int(val)
        index += 1

    if ins == 'nop': index += 1

    return index, accum

while True:
    if cur_ind not in ind_ran:
        ind_ran.append(cur_ind)
        cur_ind, accum = process(accum, cur_ind, instructions)

    if cur_ind in ind_ran:
        print(accum)
        print(cur_ind)
        print(ind_ran)
        break

    if cur_ind + 1 > len(instructions):
        print(accum)
        break
