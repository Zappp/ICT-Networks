class Tree:
    def __init__(self):
        self.edges = []
        self.number_of_edges = 0

    def join_edge(self, edge):
        self.edges.append(edge)
        self.number_of_edges += 1

    def print_edges(self):
        weight = 0
        for edge in self.edges:
            print("Node1 : {}, Node2 : {}, Weight : {}".format(edge.node1.name,edge.node2.name,edge.weight))
            weight += edge.weight
        print("weight : ", weight)


class Node:
    def __init__(self, name):
        self.name = name
        self.parent_tree = None

    def add_parent(self, parent_t):
        self.parent_tree = parent_t


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


###########################################################################
############################# Kruskal #####################################
###########################################################################

def add_edge(edge):
    """
    different cases for connecting vertexes
    """
    if(edge.node1.parent_tree == None and edge.node2.parent_tree == None):
        Trees.append(Tree())
        Trees[-1].join_edge(edge)
        edge.node1.add_parent(Trees[-1])
        edge.node2.add_parent(Trees[-1])

    elif(edge.node1.parent_tree != None and edge.node2.parent_tree == None):
        edge.node1.parent_tree.join_edge(edge)
        edge.node2.add_parent(edge.node1.parent_tree)

    elif(edge.node1.parent_tree == None and edge.node2.parent_tree != None):
        edge.node2.parent_tree.join_edge(edge)
        edge.node1.add_parent(edge.node2.parent_tree)

    elif edge.node1.parent_tree != edge.node2.parent_tree:
        Trees.append(Tree())

        edges_par1 = edge.node1.parent_tree.edges.copy()
        edges_par2 = edge.node2.parent_tree.edges.copy()

        for edge_ in edges_par1:
            Trees[-1].join_edge(edge_)
            edge_.node1.add_parent(Trees[-1])
            edge_.node2.add_parent(Trees[-1])

        for edge_ in edges_par2:
            Trees[-1].join_edge(edge_)
            edge_.node1.add_parent(Trees[-1])
            edge_.node2.add_parent(Trees[-1])

        Trees[-1].join_edge(edge)


def print_biggest_tree(Trees):
    """
    from all Trees print that which has the highest number of edges
    that will be the MST
    """
    num_edges = -1
    bestTree = None
    for tree in Trees:
        if tree.number_of_edges > num_edges:
            num_edges = tree.number_of_edges
            bestTree = tree

    bestTree.print_edges()



Trees = []
general_edges = []
general_nodes = {}


print("Give edges like (Node1, Node2, weight)")
print("Give number of edges first : ")

count = int(input())
import numpy as np

while count != 0:
    a = int(input())
    b = int(input())
    c = int(input())

    if a in general_nodes.keys():
        a = general_nodes[a]
    else:
        a = Node(a)
        general_nodes.update({a.name : a})

    if b in general_nodes.keys():
        b = general_nodes[b]
    else:
        b = Node(b)
        general_nodes.update({b.name : b})

# edges are defined as a - source, b - destination, c - Weight
# general_edges stores all edges added to our graph
    general_edges.append(Edge(a,b,c))
    count -= 1

# sorting edges by their weight to first consider that with lowest weight
general_edges.sort(key=lambda x : x.weight)


# for each edge lets make some action - try add to MST
for edge_ in general_edges:
    add_edge(edge_)

print_biggest_tree(Trees)