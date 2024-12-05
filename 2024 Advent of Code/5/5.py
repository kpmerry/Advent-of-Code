def import_info(filename):
    prerequisites = []
    lists = []
    with open(filename, "r") as fin:
        for line in fin:
            if "|" in line:
                prerequisites.append((line.strip()).split("|"))
            elif line.strip() == "":
                continue
            else:
                lists.append((line.strip()).split(","))
    return prerequisites, lists


def check_line_order(update, prerequisites):
    index_dict = {}

    for i in range(len(update)):
        index_dict[update[i]] = i

    for pair in prerequisites:
        if pair[0] in update and pair[1] in update:
            if index_dict[pair[0]] > index_dict[pair[1]]:
                return False
    return True


def fix_line_order(update, prerequisites):
    order_dict = {}
    n = len(update)
    ordered = [0 for _ in range(n)]

    for i in range(n):
        order_dict[update[i]] = []

    for pair in prerequisites:
        if pair[0] in update and pair[1] in update:
            order_dict[pair[0]].append(pair[1])

    for key in order_dict:
        index = len(order_dict[key])
        ordered.pop(index)
        ordered.insert(index, key)

    return ordered


def part_one(filename):
    order_rules, updates = import_info(filename)
    valid = []
    for update in updates:
        if check_line_order(update, order_rules):
            valid.append(update)

    count = 0

    for valid_update in valid:
        mid = len(valid_update) // 2
        count += int(valid_update[mid])
    return count


def part_two(filename):
    order_rules, updates = import_info(filename)
    invalid_updates = []

    for update in updates:
        if not check_line_order(update, order_rules):
            invalid_updates.append(update)

    fixed = []
    count = 0

    for update in invalid_updates:
        fixed_update = fix_line_order(update, order_rules)
        fixed.append(fixed_update)

    for i in fixed:
        mid = len(i) // 2
        count += int(i[mid])

    return count


def main():
    print("Day 5:")
    print(part_one("input.txt"))
    print(part_two("input.txt"))


if __name__ == "__main__":
    main()
