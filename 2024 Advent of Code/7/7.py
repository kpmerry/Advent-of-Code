def read_file(filename):
    data = {}
    with open(filename, "r") as fin:
        for line in fin:
            nums = line.strip().split(" ")
            data[nums[0][:-1]] = nums[1:]
    return data


def check_true(target, nums):

    target = int(target)
    root = int(nums[0])
    stack = [(int(nums[0]), 0)]  # (value, index)

    while stack:
        value, index = stack.pop(0)
        if value == target:
            return True
        next_index = index + 1
        if next_index < len(nums):
            stack.append((value + int(nums[next_index]), next_index))
            stack.append((value * int(nums[next_index]), next_index))

    return False


def part_one(filename):
    puzzle_dict = read_file(filename)  # Dict of strings.
    count = 0

    for key in puzzle_dict:
        if check_true(key, puzzle_dict[key]):
            count += int(key)

    return count


def main():
    print("Day 7:")
    print(part_one("input.txt"))


if __name__ == "__main__":
    main()
