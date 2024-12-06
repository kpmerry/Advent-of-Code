def extract_environment(filename):
    env = []
    with open(filename, "r") as fin:
        for line in fin:
            env.append(list(line.strip()))
    return env


def part_one(filename):
    env = extract_environment(filename)
    guard = "^"
    queue = []

    for i in range(0, len(env)):
        for j in range(0, len(env[0])):
            if env[i][j] == guard:
                queue.append([i, j])  # row, col

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    direction = 0
    count = 0

    while queue:
        current = queue.pop(0)
        if (
            current[0] < 0
            or current[0] >= len(env)
            or current[1] < 0
            or current[1] >= len(env)
        ):
            break
        env[current[0]][current[1]] = "X"
        try:
            next_cell = [
                current[0] + dirs[direction][0],
                current[1] + dirs[direction][1],
            ]
            if env[next_cell[0]][next_cell[1]] == "#":
                direction += 1
                if direction >= 4:
                    direction %= 4
                queue.append(
                    [current[0] + dirs[direction][0], current[1] + dirs[direction][1]]
                )
            else:
                queue.append(next_cell)
        except:
            break

    for a in range(len(env)):
        for b in range(len(env[0])):
            if env[a][b] == "X":
                count += 1

    return count


def part_two(filename):
    return None


def main():
    print("Day 6:")
    print((part_one("input.txt")))
    print(part_two("example.txt"))


if __name__ == "__main__":
    main()
