from copy import deepcopy


def assign(dset, clusters):
    for d in dset:
        dist = []
        for c in clusters:
            dist.append(
                ((d[0] - c['centroid'][0]) ** 2 + (d[0] - c['centroid'][0]) ** 2) ** (1 / 2)
            )
        clusters[dist.index(min(dist))]['values'].append(d)


dataset = (
    (2, 3), (5, 6), (8, 7), (1, 4), (2, 2), (6, 7), (3, 4), (8, 6)
)

k = int(input("Enter number of clusters (k) : "))
cluster = list()
for i in range(len(dataset[:k])):
    cluster.append({'centroid': dataset[i], 'values': []})

assign(dataset, cluster)

print("Initial assignment")
print(cluster)

pass_no = 1
prev_cluster = list()

while prev_cluster != cluster:
    prev_cluster = deepcopy(cluster)

    for cl in cluster:
        cl['centroid'] = (
            sum(map(lambda x: x[0], cl['values'])) / len(cl['values']),
            sum(map(lambda x: x[1], cl['values'])) / len(cl['values'])
        )
        cl['values'] = []

    assign(dataset, cluster)

    print("\nAssignment in pass", pass_no)
    print(cluster)
    pass_no += 1
