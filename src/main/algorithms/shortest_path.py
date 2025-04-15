def get_shortest_path(previous: list, start: int, end: int):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return []
