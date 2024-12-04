def read_file(filename):
    info = []
    with open(filename, "r") as fin:
        for line in fin:
            info.append(line.strip())
    return info


def find_words(wordsearch):

    # Where wordsearch is m x n rows x cols.
    m = len(wordsearch)
    n = len(wordsearch[0])

    letter = "X"
    word = "XMAS"

    dirs = [[1, 1], [1, 0], [0, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]
    count = 0

    for i in range(n):
        for j in range(m):
            if wordsearch[i][j] != letter:
                continue
            for di in dirs:
                word_check = ""
                if (i + (3 * di[0])) < 0 or (j + (3 * di[1])) < 0:
                    continue
                try:
                    word_check += wordsearch[i][j]
                    word_check += wordsearch[i + di[0]][j + di[1]]
                    word_check += wordsearch[i + (2 * di[0])][j + (2 * di[1])]
                    word_check += wordsearch[i + (3 * di[0])][j + (3 * di[1])]
                    if word_check == word:
                        count += 1
                except:
                    continue
    return count


def find_cross(wordsearch):

    # Where wordsearch is m x n rows x cols.
    m = len(wordsearch)
    n = len(wordsearch[0])

    count = 0
    word = "MAS"
    letter = "A"

    dirs = [[1, 1], [-1, 1]]

    for i in range(n):
        for j in range(m):
            local_count = 0

            if wordsearch[i][j] != letter:
                continue
            for di in dirs:
                word_check = ""
                if (
                    (i + di[0]) < 0
                    or (i - di[0]) < 0
                    or (j + di[1]) < 0
                    or (j - di[1]) < 0
                ):
                    continue
                try:
                    word_check += wordsearch[i - di[0]][j - di[1]]
                    word_check += wordsearch[i][j]
                    word_check += wordsearch[i + di[0]][j + di[1]]
                except:
                    continue
                if word_check == word or word_check == word[::-1]:
                    local_count += 1
            count += local_count // 2

    return count


def part_one(filename):
    wordsearch = read_file(filename)
    count = find_words(wordsearch)
    return count


def part_two(filename):
    wordsearch = read_file(filename)
    count = find_cross(wordsearch)
    return count


def main():
    print("Day 4:")
    print(part_one("input.txt"))
    print(part_two("input.txt"))


if __name__ == "__main__":
    main()
