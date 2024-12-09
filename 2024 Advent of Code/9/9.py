def part_one(filename):
    data = ""

    with open(filename, "r") as fin:
        for line in fin:
            data += line.strip()

    file_system = ""

    for i in range(len(data)):
        if i % 2 == 0:
            file_system += str(i // 2) * int(data[i])
        else:
            file_system += "." * int(data[i])

    j = len(file_system) - 1
    count = 0
    dot_count = file_system.count(".")

    for index in range(0, len(file_system)):
        # If j is less than current index.
        if (j) < index:
            break
        if file_system[index] == ".":
            while file_system[j] == ".":
                j -= 1
            # If decremented j is less than or equal to index, break.
            if (j) <= index:
                break
            count += index * int(file_system[j])
            j -= 1
            continue
        else:
            count += index * int(file_system[index])

    return count


def main(filename):
    print(part_one(filename))


if __name__ == "__main__":
    main("input.txt")
