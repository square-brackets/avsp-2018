import sys
import time

if __name__ == '__main__':
    nodes = []
    queries = []

    n, beta = sys.stdin.readline().split(' ')
    n = int(n)
    beta = float(beta)

    destination_nodes = [[] for _ in range(n)]
    ds = []

    for i in range(n):
        node_counter = 0
        for node in sys.stdin.readline().split(' '):
            node_int = int(node)
            destination_nodes[node_int].append(i)
            node_counter += 1
        ds.append(node_counter)

    q = int(sys.stdin.readline())
    max_step = 0
    query_steps = []
    for i in range(q):
        ni, ti = sys.stdin.readline().split(' ')
        ni = int(ni)
        ti = int(ti)
        max_step = max(max_step, ti)
        query_steps.append(ti)
        queries.append(ni)

    r = [1 / n] * n
    results = [0] * q
    current_step = 1
    while current_step <= max_step:
        s = 0
        r_old = r[:]
        for j in range(n):
            r[j] = sum([beta * r_old[i] / ds[i] for i in destination_nodes[j]])
            s += r[j]
        for j in range(n):
            r[j] += (1 - s) / n

        for i in range(q):
            if query_steps[i] == current_step:
                results[i] = r[queries[i]]

        current_step += 1

    for result in results:
        # print(round(result), 10)
        print("{:05.10f}".format(result))
