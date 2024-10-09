from sklearn.datasets import make_blobs, make_moons, make_circles

def generate_datasets():
    datasets = {
        'blobs': make_blobs(n_samples=1000, centers=3, random_state=42),
        'moons': make_moons(n_samples=1000, noise=0.1, random_state=42),
        'circles': make_circles(n_samples=1000, noise=0.1, factor=0.5, random_state=42)
    }
    return datasets
