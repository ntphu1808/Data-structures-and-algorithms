class Graph:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self, vertex):
        if vertex in self.adj_list:  # check whether the vertex exists in the adj_list or not, this is O(1) because looking up the key in a dictionary is always O(1).
            return False
        self.adj_list[vertex]=[]
        return True

    def add_edge(self, vertexA, vertexB):
        if vertexA in self.adj_list and vertexB in self.adj_list and vertexB!=vertexA:
            for edge in self.adj_list[vertexA]:  #iterate through the list of edges to find out if the vertexB we want to connect with vertexA is already exist or not
                if vertexB==edge: # if it's already been there. return False.
                    return False
            self.adj_list[vertexA].append(vertexB)
            self.adj_list[vertexB].append(vertexA)
            return True
        return False

    def remove_edge(self, vertexA, vertexB):
        try:
            self.adj_list[vertexA].remove(vertexB)
            self.adj_list[vertexB].remove(vertexA)
            return True
        except ValueError:
            return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:    #we only remove the vertex if it exists in the self.adj_list
            for edge in self.adj_list[vertex]:   # loop through the edges list of the vertex.
                self.adj_list[edge].remove(vertex)    #remove all the connection between the current vertex with the other vertices
            self.adj_list.pop(vertex)         #finally, remove the current vertex.
            return True
        return False

gra=Graph()
gra.add_vertex("A")
gra.add_vertex("B")
gra.add_vertex("C")
gra.add_vertex("D")
gra.add_vertex("E")
gra.add_edge("A", "B")
gra.add_edge("A", "C")
gra.add_edge("B", "C")
gra.add_edge("B", "D")
gra.add_edge("D", "C")

gra.remove_vertex("E")

print(gra.adj_list)
