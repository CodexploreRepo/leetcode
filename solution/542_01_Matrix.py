class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        we flip the problem.
        The flipped problem is to start from target (0 - sea) and to figure our the closest source (1 - land)
        This allows us to run a single BFS search that emerges from different places (all the targets aka all the zero cells) in the grid
        Add all the targets (all zero cells) into the queue. While you're at it, also mark those targets as visited (add to a visited set)
        Run a single BFS on the pre-processed queue and investigate neighbours.
        if neighbiour cell has not been visited --> then it must be a land cell (since all the sea cells have been marked visited):
        append the neighbour cell into the queue and mutate the gird
        """
        row, col = len(mat), len(mat[0])

        direction = [(0,-1), (0,1), (-1,0), (1,0)] #Top, Down, Left, Right
        visited, queue = set(), []

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j))

        while(queue):
            i, j = queue.pop(0)
            for d_i, d_j in direction:
                new_i, new_j = i+d_i, j+d_j
                if (new_i >= 0 and new_i < row) and (new_j >= 0 and new_j < col):
                    if (new_i, new_j) not in visited:
                        mat[new_i][new_j] = mat[i][j] + 1
                        visited.add((new_i, new_j))
                        queue.append((new_i, new_j))
        return mat
