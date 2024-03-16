def dfs(i, j, grid, visited):
  visited[i][j] = True
  count = 1
  n, m = len(grid), len(grid[0])

  # Traverse across all 4 neighbors
  if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == '0':
      count += dfs(i - 1, j, grid, visited)
  if i + 1 < n and not visited[i + 1][j] and grid[i + 1][j] == '0':
      count += dfs(i + 1, j, grid, visited)
  if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == '0':
      count += dfs(i, j - 1, grid, visited)
  if j + 1 < m and not visited[i][j + 1] and grid[i][j + 1] == '0':
      count += dfs(i, j + 1, grid, visited)

  return count

def numIslands(grid):
  n, m = len(grid), len(grid[0])
  max_size = 0
  visited = [[False] * m for _ in range(n)]

  for i in range(n):
      for j in range(m):
          if grid[i][j] == '1':
              grid[i][j] = '0'
              size = dfs(i, j, grid, visited)
              max_size = max(max_size, size)
              grid[i][j] = '1'  # Restore the original value
              visited = [[False] * m for _ in range(n)]  # Reset visited array

  return max_size

input_grid =[["1","0","1","0","0"],
             ["0","0","1","1","0"],
             ["0","1","1","1","1"],
             ["1","0","1","0","0"]]

print(numIslands(input_grid))
