instructions = [line.replace('\n', '') for line in open("./day8.txt", 'r').readlines() if line != '']

def process(accum, index, instructions):
    instruction = instructions[index]
    ins, val = instruction.split(" ")
    if ins == 'jmp': index += int(val)

    if ins == 'acc':
        accum += int(val)
        index += 1

    if ins == 'nop': index += 1

    return index, accum

def run_program(instructions):
    cur_ind = 0
    ind_ran = []
    accum = 0
    while True:
        if cur_ind not in ind_ran:
            ind_ran.append(cur_ind)
            cur_ind, accum = process(accum, cur_ind, instructions)

        if cur_ind in ind_ran:
            return 0, accum, cur_ind, ind_ran

        if cur_ind + 1 > len(instructions):
            return 1, accum, cur_ind, ind_ran

def part_two(instructions):
    cur_ind = 0
    ind_ran = []
    accum = 0
    copy = instructions.copy()
    for line in range(1, len(copy)):
        ins, val = instructions[line].split(" ")

        if ins == 'nop':
            ins == 'jmp'

        if ins == 'jmp':
            ins == 'nop'

        copy = instructions.copy()
        copy[line] = f"{ins} {val}"
        valid, accum, x, y = run_program(copy)
        if valid == 1: print(accum)

part_two(instructions)
