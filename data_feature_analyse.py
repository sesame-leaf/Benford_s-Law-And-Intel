import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from modules.benford import *


def main():
    
    # load data
    intel_stock_data1 = np.load("data\\Intel_Stock_History_from_1980_03_17.npy")
    intel_stock_data2 = pd.read_csv("data\\intel_stock_data.csv")["Adj_Close"][:len(intel_stock_data1)]
    
    # preprocess data
    first_numbers1 = first_num(intel_stock_data1 * 10)
    number_count1 = num_count(first_numbers1)
    relative_freq1 = number_count1 / np.sum(number_count1)
    
    first_numbers2 = first_num(intel_stock_data2)
    number_count2 = num_count(first_numbers2)
    relative_freq2 = number_count2 / np.sum(number_count2)
    
    # make data Distribution plot
    plt.plot(range(1, 10), relative_freq1, label="Given Data (%)", color="#ff0000")
    plt.plot(range(1, 10), relative_freq2, label="Yahoo Data (%)", color="#0000ff")
    
    # show plot
    plt.legend()
    plt.show()


main()
