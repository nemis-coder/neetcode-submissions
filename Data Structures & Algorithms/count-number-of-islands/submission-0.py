"""
          i-1,j
   i,j-1  i,j   i,j+1
          i+1,j
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [ [-1,0], [1,0], [0,-1], [0,1]]
        count = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):
            if not((0<=i<n) and (0<=j<m)):
                return 
            if visited[i][j] or grid[i][j]=="0":
                return 
            visited[i][j] = 1
            for direction in directions:
                new_i, new_j = i+direction[0], j+direction[1]
                dfs(new_i,new_j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        return count
        
