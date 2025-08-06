from Queue import Queue
from Stack import Stack

class DirectedGraph:
    #Creates a graph from the provided list of tuples.
    def __init__(self,tupleList = None):
        self.__dict = {}
        self.__vertexSet = set()
        if(tupleList != None):
            for (fst,snd) in tupleList:
                self.addEdge((fst,snd))
    
    #Using set here implies that there cannot be two edges between the same two points.
    def addEdge(self,edge):
        if(edge[0] not in self.__dict.keys()):
            self.__dict[edge[0]] = set()
            self.__dict[edge[0]].add(edge[1])
            self.__vertexSet.add(edge[0])
            self.__vertexSet.add(edge[1])
        else:
            self.__dict[edge[0]].add(edge[1])
            self.__vertexSet.add(edge[1])
    
    @staticmethod
    def bfs(graph):
        visited = set()
        for key in graph.__dict.keys():
            if(key not in visited):
                DirectedGraph.bfsFromVertex(graph,key,visited)
    
    @staticmethod
    def bfsFromVertex(graph,val,visited):
        visited.add(val)
        print(val)
        q = Queue()
        q.enqueue(val)
        while(not q.isEmpty()):
            v = q.dequeue()
            if(v in graph.__dict.keys()):
                for adjV in graph.__dict[v]:
                    if(adjV not in visited):
                        print(adjV)
                        visited.add(adjV)
                        q.enqueue(adjV)

    
    #Prints the graph:
    def printGraph(self):
        print(self.__dict)


if __name__ == '__main__':
    g = DirectedGraph([(1,2),(2,3),(3,4),(1,2)])
    DirectedGraph.bfs(g)
    g.printGraph()