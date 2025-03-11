import numpy as np, pandas as pd
from gxctmm import log, fit


def main():

    dataset = np.load('tests/sim.npy', allow_pickle=True).item()  # load the dataset
    data = dataset[0]  # get the first dataset
    
    Y = data['Y']  # Cell type pseudobulk
    K = data['K']  # genomic relationship matrix
    ctnu = data['ctnu']  # cell-to-cell variance matrix \delta
    P = data['P']  # cell type proportion matrix

    # run CIGMA
    out, _ = fit.free_HE(Y, K, ctnu, P)
    print(out)


if __name__ == '__main__':
    main()
