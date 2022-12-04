def get_duplicate_item(rucksack_contents):
    section_size = len(rucksack_contents) // 2
    first_section_items = set(rucksack_contents[:section_size])
    second_section_items = set(rucksack_contents[section_size:])
    return list(first_section_items & second_section_items)[0]

def get_item_priority(item):
    return (
        ord(item) - ord('a') + 1
        if item.islower()
        else ord(item) - ord('A') + 27
    )

def get_badge_item(rucksack_contents1, rucksack_contents2, rucksack_contents3):
    return list(set(rucksack_contents1) & set(rucksack_contents2) & set(rucksack_contents3))[0]

with open("inputs/day03_rucksacks.txt", "r") as rucksack_file:
    rucksack_contents_list = rucksack_file.readlines()
    total_priority = sum(
        map(
            lambda rucksack_contents: get_item_priority(
                get_duplicate_item(rucksack_contents.strip())
            ),
            rucksack_contents_list,
        )
    )
    print(f"Part 1: {total_priority}")

    badge_priority_sum = 0
    for elf_group in range(0, len(rucksack_contents_list), 3):
        badge_item = get_badge_item(
            rucksack_contents_list[elf_group].strip(),
            rucksack_contents_list[elf_group+1].strip(),
            rucksack_contents_list[elf_group+2].strip(),
        )
        badge_priority_sum += get_item_priority(badge_item)
    print(f"Part 2: {badge_priority_sum}")
