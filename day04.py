def check_range_fully_contains_range(range1, range2):
    return (
        range1[0] <= range2[0] and range1[1] >= range2[1] or
        range2[0] <= range1[0] and range2[1] >= range1[1]
    )

def check_range_overlaps_range(range1, range2):
    return (
        range1[0] <= range2[1] and range1[1] >= range2[0] or
        range2[0] <= range1[1] and range2[1] >= range1[0]
    )

with open("inputs/day04_assignments.txt", "r") as assignment_file:
    assignment_list = list(
        map(
            lambda assignment_pair: list(
                map(
                    lambda assignment: [int(section) for section in assignment.split('-')],
                    assignment_pair.split(','),
                ),
            ),
            assignment_file.readlines(),
        )
    )

    number_of_fully_contained_ranges = sum(
        map(
            lambda assignment_pair: check_range_fully_contains_range(*assignment_pair),
            assignment_list,
        )
    )
    print(f"Part 1: {number_of_fully_contained_ranges}")

    number_of_overlapping_ranges = sum(
        map(
            lambda assignment_pair: check_range_overlaps_range(*assignment_pair),
            assignment_list,
        )
    )
    print(f"Part 2: {number_of_overlapping_ranges}")