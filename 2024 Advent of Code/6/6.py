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


def record_path(env):
    guard = "^"
    queue = []
    data = []
    guard_point = []

    # Find starting position.
    for i in range(0, len(env)):
        for j in range(0, len(env[0])):
            if env[i][j] == guard:
                queue.append([i, j])  # row, col
                guard_point = [i, j]

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    direction = 0

    # Visit each point in route and mark in environment with an "X".
    while queue:
        current = queue.pop(0)
        data.append((current[0], current[1], direction))

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
            direction = (direction + 1) % 4
        queue.append([current[0] + dirs[direction][0], current[1] + dirs[direction][1]])
    return data


def find_cycle(point_data, env, point_before):

    px, py, pdi = point_data
    sx, sy, sdi = point_before
    env[px][py] = "#"
    queue = []

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    di = sdi

    queue.append([sx, sy])
    visited_corners = []

    while queue:
        cx, cy = queue.pop(0)
        if cx < 0 or cx >= len(env) or cy < 0 or cy >= len(env[0]):
            return False
        nx, ny = cx + dirs[di][0], cy + dirs[di][1]
        if nx < 0 or nx >= len(env) or ny < 0 or ny >= len(env[0]):
            return False
        if (nx, ny, di) == (sx, sy, sdi):
            return True
        if (cx, cy, di) in visited_corners:
            return True
        if env[nx][ny] == "#":
            visited_corners.append((cx, cy, di))
            di = (di + 1) % 4
            nx, ny = cx + dirs[di][0], cy + dirs[di][1]
        # Again for corners.
        if env[nx][ny] == "#":
            di = (di + 1) % 4
            nx, ny = cx + dirs[di][0], cy + dirs[di][1]
        if (nx, ny, di) == (px, py, pdi):
            return True
        queue.append([nx, ny])

    return False


def part_two(filename):
    """Identify where to place obstacles to create a cycling path."""
    env = extract_environment(filename)
    path_data = record_path(env)
    count = 0
    for i in range(1, len(path_data)):
        if find_cycle(path_data[i], [row[:] for row in env], path_data[i - 1]):
            count += 1
    return count


def main(filename):
    print("Day 6:")
    print((part_one(filename)))
    res = part_two(filename)
    print(res)


if __name__ == "__main__":
    main("input.txt")
