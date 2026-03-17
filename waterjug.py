from collections import deque

capacities = (12,8,5,3)
start = (12,0,0,0)
goal = (6,6,0,0)

def get_moves(state):
    moves = []
    jugs = list(state)

    # empty jug to fountain
    for i in range(4):
        if jugs[i] > 0:
            new = list(jugs)
            amount = new[i]
            new[i] = 0
            moves.append((tuple(new), f"Empty Jug{i+1} ({amount}L) to fountain"))

    # pour from one jug to another
    for i in range(4):
        for j in range(4):
            if i != j and jugs[i] > 0 and jugs[j] < capacities[j]:

                transfer = min(jugs[i], capacities[j] - jugs[j])

                new = list(jugs)
                new[i] -= transfer
                new[j] += transfer

                moves.append((tuple(new),
                f"Pour {transfer}L from Jug{i+1} -> Jug{j+1}"))

    return moves


def bfs():
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            print("\nSolution Found!\n")
            print("Step 0 :", start)

            step = 1
            for action, s in path:
                print(f"Step {step} :", s, "|", action)
                step += 1

            print("\nTotal steps:", step-1)
            return

        for new_state, action in get_moves(state):
            if new_state not in visited:
                queue.append((new_state, path + [(action,new_state)]))


bfs()
