import numpy as np
import matplotlib.pyplot as plt
from modules.benford import *


def main():
    
    # load data
    """
        data length   10597
        data type     np.float64
    """
    intel_stock_data = np.load("data\\Intel_Stock_History_from_1980_03_17.npy")
    
    # preprocess data
    first_numbers = first_num(intel_stock_data)
    number_count = num_count(first_numbers)
    relative_freq = number_count / np.sum(number_count)
    
    # make Benford Distribution plot
    plt.plot(range(1, 10), benford()*100, label="Benford Curve (%)", color="#0000ff")
    plt.scatter(range(1, 10), benford()*100, color="#0000ff")
    
    # make data Distribution plot
    plt.plot(range(1, 10), relative_freq*100, label="Intel Stock (%)", color="#ff0000")
    plt.scatter(range(1, 10), relative_freq*100, color="#ff0000")
    
    # make difference between data Distribution and Benford Distribution plot
    plt.plot(range(1, 10), (relative_freq-benford())*100, label="Difference (%p)", color="#00ff00")
    plt.scatter(range(1, 10), (relative_freq-benford())*100, color="#00ff00")
    
    # set plot form
    plt.xlabel("First Digit")
    plt.yticks(range(-5, 41, 5))
    plt.axhline(y=0, color="#000000", linestyle="-", linewidth=1)
    
    # show plot
    plt.legend()
    plt.show()


main()
