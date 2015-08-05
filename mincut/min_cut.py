import sys
import random
from math import log
from copy import deepcopy

def form_adjacency_list(file_url):
    graph = dict()
    f = open(file_url, 'r')
    for line in f:
        data = [int(x) for x in line.strip().split()]
        graph[data[0]] = data[1:]
    return graph

def random_contract(graph):
    while len(graph) > 2:
        v1 = random.choice(graph.keys())
        v2 = random.choice(graph[v1])
        edge = (v1, v2,) 
        contract(edge, graph)
    return len(graph.values()[0])

def contract(edge, graph):
    graph[edge[1]].extend(graph[edge[0]])
    for vertex in graph[edge[0]]:
        graph[vertex].remove(edge[0])
        graph[vertex].append(edge[1])
    graph[edge[1]] = [x for x in graph[edge[1]] if x != edge[1]]
    del(graph[edge[0]])

def min_cut(graph):
    min_cut = sys.maxint 
    n = len(graph)
    iters = n * int(log(n, 2))
    for i in xrange(iters):
        copy_graph = deepcopy(graph)
        new_cut = random_contract(copy_graph)
        min_cut = new_cut if new_cut < min_cut else min_cut
    return min_cut

def main():
    try:
        file_url = sys.argv[1]
    except Exception as e:
        print('Usage: python min_cut.py <file_url>')
        file_url = 'kargerMinCut.txt'
    graph = form_adjacency_list(file_url)
    print 'Min cut found: {}'.format(min_cut(graph))

if __name__ == "__main__":
    sys.exit(main())
