import math
import numpy as np
from scipy.stats import chi2


def first_num(datas:np.ndarray[np.float64]) -> np.ndarray[np.int32]:
    result = np.array([np.int32(x / (10**int(math.log10(x)))) for x in datas])
    return result


def num_count(datas:np.ndarray[np.int32]) -> np.ndarray[np.int32]:
    result = np.zeros(9, dtype=np.int32)
    for x in datas:
        result[x-1] += 1
    return result


def benford() -> np.ndarray[np.float64]:
    result = np.zeros(9, dtype=np.float64)
    for i in range(1, 10):
        result[i-1] = np.float64(math.log10(1+(1/i)))
    return result


def Chi_square_val(observe_freq:np.ndarray[np.int32], expect_freq:np.ndarray[np.float64]) -> np.float64:
    return np.sum((observe_freq-expect_freq)**2 / expect_freq)


def p_value(chi_val:np.float64, df:int) -> np.float64:
    return np.float64(1 - chi2.cdf(chi_val, df))


def main():
    pass


if __name__ == "__main__":
    main()
    