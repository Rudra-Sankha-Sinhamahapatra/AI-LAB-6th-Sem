import heapq


graph = {
    'Src': [('1', 22), ('2', 21), ('3', 10)],
    '1': [('4', 25), ('5', 24)],
    '2': [('6', 30)],
    '3': [('7', 5), ('8', 12)],
    '6': [('dest', 0)],
}


heuristic = {
    'Src': 20, '1': 22, '2': 21, '3': 10,
    '4': 25, '5': 24, '6': 30, '7': 5, '8': 12,
    'dest': 0
}

def best_first_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        
        print(f"Visiting: {current}")

        if current == goal:
            print("Treasure found at", current)
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    print("Treasure not found!")


best_first_search("Src", "dest")