import numpy as np
import scipy.sparse as sparse
from scipy.sparse import csr_matrix
import os

def perform_sparse_compression(input_path):
    
    # Creates sparse dataset and returns compression ratio
    
    data = np.load(input_path)["data"]
    sparse_data = []
    recovered_data = np.empty(data.shape)
    
    for array in data:
        sparse_data.append(csr_matrix(array))
    sparse_array = sparse.vstack(sparse_data)
    sparse.save_npz("sparse_data.npz", sparse_array)
    
    for i in range(len(sparse_data)):
        recovered_data[i] = sparse_data[i].toarray()
        
    return os.path.getsize(input_path)/os.path.getsize("sparse_data.npz")
