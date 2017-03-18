class DirectedGraph:
    #Creates a graph from the provided list of tuples.
    def __init__(self,tupleList = None):
        self.__dict = {}
        if(tupleList != None):
            for (fst,snd) in tupleList:
                self.addVertex(fst)
                self.addEdge((fst,snd))
    
    def addVertex(self,vertex):
        if(self.__dict.get(vertex,True)):
            self.__dict[vertex] = []
    
    def addEdge(self,edge):
        self.addVertex(edge[0])
        if(edge[1] not in self.__dict[edge[0]]):
            self.__dict[edge[0]].append(edge[1])
    
    #Prints the graph:
    def printGraph(self):
        print(self.__dict)


if __name__ == '__main__':
    g = DirectedGraph([(1,2),(2,3),(3,4),(1,2)])
    g.printGraph()