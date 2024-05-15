import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def plot_MSE_histogram(input_data, output_data, title, output_image_file_name):
    MSE_array = []
    N_bins = 100
    for i in range(np.array(input_data.shape)[0]):
        MSE_array.append(mean_squared_error(input_data[i], output_data[i]))
    
    plt.hist(MSE_array, bins=N_bins)
    plt.title(title)
    plt.xlabel("Mean squared error")
    plt.ylabel("Frequency")
    plt.savefig(output_image_file_name)
    plt.show()
    
def compare_MSE_histograms(input_data_1, input_data_2, output_data_1, output_data_2, title, output_image_file_name):
    MSE_array_1 = []
    MSE_array_2 = []
    N_bins = 100
    for i in range(np.array(input_data_1.shape)[0]):
        MSE_array_1.append(mean_squared_error(input_data_1[i], output_data_1[i]))
    for i in range(np.array(input_data_2.shape)[0]):
        MSE_array_2.append(mean_squared_error(input_data_2[i], output_data_2[i]))
    
    plt.hist(MSE_array_1, bins=N_bins, density=True)
    plt.hist(MSE_array_2, bins=N_bins, density=True)
    plt.title(title)
    plt.xlabel("Mean squared error")
    plt.ylabel("Arbitrary units")
    plt.legend(["Not pre-aligned", "Pre-aligned"])
    plt.savefig(output_image_file_name)
    plt.show()

