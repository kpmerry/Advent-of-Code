def read_file(filename):
    """Read the file and return as a grid."""
    env = []
    with open(filename, "r") as fin:
        for line in fin:
            env.append(list(line.strip()))
    return env


def get_adj(point_x, point_y, m, n, env):
    adjacents = []
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # Check all directions.
    for di_x, di_y in dirs:
        next_x, next_y = point_x + di_x, point_y + di_y
        # Don't add to list if out of bounds.
        if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n:
            continue
        adjacents.append([next_x, next_y])

    return adjacents


def bfs(m, n, env, start):
    """Search from a given 0 start point for a 9, return unique start/end pairs."""
    x, y = start
    unique_trails = set()
    # visited = set()

    # BFS.
    queue = []
    queue.append(start)
    while queue:
        cur_x, cur_y = queue.pop(0)
        # visited.add((cur_x, cur_y))
        cur_val = int(env[cur_x][cur_y])
        # If the current is a 9 add to list and continue until queue empty.
        if env[cur_x][cur_y] == "9":
            unique_trails.add(((cur_x, cur_y), (x, y)))
            continue

        adjs = []
        for adj_x, adj_y in get_adj(cur_x, cur_y, m, n, env):
            # Check adjacent hasn't been visited and is correct value.
            # if (adj_x, adj_y) in visited:
            #    continue
            if int(env[adj_x][adj_y]) == (cur_val + 1):
                adjs.append([adj_x, adj_y])
        queue.extend(adjs)

    return len(unique_trails)


def part_one(filename):
    env = read_file(filename)
    # m x n
    m = len(env)
    n = len(env[0])
    # Find the position of the zeros.
    zero_pos = []
    for i in range(m):
        for j in range(n):
            if env[i][j] == "0":
                zero_pos.append([i, j])
    # Use bfs to find the 9s.
    trail_pairs = 0
    for point in zero_pos:
        trails = bfs(m, n, env, point)
        # Add each zero and nine pair.
        trail_pairs += trails

    # Count the length of pairs.
    return trail_pairs


def bfs_path(m, n, env, start):
    """Search from a given 0 start point for a 9, return unique start/end pairs."""
    x, y = start
    unique_trails = []
    # visited = set()

    # BFS.
    queue = []
    queue.append(start)
    while queue:
        # Visit the current.
        cur_x, cur_y = queue.pop(0)
        # visited.add((cur_x, cur_y))
        cur_val = int(env[cur_x][cur_y])
        # If the current is a 9 add to list and continue until queue empty.
        if env[cur_x][cur_y] == "9":
            unique_trails.append(((cur_x, cur_y), (x, y)))
            continue

        adjs = []
        for adj_x, adj_y in get_adj(cur_x, cur_y, m, n, env):
            # Check adjacent hasn't been visited and is correct value.
            # if (adj_x, adj_y) in visited:
            #    continue
            if int(env[adj_x][adj_y]) == (cur_val + 1):
                adjs.append([adj_x, adj_y])
        queue.extend(adjs)

    return len(unique_trails)


def part_two(filename):
    env = read_file(filename)
    # m x n
    m = len(env)
    n = len(env[0])
    # Find the position of the zeros.
    zero_pos = []
    for i in range(m):
        for j in range(n):
            if env[i][j] == "0":
                zero_pos.append([i, j])
    # Use bfs to find the 9s.
    trail_pairs = 0
    for point in zero_pos:
        trails = bfs_path(m, n, env, point)
        # Add each zero and nine pair.
        trail_pairs += trails

    # Count the length of pairs.
    return trail_pairs


def main():
    print("Day 10:")
    print(part_one("input.txt"))
    print(part_two("input.txt"))


if __name__ == "__main__":
    main()
