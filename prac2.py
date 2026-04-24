import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {'A': 3, 'B': 1, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Reached:", goal)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight + heuristic[neighbor], neighbor))

astar('A', 'D')
