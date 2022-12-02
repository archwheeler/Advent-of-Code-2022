from functools import reduce

def calculate_calorie_sums(calorie_counts):
    return [sum(calorie_count) for calorie_count in calorie_counts]

with open("inputs/day01_calorie_counts.txt", "r") as calorie_counts_file:
    calorie_counts = reduce(
        lambda calorie_counts, line_entry: (
            calorie_counts[:-1] + [(calorie_counts[-1] + [int(line_entry)])]
            if line_entry != "\n"
            else calorie_counts + [[]]
        ),
        calorie_counts_file.readlines(),
        [[]],
    )

    calorie_sums = calculate_calorie_sums(calorie_counts)

    top_calorie_sum = max(calorie_sums)
    print(f"Part 1: {top_calorie_sum}")

    top_three_calorie_sum = sum(sorted(calorie_sums)[-3:])
    print(f"Part 2: {top_three_calorie_sum}")
