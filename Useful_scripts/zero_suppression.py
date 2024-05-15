import numpy as np 
from numpy import random
import matplotlib.pyplot as plt 
from matplotlib import colors

def perform_zero_suppression(data, cutoff):
    data_suppressed = np.zeros(data.shape)
    for i in range(np.array(data.shape)[0]):
        array = data[i]
        for j in range(np.array(array.shape)[0]):
                for k in range(np.array(array.shape)[1]):
                    if array[j][k] > cutoff:
                        data_suppressed[i][j][k] = array[j][k]
                        
    return data_suppressed
        
def histogram_over_images(data):

    for i in range(4):
        arr = data[i].reshape(data.shape()[1], data.shape()[2])
        filtered_arr = arr[arr < 1]
        plt.hist(filtered_arr, bins=100)

    plt.xlabel("Pixel intensity")
    plt.ylabel("Frequency")
    plt.title("Pixel intensity averaged over individual images")
    plt.legend(["Image 0", "Image 1", "Image 2", "Image 3"])
    plt.show()
    
    return None

def plot_before_and_after_suppression(original_data, suppressed_data):

    fig, (ax1, ax2) = plt.subplots(figsize=(13, 3), ncols=2) 

    index = random.randint(0,np.array(original_data.shape)[0])
    min_val = original_data[index].min() 
    max_val = original_data[index].max()
    norm = colors.Normalize(vmin=min_val, vmax=max_val)
    before_suppression = ax1.imshow(original_data[index])
    ax1.set_title("Before")
    before_suppression.set_norm(norm)

    after_suppression = ax2.imshow(suppressed_data[index])
    ax2.set_title("After")
    after_suppression.set_norm(norm)
    fig.suptitle(f"Image {index} before and after zero suppression")
    fig.colorbar(before_suppression, ax=ax1)
    plt.show()
    
    return None

def filter_dataset(data, names, cutoff): # Taken from create_oriented_dataset

    mean_array = np.mean(data, axis=(1, 2))
    mask = mean_array > cutoff
    filtered_array = data[mask]
    filtered_names = names[mask]

    return filtered_array, filtered_names