def extract_environment(filename):
    """Extract input file information."""
    env = []
    with open(filename, "r") as fin:
        for line in fin:
            env.append(list(line.strip()))
    return env


def mark_path(env):
    guard = "^"
    queue = []

    # Find starting position.
    for i in range(0, len(env)):
        for j in range(0, len(env[0])):
            if env[i][j] == guard:
                queue.append([i, j])  # row, col

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    direction = 0

    # Visit each point in route and mark in environment with an "X".
    while queue:
        current = queue.pop(0)
        env[current[0]][current[1]] = "X"

        next_cell = [
            current[0] + dirs[direction][0],
            current[1] + dirs[direction][1],
        ]
        # If route will go off grid, end the loop.
        if (
            next_cell[0] < 0
            or next_cell[0] >= len(env)
            or next_cell[1] < 0
            or next_cell[1] >= len(env)
        ):
            break
        # If the route hits an obstacle, shift direction clockwise.
        elif env[next_cell[0]][next_cell[1]] == "#":
            direction += 1
            if direction >= 4:
                direction %= 4
        queue.append([current[0] + dirs[direction][0], current[1] + dirs[direction][1]])
    return env


def is_valid(env, point):
    if point[0] < 0 or point[1] < 0 or point[0] >= len(env) or point[1] >= len(env[0]):
        return False
    return True


def identify_cycle(env, point):
    if not is_valid(env, point) or env[point[0]][point[1]] == "#":
        return False
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    slow, fast = point, point

    for i in range(len(dirs)):
        di_s, di_f = i, i
        start = point
        env[start[0]][start[1]] = "#"

        while is_valid(env, fast):

            next_slow = [slow[0] + dirs[di_s][0], slow[1] + dirs[di_s][1]]
            if not is_valid(env, next_slow):
                break
            elif env[next_slow[0]][next_slow[1]] == "#":
                di_s = (di_s + 1) % 4
                next_slow = [slow[0] + dirs[di_s][0], slow[1] + dirs[di_s][1]]
            slow = next_slow

            for _ in range(2):
                next_fast = [fast[0] + dirs[di_f][0], fast[1] + dirs[di_f][1]]
                if not is_valid(env, next_fast):
                    break
                elif env[next_fast[0]][next_fast[1]] == "#":
                    di_f = (di_f + 1) % 4
                    next_fast = [fast[0] + dirs[di_f][0], fast[1] + dirs[di_f][1]]
            fast = next_fast

            if slow == fast:
                print(point)
                return True

    return False


def part_one(filename):
    """Identify how many distinct cells the path will visit."""
    env = mark_path(extract_environment(filename))

    count = 0

    # Count marked (visited) cells.
    for a in range(len(env)):
        for b in range(len(env[0])):
            if env[a][b] == "X":
                count += 1

    return count


def part_two(filename):
    """Identify where to place obstacles to create a cycling path."""
    environment = mark_path(extract_environment(filename))
    count = 0

    for i in range(len(environment)):
        for j in range(len(environment[0])):
            if environment[i][j] != "X":
                continue
            if identify_cycle([row[:] for row in environment], [i, j]):
                count += 1

    return count


def main():
    print("Day 6:")
    print((part_one("example.txt")))
    res = part_two("example.txt")
    print(res)


if __name__ == "__main__":
    main()
