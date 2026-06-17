def neighbor_joining(dist_matrix, labels, tree, new_label):
    num = len(labels)
    if num == 2:
        a, b = labels[0], labels[1]
        while len(tree) <= max(a, b):
            tree.append([])
        tree[a].append((b, dist_matrix[0][1]))
        tree[b].append((a, dist_matrix[0][1]))
        return tree

    total_dist = [sum(dist_matrix[i][j] for j in range(num) if i != j) for i in range(num)]

    dist_prime = [[0]*num for _ in range(num)]
    smallest = None
    min_a, min_b = None, None
    for a in range(num):
        for b in range(num):
            if a != b:
                dist_prime[a][b] = (num - 2) * dist_matrix[a][b] - total_dist[a] - total_dist[b]
                if smallest is None or dist_prime[a][b] < smallest:
                    smallest = dist_prime[a][b]
                    min_a, min_b = a, b

    a, b = min_a, min_b
    diff = (total_dist[a] - total_dist[b]) / (num - 2)
    len_a = 0.5 * (dist_matrix[a][b] + diff)
    len_b = 0.5 * (dist_matrix[a][b] - diff)

    new_node = new_label[0]
    new_label[0] += 1

    new_dists = []
    for x in range(num):
        if x != a and x != b:
            new_dists.append(0.5 * (dist_matrix[a][x] + dist_matrix[b][x] - dist_matrix[a][b]))

    updated_matrix = []
    new_labels = []
    mapping = {}
    idx = 0
    for x in range(num):
        if x != a and x != b:
            row = []
            for y in range(num):
                if y != a and y != b:
                    row.append(dist_matrix[x][y])
            updated_matrix.append(row)
            new_labels.append(labels[x])
            mapping[x] = idx
            idx += 1

    for idx_x in range(len(new_dists)):
        updated_matrix[idx_x].append(new_dists[idx_x])
    updated_matrix.append(new_dists + [0.0])
    new_labels.append(new_node)

    while len(tree) <= new_node:
        tree.append([])
    neighbor_joining(updated_matrix, new_labels, tree, new_label)

    a_label = labels[a]
    b_label = labels[b]
    while len(tree) <= max(a_label, b_label):
        tree.append([])
    tree[new_node].append((a_label, len_a))
    tree[new_node].append((b_label, len_b))
    tree[a_label].append((new_node, len_a))
    tree[b_label].append((new_node, len_b))

    return tree

if __name__ == "__main__":
    size = int(input())
    dist_matrix = []
    for _ in range(size):
        dist_matrix.append(list(map(int, input().split())))

    labels = list(range(size))
    tree = [[] for _ in range(2 * len(labels) - 1)]
    new_label = [len(labels)]
    neighbor_joining(dist_matrix, labels, tree, new_label)

    n = len(labels)


    edges_set = set()
    for index, neighbors in enumerate(tree):
        for neighbor, length in neighbors:
            if index < neighbor:
                edges_set.add( (index, neighbor, length) )


    sorted_edges = sorted(edges_set, key=lambda x: (x[0], x[1]))
    for index, neighbors in enumerate(tree): 
        d=index
    '''
    for n in range(d):
        for edge in sorted_edges:
            a, b, dist = edge
            print(a,b)
            if (a==n):
                pm.append([a,b,dist])
                print('*')
            if(a!=b) :
                if (b==n):
                    pm.append([b,a,dist])
                    print("**")
    '''

    pm=[]
    for edge in sorted_edges:
        a, b, dist = edge
        pm.append([a,b,dist])

    for edge in sorted_edges:
        a, b, dist = edge
        pm.append([b,a,dist])

    for n in range (d):
        for m in pm:
            if m[0]==n:
                print(f"{m[0]}->{m[1]}:{m[2]:.3f}")