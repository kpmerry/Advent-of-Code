def read_file(filename):
    info = []
    with open(filename, "r") as fin:
        for line in fin:
            info.append(list(line.strip()))
    return info


def find_words(wordsearch):

    # Where wordsearch is m x n rows x cols
    m = len(wordsearch)
    n = len(wordsearch[0])

    # Conditions: xmas can go across, up/down, diagonally, forwards/backwards.
    # Method: focus on one letter to avoid repeats.
    # Store the number of words each one appears in.

    letter = "x"
    word = "xmas"

    dirs = [[1, 1], [1, 0], [0, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]
    count = 0

    for i in range(m):
        for j in range(n):
            if wordsearch[i][j] != letter:
                continue
            for di in dirs:
                word_check = ""
                try:
                    word_check += wordsearch[i][j]
                    word_check += wordsearch[i + dir[0]][j + dir[1]]
                    word_check += wordsearch[i + (2 * dir[0])][j + (2 * dir[1])]
                    word_check += wordsearch[i + (3 * dir[0])][j + (3 * dir[1])]
                    if word_check == "xmas" or word_check == "samx":
                        count += 1
                except:
                    continue
        return count


def part_one(filename):
    wordsearch = read_file(filename)
    print(wordsearch)
    count = find_words(wordsearch)
    return count


def main():
    print("Day 4:")
    print(part_one("example.txt"))


if __name__ == "__main__":
    main()
