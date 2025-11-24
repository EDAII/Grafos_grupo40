class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        Node = namedtuple('Node', ['node', 'mask', 'cost'])
        
        qu = deque()
        st = set()

        for i in range(n):
            head = Node(i, (1 << i), 0)
            st.add((i, (1 << i)))
            qu.append(head)

        while qu:
            tup = qu.popleft()

            if tup.mask == ((1 << n) - 1):
                return tup.cost

            for child in graph[tup.node]:
                bitMask = tup.mask | (1 << child)

                if (child, bitMask) not in st:
                    st.add((child, bitMask))
                    qu.append(Node(child, bitMask, tup.cost + 1))

        return -1