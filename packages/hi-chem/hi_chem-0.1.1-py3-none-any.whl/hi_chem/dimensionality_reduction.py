from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from umap import UMAP
import numpy as np


def tsne_reduce(X: np.ndarray, n_components=2) -> tuple[TSNE, np.ndarray]:
    """
    Performs dimensionality reduction using t-SNE on the input data.

    The function applies t-SNE (t-Distributed Stochastic Neighbor Embedding),
    a nonlinear dimensionality reduction technique, to reduce the dimensions
    of the given high-dimensional data while retaining its significant patterns
    and structures. This is commonly used for visualization purposes or further
    analysis, such as clustering or classification.

    Parameters
    ----------
    X : numpy.ndarray
        The input data array with shape (n_samples, n_features) containing the
        high-dimensional data to be reduced.
    n_components : int, optional
        The number of dimensions to which the data will be reduced. Default is 2.

    Returns
    -------
    tuple[TSNE, numpy.ndarray]
        A tuple containing:
        - The TSNE object used for dimensionality reduction.
        - The transformed data array with reduced dimensions.
    """
    reducer = TSNE(n_components=n_components)
    embedding = reducer.fit_transform(X)
    return reducer, embedding


def pca_reduce(X: np.ndarray, n_components=2) -> tuple[PCA, np.ndarray]:
    """
    Performs Principal Component Analysis (PCA) for dimensionality reduction.

    This function reduces the dimensionality of the given data `X` to the specified
    number of components using PCA. It computes the principal components and returns
    the PCA model and the transformed data.

    Parameters:
        X: np.ndarray
            Input data to be reduced. It should be a 2-dimensional NumPy array.
        n_components: int, optional
            Number of components to reduce the data to. The default is 2.

    Returns:
        tuple[PCA, np.ndarray]
            A tuple containing the trained PCA object and the reduced data as a
            2-dimensional NumPy array.
    """
    reducer = PCA(n_components=n_components)
    embedding = reducer.fit_transform(X)
    return reducer, embedding


def umap_reduce(X: np.ndarray, n_components=2) -> tuple[UMAP, np.ndarray]:
    """
    Apply Uniform Manifold Approximation and Projection (UMAP) dimensionality
    reduction to the provided dataset.

    UMAP is a non-linear dimensionality reduction algorithm commonly used in
    machine learning and data visualization. This function simplifies
    high-dimensional data into a space with fewer dimensions while preserving
    local and global data relationships, making it especially useful for
    visualization or downstream tasks.

    Parameters:
        X: np.ndarray
            The input data to be reduced. It is a two-dimensional array where rows
            represent samples and columns represent features.
        n_components: int
            The number of dimensions to reduce the data to. Default is 2.

    Returns:
        tuple[UMAP, np.ndarray]:
            A tuple containing two elements:
            - A UMAP object (the reducer) fitted to the input data.
            - A NumPy array with the reduced representation of the input data.
    """
    reducer = UMAP(n_components=n_components)
    embedding = reducer.fit_transform(X)
    return reducer, embedding
