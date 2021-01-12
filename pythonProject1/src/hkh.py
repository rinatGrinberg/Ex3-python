
import collections
if __name__ == '__main__':

    def bfs(graph, root):

        visited, queue = set(), collections.deque([root])
        visited.add(root)
        res = []
        while queue:

            # Dequeue a vertex from queue
            vertex = queue.popleft()

            res.append(vertex)
            print(str(vertex) + " ", end="")
            print(res)
            # If not visited, mark it as visited, and
            # enqueue it
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)






    graph = {0: [1, 2], 1: [0], 2: [0], 3: [4], 4:[3],5:[2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 5)






