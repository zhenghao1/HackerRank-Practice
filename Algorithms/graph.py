# DFS of Graph
from typing import List

class Solution:

    def dfsOfGraph(self, V: int, adj: List[List[int]]):
        visited = []
        start = 0
        result = self.dfsUtil(adj, start, visited)
        return result

    def dfsUtil(self, adj: List[List[int]], start: int, visited: List[int]):
        visited.append(start)
        #print(start, end=' ')
        for neighbour in adj[start]:
            if neighbour not in visited:
                self.dfsUtil(adj, neighbour, visited)
        return visited

    def printAdjacencyList(self, adj: List[List[int]]):
        print(adj)
        print()


if __name__ == '__main__':
    T = int(input())
    while T>0:
        V,E = map(int, input("Enter number of vertices and number of edges: ").split())
        adj = [[] for i in range(V+1)]
        for i in range(E):
            u,v = map(int, input("Enter the vertice connected to each other: ").split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
        T -= 1

