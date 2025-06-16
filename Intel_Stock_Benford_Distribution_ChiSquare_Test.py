import numpy as np
from modules.benford import *


def main():
    
    # data length   10597
    # data type     np.float64
    intel_stock_data = np.load("data\\Intel_Stock_History_from_1980_03_17.npy")
    
    # data preprocess
    first_numbers = first_num(intel_stock_data)
    number_count = num_count(first_numbers)
    
    chi_square_val = Chi_square_val(number_count, benford()*np.sum(number_count))
    
    p_val = p_value(chi_square_val, 8)
    
    print(p_val)


main()
