def read_file(filename):
    grid = []
    with open(filename, "r") as fin:
        for line in fin:
            grid.append(line.strip())
    return grid


def in_bounds(pair, grid):
    """Count the antinodes in bounds for a pair of nodes."""
    x, y = pair[0]
    a, b = pair[1]

    x_diff = x - a
    y_diff = y - b

    a1 = (x + x_diff, y + y_diff)
    a2 = (a - x_diff, b - y_diff)

    # print(f"The nodes: ({x},{y}) and ({a},{b}) have antinodes {a1} and {a2}.")

    m = len(grid)
    n = len(grid[0])

    in_bounds = set()

    if not (a1[0] < 0 or a1[0] >= n or a1[1] < 0 or a1[1] >= m):
        in_bounds.add(a1)
    if not (a2[0] < 0 or a2[0] >= n or a2[1] < 0 or a2[1] >= m):
        in_bounds.add(a2)

    return in_bounds


def all_in_bounds(pair, grid):
    x, y = pair[0]
    a, b = pair[1]

    x_diff = x - a
    y_diff = y - b

    m = len(grid)
    n = len(grid[0])

    in_bounds = set()

    a1 = [x + x_diff, y + y_diff]

    while a1[0] >= 0 and a1[0] < n and a1[1] >= 0 and a1[1] < m:
        in_bounds.add((a1[0], a1[1]))
        a1[0] += x_diff
        a1[1] += y_diff

    a2 = [a - x_diff, b - y_diff]

    while a2[0] >= 0 and a2[0] < n and a2[1] >= 0 and a2[1] < m:
        in_bounds.add((a2[0], a2[1]))
        a2[0] -= x_diff
        a2[1] -= y_diff

    return in_bounds


def poss_antinodes(nodes, grid):
    nodes.sort(key=lambda x: x[2])

    node_dict = {}

    for data in nodes:
        if data[2] in node_dict:
            (node_dict[data[2]]).append((data[0], data[1]))
        else:
            node_dict[data[2]] = [(data[0], data[1])]

    pairs = []

    for key in node_dict:
        index = 1
        for i in range(len(node_dict[key])):
            for j in range(index, len(node_dict[key])):
                pairs.append((node_dict[key][i], node_dict[key][j]))
            index += 1

    return pairs


def find_nodes(grid):
    # For an m x n (row x col) grid:
    m = len(grid)
    n = len(grid[0])

    nodes = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] != "." and grid[i][j] != "#":
                nodes.append((i, j, grid[i][j]))

    return nodes


def part_one(filename):
    grid = read_file(filename)
    nodes = find_nodes(grid)
    pairs = poss_antinodes(nodes, grid)

    unique_points = set()

    for pair in pairs:
        unique_points.update(in_bounds(pair, grid))

    return len(unique_points)


def part_two(filename):
    grid = read_file(filename)
    nodes = find_nodes(grid)
    pairs = poss_antinodes(nodes, grid)

    unique_points = set()

    for pair in pairs:
        unique_points.update(all_in_bounds(pair, grid))

    print(unique_points)

    return len(unique_points) + len(pairs)


def main(filename):
    print("Day 8:")
    print(part_one(filename))
    print(part_two(filename))


if __name__ == "__main__":
    main("example.txt")
