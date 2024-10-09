# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering, Birch, DBSCAN
from sklearn_extra.cluster import KMedoids
from generate_data import generate_datasets
from evaluate import evaluate_clustering
from plot_results import plot_results

# Initialize results dictionary
results = {
    'dataset': [],
    'algorithm': [],
    'silhouette': [],
    'ari': [],
    'nmi': []
}

# List of clustering algorithms
clustering_algorithms = {
    'KMeans': KMeans(n_clusters=3, random_state=42, n_init='auto'),
    'KMedoids': KMedoids(n_clusters=3, random_state=42),
    'AGNES': AgglomerativeClustering(n_clusters=3),
    'Birch': Birch(n_clusters=3),
    'DBSCAN': DBSCAN(eps=0.3, min_samples=10)
}

# Generate synthetic datasets
datasets = generate_datasets()

# Perform clustering and evaluation
for dataset_name, (data, labels_true) in datasets.items():
    for algo_name, algorithm in clustering_algorithms.items():
        algorithm.fit(data)
        labels_pred = algorithm.labels_ if hasattr(algorithm, 'labels_') else algorithm.predict(data)

        # Evaluate clustering
        silhouette, ari, nmi = evaluate_clustering(data, labels_true, labels_pred)

        # Store results
        results['dataset'].append(dataset_name)
        results['algorithm'].append(algo_name)
        results['silhouette'].append(silhouette if silhouette is not None else np.nan)
        results['ari'].append(ari)
        results['nmi'].append(nmi)

# Create a DataFrame to display results
results_df = pd.DataFrame(results)
print(results_df)

# Plotting the results
plot_results(results_df)
