def extract_readings(filename):
    readings = []
    with open(filename, "r") as fin:
        for line in fin:
            nums = []
            str_list = line.strip().split(" ")
            for i in str_list:
                nums.append(int(i))
            readings.append(nums)
    return readings


def get_diffs(reading):
    diffs = []
    for i in range(len(reading) - 1):
        diff = reading[i] - reading[i + 1]
        diffs.append(diff)
    return check_diffs(diffs)


def check_diffs(diffs):
    pos = []
    neg = []
    # Check diff isn't too big.
    for diff in diffs:
        if diff > 3 or diff < -3 or diff == 0:
            return False
        # Check if all positive.
        elif diff > 0:
            pos.append(diff)
            continue
        # Check if all neg
        elif diff < 0:
            neg.append(diff)
    if pos == [] or neg == []:
        return True
    return False


def count_true(filename):
    count = 0
    readings = extract_readings(filename)
    for reading in readings:
        if get_diffs(reading):
            count += 1
    return count


def check_with_dampener(reading):
    for i in range(len(reading)):
        new = []
        for j in range(len(reading)):
            if j == i:
                continue
            new.append(reading[j])
        if get_diffs(new):
            return True
    return False


def problem_dampener(filename):
    count = 0
    readings = extract_readings(filename)
    for reading in readings:
        if get_diffs(reading):
            count += 1
        elif check_with_dampener(reading):
            count += 1
    return count


def main():
    part1 = count_true("input.txt")
    part2 = problem_dampener("input.txt")
    print(f"Day 2:\n{part1}\n{part2}")


if __name__ == "__main__":
    main()
