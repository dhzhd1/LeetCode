def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    edge_count = 0
    width = len(grid[0])
    height = len(grid)
    for i in xrange(height):
        for j in xrange(width):
            if grid[i][j] == 1:
                if i == 0:
                    edge_count += 1
                if i == height - 1:
                    edge_count += 1
                if j == 0:
                    edge_count += 1
                if j == width - 1:
                    edge_count += 1

                if i - 1 >= 0 and grid[i-1][j] == 0:
                    edge_count += 1
                if i + 1 < height and grid[i+1][j] == 0:
                    edge_count += 1
                if j - 1 >= 0 and grid[i][j-1] == 0:
                    edge_count += 1
                if j + 1 < width and grid[i][j+1] == 0:
                    edge_count += 1

    return edge_count

if __name__ == "__main__":
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    print(islandPerimeter(grid))
    grid = [[1,0]]
    print(islandPerimeter(grid))