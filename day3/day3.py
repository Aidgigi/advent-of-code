map_data = [i.replace('\n', '') for i in open('./day3.txt', 'r').readlines()]


def c_slope(x_shift, y_shift):
    num_trees = 0
    curr_x = 0
    iter = 0

    for row in map_data:
        if iter % y_shift == 0:
            if row[0] == 'x':
                print(f"Encountered {num_trees} trees.")

            if row[curr_x % len(row)] == '#':
                num_trees += 1

            curr_x = curr_x + x_shift
        iter += 1

    return num_trees

print(f"Hit {c_slope(1, 1) * c_slope(3, 1) * c_slope(5, 1) * c_slope(7, 1) * c_slope(1, 2)} trees in total.")
