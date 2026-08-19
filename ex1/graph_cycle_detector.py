def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    state = {}
    def dfs(node):
        if state.get(node, 0) == 1:
            return True
        if state.get(node, 0) == 2:
            return False
        state[node] = 1
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        state[node] = 2
        return False
    for node in graph:
        if dfs(node):
            return True
    return False

print(graph_cycle_detector(graph = {
}))