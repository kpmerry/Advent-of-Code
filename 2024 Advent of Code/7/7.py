def read_file(filename):
    data = {}
    with open(filename, "r") as fin:
        for line in fin:
            nums = line.strip().split(" ")
            data[nums[0][:-1]] = nums[1:]
    return data


def three_operators_recursive(target, nums, index, value):

    if value == target:
        return True

    if target - value in nums:
        return True
    if target / value in nums:
        return True

    index += 1
    if index == len(nums):
        return False

    return (
        three_operators_recursive(target, nums, index, (value) + int(nums[index]))
        or three_operators_recursive(target, nums, index, (value) * int(nums[index]))
        or three_operators_recursive(target, nums, index, int(str(value) + nums[index]))
    )


def two_operators_recursive(target, nums, index, value):

    if (value) == int(target):
        return True

    index += 1
    if index == len(nums):
        return False

    return two_operators_recursive(
        target, nums, index, (value) + int(nums[index])
    ) or two_operators_recursive(target, nums, index, (value) * int(nums[index]))


def part_one(filename):
    puzzle_dict = read_file(filename)  # Dict of strings.
    count = 0

    for key in puzzle_dict:
        if two_operators_recursive(key, puzzle_dict[key], 0, int(puzzle_dict[key][0])):
            count += int(key)

    return count


def part_two(filename):
    puzzle_dict = read_file(filename)

    count = 0

    for key in puzzle_dict:
        if two_operators_recursive(key, puzzle_dict[key], 0, int(puzzle_dict[key][0])):
            count += int(key)
            continue
        if three_operators_recursive(
            int(key), puzzle_dict[key], 0, int(puzzle_dict[key][0])
        ):
            count += int(key)
            continue

    return count


def main(filename):
    print("Day 7:")
    print(part_one(filename))
    print(part_two(filename))


if __name__ == "__main__":
    main("input.txt")
