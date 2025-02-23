import math;

def calc_distance_falling(t):
    GRAV_ACCEL = 9.8
    return round(float(0.5 * GRAV_ACCEL * t ** 2), 3)

def get_column(array_2d, col_index):
    col_items = [];

    for row in array_2d:
        col_items.append(row[col_index])
    return col_items


def create_table(headers, rows):
    header_widths = list(map(lambda x: len(x), headers));
    max_column_widths = []

    # determine the max column width for the values.
    for col in range(len(headers)):
        col_nums = get_column(rows, col);
        max_widths = list(map(lambda x: len(str(x)), col_nums))
        max_column_widths.append(max(max_widths[col], header_widths[col]))

    # Create the format string for each row (with dynamic column width)
    row_format = " | ".join([f"{{:<{width}}}" for width in max_column_widths])

    # Print the headers
    print(row_format.format(*headers))
    sep_length = sum(max_column_widths) + len(max_column_widths) * 3 - 1
    print("-" * int(sep_length))  # Print separator

    # Print the rows
    for row in rows:
        print(row_format.format(*[str(value) for value in row]))

    
def main():
    headers = ["Time (s)", "Distance Falled (M)"]
    rows = [];
    for i in range(1,11):
       rows.append([i, calc_distance_falling(i)])
    create_table(headers, rows)

main()