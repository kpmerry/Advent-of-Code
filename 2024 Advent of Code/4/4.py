def read_file(filename):
    info = []
    with open(filename, "r") as fin:
        for line in fin:
            info.append(line.strip())
    return info


def find_words(wordsearch):
    count = 0
    # Where wordsearch is m x n rows x cols
    m = len(wordsearch)
    n = len(wordsearch[0])

    # Conditions: xmas can go across, up/down, diagonally, forwards/backwards.
    # Method: focus on one letter to avoid repeats.
    # Store the number of words each one appears in.

    letter = "x"
    word = "xmas"

    dirs = [[1, 1], [1, 0], [0, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]

    return count


def part_one(filename):
    wordsearch = read_file(filename)
    count = find_words(wordsearch)
    return count


def main():
    print("Day 4:")
    print(part_one("example.txt"))


if __name__ == "__main__":
    main()
