def read_file(filename):
    grid = []
    with open(filename, "r") as fin:
        for line in fin:
            grid.append(line.strip())
    return grid


def find_region(reg_type, point, grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = [point]
    region_points = set()
    region_points.add((point[0], point[1]))
    while queue:
        adjs = []
        x, y = queue.pop(0)
        if visited[x][y] == True:
            continue
        visited[x][y] = True
        for di in dirs:
            adj = x + di[0], y + di[1]
            if (
                adj[0] < 0
                or adj[0] >= len(grid)
                or adj[1] < 0
                or adj[1] >= len(grid[0])
            ):
                continue
            elif grid[adj[0]][adj[1]] != reg_type:
                continue
            adjs.append(adj)
        for adj in adjs:
            region_points.add((adj[0], adj[1]))
        queue.extend(adjs)
    return region_points


def count_edges(point, grid, reg_type):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    adjs = []
    x, y = point
    for di in dirs:
        adj = x + di[0], y + di[1]
        if adj[0] < 0 or adj[0] >= len(grid) or adj[1] < 0 or adj[1] >= len(grid[0]):
            continue
        elif grid[adj[0]][adj[1]] != reg_type:
            continue
        adjs.append(adj)
    return 4 - len(adjs)


def part_one(filename):
    # Not the fastest but produces the right answer!
    grid = read_file(filename)
    regions = []
    total = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            region_type = grid[i][j]
            region = find_region(region_type, [i, j], grid)
            if region in regions:
                continue
            regions.append(region)
    for region in regions:
        perimeter = 0
        for point in region:
            reg_type = grid[point[0]][point[1]]
            perimeter += count_edges(point, grid, reg_type)
        total += perimeter * len(region)
    return total


def part_two(filename):
    grid = read_file(filename)
    regions = []
    total = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            region_type = grid[i][j]
            region = find_region(region_type, [i, j], grid)
            if region in regions:
                continue
            regions.append(region)
    return


def main():
    print(part_one("example.txt"))
    print(part_two("example.txt"))


if __name__ == "__main__":
    main()
