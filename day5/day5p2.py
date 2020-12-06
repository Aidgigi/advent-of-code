def process_pass(pass_dat):
    row_data, col_data = pass_dat[:7], pass_dat[-3:]
    rows, cols = [num for num in range(0, 128)], [num for num in range(0, 8)]
    for char in row_data: rows = rows[0:int(len(rows)/2)] if char == 'F' else rows[int(len(rows)/2):len(rows)]
    for char in col_data: cols = cols[0:int(len(cols)/2)] if char == 'L' else cols[int(len(cols)/2):len(cols)]
    return rows[0], cols[0]
seat_ids = [(((e := process_pass(b_pass))[0] * 8) + e[1]) for b_pass in [line.replace('\n', '') for line in open("./day5.txt", 'r').readlines()]]
[print(f"Seat with ID \"{seat}\" is empty!") for seat in range(13, 881) if seat not in seat_ids]
