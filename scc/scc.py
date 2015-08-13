import sys
import sys
import resource 

global s, t, explored, leader, finish_time


def graphify(file_url):
    graph = {}
    reverse = {}
    f = open(file_url, 'r')
    for line in f:
        data = [int(x) for x in line.strip().split()]
        for data_point in data:
            if data_point not in graph:
                graph[data_point] = []
            if data_point not in reverse:
                reverse[data_point] = []
        graph[data[0]].append(data[1])
        reverse[data[1]].append(data[0])
    return graph, reverse


def dfs(graph, node, second_run=False):
    global s, t, explored, finish_time, leader
    explored[node] = 1
    for next_node in graph[node]:
        if next_node not in explored:
            dfs(graph, next_node, second_run)
    if second_run:
        leader[node] = s
    else:
        t += 1
        finish_time[t] = node


def dfs_driver(graph, second_run=False):
    global s, t, explored, finish_time
    explored = {}
    s, t = None, 0

    for i in xrange(len(graph), 0, -1):
        if second_run:  # Process in order of finish time from n to 1
            node = finish_time[i]
        else:  # Process from n to 1
            node = i
        if node not in explored:
            s = node
            dfs(graph, node, second_run)


def scc(graph, reverse):
    global finish_time, leader
    finish_time = {}
    leader = {}
    dfs_driver(reverse)
    dfs_driver(graph, True)
    count = {}
    for key, value in leader.iteritems():
        count[value] = count.get(value, 0) + 1
    top_five = sorted(count.values(), reverse=True)[:5]
    return top_five


def main():
    try:
        file_url = sys.argv[1]
    except Exception as e:
        print('Usage: python min_cut.py <file_url>')
        file_url = 'SCC.txts'
    graph_fwd, graph_rev = graphify(file_url)
    return scc(graph_fwd, graph_rev)


if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_STACK, (2**29, 2**30))
    sys.setrecursionlimit(10 ** 6)
    sys.exit(main())