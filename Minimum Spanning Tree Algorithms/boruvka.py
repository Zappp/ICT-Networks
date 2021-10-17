class Tree:
    def __init__(self):
        self.number_of_nodes = 0
        self.nodes = []


    def add_node(self, node):
        self.nodes.append(node)
        self.number_of_nodes += 1
    #
    # def print(self):
    #     weight = 0
    #     for edge in self.edges:
    #         print("Node1 : {}, Node2 : {}, Weight : {}".format(edge.node1.name,edge.node2.name,edge.weight))
    #         weight += edge.weight
    #     print("weight : ", weight)


class Node:
    def __init__(self, name):
        self.name = name
        self.parent_tree = None
        self.number_of_edges = 0
        self.edges = [] # zbior krawiedzi dla wezla, format klasy

    def add_parent(self, parent_t): # dodaje info ze jest w jakims drzewie
        self.parent_tree = parent_t

    def join_edge(self, edge): # dodaje krawedz do zbioru krawedzi
        self.edges.append(edge)
        self.number_of_edges += 1


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight




Trees = []
general_edges = []
general_nodes = {}
used_connections = []


# initialize

def initialize(edges, nodes):
    for node_ in nodes.values():
        Trees.append(Tree())
        Trees[-1].add_node(node_)
        node_.add_parent(Trees[-1])
        [node_.join_edge(x) for x in edges if x.node1.name == node_.name or x.node2.name == node_.name]

# Boruvka

def Boruvka():
    while len(Trees)>1:
        # print("###########################################")
        # print("###########################################")
        # for Tree_ in Trees:
        #     for node_ in Tree_.nodes:
        #         print("Node :", node_.name)
        #         for edge_ in node_.edges:
        #             print("Edge : {} - {} : {}".format(edge_.node1.name, edge_.node2.name, edge_.weight))
        #     print("######       #####       #####       #####")

        best_connections = []
        for Tree_ in Trees:
            for node_ in Tree_.nodes:
                edge_best = Edge(None, None, None)
                for edge_ in node_.edges:
                    if edge_best.weight == None:
                        edge_best = edge_
                    elif edge_best.weight > edge_.weight and (edge_.node1 not in Tree_.nodes or edge_.node2 not in Tree_.nodes ):
                        edge_best = edge_

            best_connections.append(edge_best)


        # for best connections create new Trees from old parents
        # delete old Trees
        # change parrents

        for edge_ in best_connections:
            Trees.append(Tree())
            for node_ in edge_.node1.parent_tree.nodes:
                if node_ not in Trees[-1].nodes:
                    Trees[-1].add_node(node_)
            for node_ in edge_.node2.parent_tree.nodes:
                if node_ not in Trees[-1].nodes:
                    Trees[-1].add_node(node_)
            if edge_.node1.parent_tree in Trees:
                Trees.remove(edge_.node1.parent_tree)
            if edge_.node2.parent_tree in Trees:
                Trees.remove(edge_.node2.parent_tree)
            for node_ in Trees[-1].nodes:
                node_.add_parent(Trees[-1])

        used_connections.append(best_connections)


def print_edges(edges_):
    weight=  0
    new_edges = []
    for es in edges_:
        for edge in es:
            if edge not in new_edges:
                new_edges.append(edge)

    for edge in new_edges:
        print("Node1 : {}, Node2 : {}, Weight : {}".format(edge.node1.name,edge.node2.name,edge.weight))
        weight += edge.weight
    print("weight : ", weight)


print("Give edges like (Node1, Node2, weight)")
print("Give number of edges first : ")

count = int(input())
import numpy as np

while count != 0:
    a = int(input())
    b = int(input())
    c = int(input())

    if a in general_nodes.keys(): # zamiana inta na klase
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


initialize(general_edges, general_nodes)

# print(len(Trees))
#
# print("##################")

Boruvka()
#
# print("##################")

print_edges(used_connections)


