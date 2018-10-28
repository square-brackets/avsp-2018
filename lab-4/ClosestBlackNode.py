import sys
import operator

if __name__ == '__main__':
    n, e = sys.stdin.readline().split(' ')
    n = int(n)
    e = int(e)
    nodes = []
    connections = []

    for i in range(n):
        ti = sys.stdin.readline().replace('\n', '')
        nodes.append(ti)
        connections.append([])

    for i in range(e):
        n1, n2 = sys.stdin.readline().split(' ')
        n1 = int(n1)
        n2 = int(n2)
        connections[n1].append(n2)
        connections[n2].append(n1)

    def search(node_index):
        visited = []
        open_list = [(node_index, 0)]
        while len(open_list) > 0:
            current_index, d = open_list.pop(0)

            if current_index in visited:
                continue

            visited.append(current_index)

            if nodes[current_index] == '1':
                return (current_index, d)

            not_visited_neighbours = [neighbor for neighbor in connections[current_index] if neighbor not in visited]
            open_list.extend([(neighbor, d + 1) for neighbor in not_visited_neighbours])
            open_list = sorted(open_list, key=operator.itemgetter(1, 0))
    for i in range(n):
        search_result = search(i)
        if search_result == None:
            print('-1 -1')
        else:
            i, d = search_result
            print(i, d)
