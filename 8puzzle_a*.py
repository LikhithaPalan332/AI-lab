# 8 puzzle using A* 

import heapq
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                dist += abs(goal_x - i) + abs(goal_y - j)
    return dist

def neighbors(state):
    x, y = find_zero(state)
    moves = [("Right", 0, 1), ("Down", 1, 0),
             ("Left", 0, -1), ("Up", -1, 0)]
    
    result = []
    for move, dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append((new_state, move))

    return result

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def solve(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, [], []))
    visited = set()

    while pq:
        f, g, current, path, moves = heapq.heappop(pq)

        if current == goal:
            return path + [current], moves

        if to_tuple(current) in visited:
            continue

        visited.add(to_tuple(current))

        for nxt, move in neighbors(current):
            if to_tuple(nxt) not in visited:
                heapq.heappush(pq, (
                    g + 1 + heuristic(nxt),
                    g + 1,
                    nxt,
                    path + [current],
                    moves + [move]
                ))

    return None, None

def print_state(state):
    for row in state:
        print(row)
    print()


start = [[1, 2, 3],
         [5, 0, 6],
         [4, 7, 8]]

states, moves = solve(start)

print("A* Shortest Solution:\n")

for i in range(len(states)):
    print_state(states[i])
    if i < len(moves):
        print("Move:", moves[i])
        print()

print("Goal State Reached!")
