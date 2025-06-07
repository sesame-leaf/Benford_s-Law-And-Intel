import numpy as np
from modules.benford import *


def main():
    
    # data length   10597
    # data type     np.float64
    intel_stock_data = np.load("data\\Intel_Stock_History_from_1980_03_17.npy")
    first_numbers = first_num(intel_stock_data)
    number_count = num_count(first_numbers)
    
    print(p_value(Chi_square_val(number_count, benford()*np.sum(number_count)), 8))


main()
