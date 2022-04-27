from typing import Text
import numpy as np
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle
from PIL import Image
import matplotlib.pyplot as plt
#make_blobs
centers = [[5, 1], [-3, -1], [1, -1], [-3, 2],[4,7],[8,2]]
X, _ = make_blobs(n_samples=800, centers=centers, cluster_std=0.6)
bandwidth = estimate_bandwidth(X, quantile=.1,#Mean-Shift Clustering#bandwidth 
n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
clusters = labels.max()+1
plt.figure(2)
plt.clf()


color = cycle('rgbcmyk')
for i, col in zip(range(clusters), color):
    my_members = labels == i
    cluster_center = cluster_centers[i]
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1],
    'o', markerfacecolor=col,
    markeredgecolor='k', markersize=12)
print('Estimated clusters:: %d' % clusters)
plt.show()

