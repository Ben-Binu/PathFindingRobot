import numpy as np
import heapq
import matplotlib.pyplot as plt

maze = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
])

start = (0, 0)   
goal = (4, 4)   


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = maze.shape
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0:
                new_g = g + 1
                new_f = new_g + heuristic((nx, ny), goal)
                heapq.heappush(open_list, (new_f, new_g, (nx, ny), path + [(nx, ny)]))
    return None


path = astar(maze, start, goal)


fig, ax = plt.subplots()
rows, cols = maze.shape


for x in range(rows + 1):
    ax.axhline(x, lw=1, color='gray', zorder=1)
for y in range(cols + 1):
    ax.axvline(y, lw=1, color='gray', zorder=1)


for x in range(rows):
    for y in range(cols):
        if maze[x, y] == 1:
            ax.add_patch(plt.Rectangle((y, x), 1, 1, color='black'))


ax.add_patch(plt.Rectangle((start[1], start[0]), 1, 1, color='green'))
ax.add_patch(plt.Rectangle((goal[1], goal[0]), 1, 1, color='red'))

if path:
    x_coords = [p[1] + 0.5 for p in path]
    y_coords = [p[0] + 0.5 for p in path]
    ax.plot(x_coords, y_coords, color='blue', linewidth=3, zorder=3)
    plt.title("Path Found")
else:
    plt.title("No Path Found ")

ax.set_xlim(0, cols)
ax.set_ylim(rows, 0)
ax.set_aspect('equal')
plt.show()
