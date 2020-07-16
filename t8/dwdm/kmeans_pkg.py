import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.DataFrame(((2, 3), (5, 6), (8, 7), (1, 4), (2, 2), (6, 7), (3, 4), (8, 6)))

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)
labels = kmeans.predict(df)
centroid = kmeans.cluster_centers_
print(centroid)

colmap = {1: 'r', 2: 'g', 3: 'b'}
fig = plt.figure(figsize=(5, 5))
colors = map(lambda x: colmap[x + 1], labels)
color1 = list(colors)

plt.scatter(df[0], df[1], color=color1, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroid):
    plt.scatter(*centroid, color=colmap[idx + 1])
plt.xlim(0, 80)
plt.ylim(0, 80)

plt.show()
