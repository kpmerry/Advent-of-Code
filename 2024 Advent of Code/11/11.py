def read_file(filename):
    numbers = []
    with open(filename, "r") as fin:
        data = fin.read().split(" ")
        for entry in data:
            numbers.append(int(entry))
    return numbers


def apply_rules(nums, count):
    if count == 0:
        return len(nums)
    new_nums = []
    for n in range(len(nums)):
        if nums[n] == 0:
            new_nums.append(1)
        elif len(str(nums[n])) % 2 == 0:
            mid = len(str(nums[n])) // 2
            new_nums.extend([int(str(nums[n])[:mid]), int(str(nums[n])[mid:])])
        else:
            new_nums.append(nums[n] * 2024)
    return apply_rules(new_nums, count - 1)


def apply_rules_faster(nums_dict, count):
    if count == 0:
        return nums_dict
    new_nums_dict = {}
    for key in nums_dict:
        if key == 0:
            if 1 in new_nums_dict:
                new_nums_dict[1] += nums_dict[key]
            else:
                new_nums_dict[1] = nums_dict[key]
        elif len(str(key)) % 2 == 0:
            mid = len(str(key)) // 2
            first_half = int(str(key)[:mid])
            second_half = int(str(key)[mid:])
            if first_half in new_nums_dict:
                new_nums_dict[first_half] += nums_dict[key]
            else:
                new_nums_dict[first_half] = nums_dict[key]
            if second_half in new_nums_dict:
                new_nums_dict[second_half] += nums_dict[key]
            else:
                new_nums_dict[second_half] = nums_dict[key]
        else:
            if key * 2024 in new_nums_dict:
                new_nums_dict[key * 2024] += nums_dict[key]
            else:
                new_nums_dict[key * 2024] = nums_dict[key]
    return apply_rules_faster(new_nums_dict, count - 1)


def part_one(filename):
    stones = read_file(filename)
    new_stones = apply_rules(stones, 25)
    return new_stones


def part_two(filename):
    stones = read_file(filename)
    stones_dict = {}
    for number in stones:
        if number in stones_dict:
            stones_dict[number] += 1
        else:
            stones_dict[number] = 1
    new_stones_dict = apply_rules_faster(stones_dict, 75)
    count = 0
    for key in new_stones_dict:
        count += new_stones_dict[key]
    return count


def main():
    print(part_one("input.txt"))
    print(part_two("input.txt"))


if __name__ == "__main__":
    main()
