import numpy as np
from sklearn.metrics import silhouette_score, adjusted_rand_score, normalized_mutual_info_score

def evaluate_clustering(data, labels_true, labels_pred):
    if len(set(labels_pred)) < 2:
        return None, adjusted_rand_score(labels_true, labels_pred), normalized_mutual_info_score(labels_true, labels_pred)

    silhouette = silhouette_score(data, labels_pred)
    ari = adjusted_rand_score(labels_true, labels_pred)
    nmi = normalized_mutual_info_score(labels_true, labels_pred)
    return silhouette, ari, nmi
