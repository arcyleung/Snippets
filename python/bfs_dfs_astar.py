# Arthur Leung 2019

import numpy as np
import sys
from heapq import *

# Count the number of explored squares using each search algo
explored_bfs = 0
explored_dfs = 0
explored_astar = 0

def bfs(array, start, goal):
    global explored_bfs
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    oheap = []
    heappush(oheap, start)
    while oheap:
        current = heappop(oheap)
        if (current == goal):
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            data.reverse()
            return data
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == "1":
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set:
                continue

            if neighbor not in oheap:
                came_from[neighbor] = current
                explored_bfs += 1
                heappush(oheap, neighbor)

    return False


def dfs(array, start, goal):
    global explored_dfs
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    stack = []
    stack.append(start)
    while stack:
        current = stack.pop()
        if (current == goal):
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            data.reverse()
            return data
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == "1":
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set:
                continue

            if neighbor not in stack:
                came_from[neighbor] = current
                explored_dfs += 1
                stack.append(neighbor)

    return False

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(array, start, goal):
    global explored_astar
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []
    heappush(oheap, (fscore[start], start))
    while oheap:
        current = heappop(oheap)[1]
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            data.reverse()
            return data
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == "1":
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                explored_astar += 1
                heappush(oheap, (fscore[neighbor], neighbor))

    return False

def transform(point):
    # Because for some reason 0,0 is not top left corner
    return (24-point[1], point[0])

def inverse_transform(point):
    # Because for some reason 0,0 is not top left corner
    return (point[1], 24-point[0])

def main():
    # Read the walls
    with open("walls.txt", "r") as wallsFile:
            walls = [line.split() for line in wallsFile]
    walls = np.array(walls)

    # All hardcoded coords use 0, 0 at bottom left
    start = input("Enter start coords: x, y ")
    end = input("Enter end coords: x, y ")
    # start = transform((2, 11))
    # end = transform((23, 19))

    tf_start = transform(start)
    tf_end = transform(end)

    # List of tuples representing a path from start to end
    path_bfs = bfs(walls, transform(start), transform(end))
    path_dfs = dfs(walls, transform(start), transform(end))
    path_astar = astar(walls, transform(start), transform(end))

    if (path_bfs == False):
        print("No path found")
        return

    sol_bfs = walls.copy()
    sol_dfs = walls.copy()
    sol_astar = walls.copy()

    # Label path
    for i in range(0, len(path_bfs)):
        sol_bfs[path_bfs[i][0]][path_bfs[i][1]] = "."

    for i in range(0, len(path_dfs)):
        sol_dfs[path_dfs[i][0]][path_dfs[i][1]] = "."

    for i in range(0, len(path_astar)):
        sol_astar[path_astar[i][0]][path_astar[i][1]] = "."
    
    # Label start and end nodes
    sol_bfs[tf_start[0]][tf_start[1]] = "S"
    sol_bfs[tf_end[0]][tf_end[1]] = "E"

    sol_dfs[tf_start[0]][tf_start[1]] = "S"
    sol_dfs[tf_end[0]][tf_end[1]] = "E"

    sol_astar[tf_start[0]][tf_start[1]] = "S"
    sol_astar[tf_end[0]][tf_end[1]] = "E"

    with open("sol_bfs_S-" + str(start) + "_E-" + str(end), 'w') as f:
        for l in sol_bfs:
            for n in l:
                f.write(n + " ")
            f.write("\n")
        f.write("Path: " + str([inverse_transform(x) for x in path_bfs]))
        f.write("\n")
        f.write("Cost: "+str(len(path_bfs)))
        f.write("\n")
        f.write("Explored: "+str(explored_bfs))

    with open("sol_dfs_S-" + str(start) + "_E-" + str(end), 'w') as f:
        for l in sol_dfs:
            for n in l:
                f.write(n + " ")
            f.write("\n")
        f.write("Path: " + str([inverse_transform(x) for x in path_dfs]))
        f.write("\n")
        f.write("Cost: "+str(len(path_dfs)))
        f.write("\n")
        f.write("Explored: "+str(explored_dfs))

    with open("sol_astar_S-" + str(start) + "_E-" + str(end), 'w') as f:
        for l in sol_astar:
            for n in l:
                f.write(n + " ")
            f.write("\n")
        f.write("Path: " + str([inverse_transform(x) for x in path_astar]))
        f.write("\n")
        f.write("Cost: "+str(len(path_astar)))
        f.write("\n")
        f.write("Explored: "+str(explored_astar))


if __name__ == '__main__':
    main()