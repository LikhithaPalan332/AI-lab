#monkey banana using dfs

start_state = ('A', 'B', False, False)
goal = True

positions = ['A', 'B', 'C'] 

def get_moves(state):
    monkey, box, on_box, has_banana = state
    moves = []


    if not on_box:
        for p in positions:
            if p != monkey:
                moves.append((p, box, False, has_banana))

    if monkey == box and not on_box:
        for p in positions:
            if p != box:
                moves.append((p, p, False, has_banana))
 
    if monkey == box and not on_box:
        moves.append((monkey, box, True, has_banana))

    if monkey == 'C' and on_box and not has_banana:
        moves.append((monkey, box, on_box, True))

    return moves


def dfs(state, visited, path):
    if state[3] == goal: 
        return path + [state]

    visited.add(state)

    for next_state in get_moves(state):
        if next_state not in visited:
            result = dfs(next_state, visited, path + [state])
            if result:
                return result

    return None

solution = dfs(start_state, set(), [])

print("Solution using DFS:\n")
for step, s in enumerate(solution):
    print(f"Step {step}: {s}")
