import numpy as np

def k_means_clustering(points, k, initial_centroids, max_iterations):

    points = np.asarray(points, dtype=float)
    centroids = np.asarray(initial_centroids, dtype=float)

    for _ in range(max_iterations):

        # Compute distances from every point to every centroid
        distances = np.linalg.norm(
            points[:, None] - centroids,
            axis=2
        )

        # Assign each point to the closest centroid
        labels = np.argmin(distances, axis=1)

        # Compute new centroids
        new_centroids = []

        for i in range(k):
            cluster = points[labels == i]

            if len(cluster) == 0:
                new_centroids.append(centroids[i])
            else:
                new_centroids.append(cluster.mean(axis=0))

        new_centroids = np.array(new_centroids)

        # Stop if converged
        if np.allclose(new_centroids, centroids):
            break

        centroids = new_centroids

    return [tuple(c) for c in centroids]