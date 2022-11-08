class Graph:
    def __init__(self):
        self.adjacencyList={}
    def get(self):
        return self.adjacencyList
    def addVertex(self,vertex):
        if vertex in self.adjacencyList.keys():
            return "Vertex Already Exist"
        self.adjacencyList[vertex]=[]
    def addEdges(self,vertex1,vertex2):
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)
    def DFS(self,vertex):
        list=[]
        visited={}

        def traverse(vertex):
            if vertex == None:
                return None
            visited[vertex]=True
            list.append(vertex)

            for neighbor in self.adjacencyList[vertex]:

                if neighbor not in visited.keys():
                    traverse(neighbor)

        traverse(vertex)
        return list

firstGraph=Graph()
firstGraph.addVertex('A')
firstGraph.addVertex('B')
firstGraph.addVertex('C')
firstGraph.addEdges('A','B')
firstGraph.addEdges('C','B')
firstGraph.addEdges('C','A')
print(firstGraph.get())
print(firstGraph.DFS('A'))