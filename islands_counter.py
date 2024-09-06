def islands_counter(grid, N, M):
    CNT = 0
    def cell_exists(x: int, y: int):
        '''
            Check edge conditions
        '''
        if (x > M - 1) or (x < 0) or (y < 0) or (y > N - 1):
            return False
        else:
            return True
    def dfs(x: int, y: int):
        '''
            Depth first search and mark all visited cells, clockwise
        '''
        neighbours_coords = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        for nx, ny in neighbours_coords:
            if cell_exists(nx, ny):
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    dfs(nx, ny)

    for x in range(M):
        for y in range(N):
            if grid[x][y] == 1:
                grid[x][y] = 0
                dfs(x,
                    y)  # brute force depth first search to mark all 1s neighbours as visited, to skip them later
                CNT += 1
    return CNT

def islands_counter_old(grid: list, N: int, M: int) -> int:
    IS_VISITED = [
        [False for i in range(N)] for j in range(M)
    ]
    CNT = 0
    def cell_exists(x: int, y: int):
        '''
            Check edge conditions
        '''
        if (x > M - 1) or (x < 0) or (y < 0) or (y > N - 1):
            return False
        else:
            return True
    def dfs(x: int, y: int):
        '''
            Depth first search and mark all visited cells, clockwise
        '''
        neighbours_coords = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        for nx, ny in neighbours_coords:
            if cell_exists(nx, ny):
                if not IS_VISITED[nx][ny]:
                    if grid[nx][ny] == 1:
                        IS_VISITED[nx][ny] = True
                        dfs(nx, ny)
                    else:
                        IS_VISITED[nx][ny] = True
    for x in range(M):
        for y in range(N):
            if not IS_VISITED[x][y]:  # skip visited cells
                if grid[x][y] == 1:
                    IS_VISITED[x][y] = True
                    dfs(x,
                        y)  # brute force depth first search to mark all 1s neighbours as visited, to skip them later
                    CNT += 1
                if grid[x][y] == 0:
                    IS_VISITED[x][y] = True
    return CNT
