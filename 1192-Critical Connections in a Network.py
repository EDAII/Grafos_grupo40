class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dis = [0] * n
        low = [0] * n
        self.time = 0
        visited = set()
        output = []
        graph = defaultdict(list)

        for s, t in connections:
            graph[s].append(t)
            graph[t].append(s)

        def dfs(cur, prev):
            visited.add(cur)
            self.time += 1
            dis[cur] = low[cur] = self.time

            for next_node in graph[cur]:
                if next_node not in visited:
                    dfs(next_node, cur)
                    low[cur] = min(low[cur], low[next_node])
                
                    if low[next_node] > dis[cur]:
                        output.append([cur, next_node])
                        
                elif next_node != prev:
                    low[cur] = min(low[cur], dis[next_node])

        dfs(0, -1)
        return output