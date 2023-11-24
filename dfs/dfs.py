# Q1. 음료수 얼려먹기

def ice_cream():
    # map(int, input().split())
    n, m = 4, 5

#    for i in range(n):
#        board.append(list(map(int, input())))
    board = []

    board.append(list(map(int, '00110')))
    board.append(list(map(int, '00011')))
    board.append(list(map(int, '11111')))
    board.append(list(map(int, '00000')))

    result = 0

    def dfs(x, y):
        if x < 0 or x == n or y < 0 or y == m:
            return False

        if board[x][y] == 0:
            board[x][y] = 1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True

        return False

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1

    print(result)

# Q2. 미로 탈출

def maze():
    from collections import deque
    # map(int, input().split())
    n, m = 5, 6

    #    for i in range(n):
    #        board.append(list(map(int, input())))
    maze = []

    maze.append(list(map(int, '101010')))
    maze.append(list(map(int, '111111')))
    maze.append(list(map(int, '000001')))
    maze.append(list(map(int, '111111')))
    maze.append(list(map(int, '111111')))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx == n or ny < 0 or ny == m:
                    continue

                if maze[nx][ny] == 0:
                    continue

                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))

    bfs(0, 0)

    print(maze[n - 1][m - 1])

if __name__ == '__main__':
    ice_cream()
    maze()
