from bioscience.base import *

import sys
import os
import threading
import warnings
import numpy as np
from numba import cuda, njit, NumbaWarning, set_num_threads, prange

def processBcca(dataset, correlationThreshold, minCols, deviceCount, mode, debug):
    
    oModel = None
    if (0.0 <= correlationThreshold <= 1.0 and minCols >= 2):
        
        sMode = ""
        if mode == 2: # NUMBA: CPU Parallel mode
            # To be developed
            sMode = "NUMBA - CPU Parallel mode (to be developed)"
        elif mode == 3: # NUMBA: GPU Parallel mode
            # To be developed
            sMode = "NUMBA - GPU Parallel mode (to be developed)"
        else: # Sequential mode
            oModel = __bccaSequential(dataset, correlationThreshold, minCols, debug)
            deviceCount = 0
            sMode = "CPU Sequential"
    
    return oModel

#############################
# BCCA sequential algorithm #
#############################
def __bccaSequential(dataset, correlationThreshold, minCols, debug):
    
    oBCCA = BiclusteringModel()  
    
    rows, cols = dataset.data.shape   
    for i in range(rows):
        for j in range(i + 1, rows):
            print(i," - ",j)
            cols = np.arange(cols, dtype=np.int64)
            corr = _corr(dataset.data[i], dataset.data[j])
            
            while corr < correlationThreshold and len(cols) >= minCols:
                cols = np.delete(cols, _find_max_decrease(dataset.data[i], dataset.data[j], cols))
                corr = _corr(dataset.data[i, cols], dataset.data[j, cols])
            
            if len(cols) >= minCols:
                rows = [i, j] + [k for k in range(rows-1) if k not in (i, j) and all(_corr(r, dataset.data[k, cols-1]) >= correlationThreshold for r in dataset.data[rows-1, cols-1])]
                b = Bicluster(rows, cols)
                if not any(np.array_equal(b.rows, bi.rows) and np.array_equal(b.cols, bi.cols) for bi in oBCCA.results):
                    oBCCA.results.add(b)
    
    return oBCCA
        
def _find_max_decrease(ri, rj, indices):
        return max(range(len(indices)), key=lambda k: _corr(np.delete(ri, indices[k]), np.delete(rj, indices[k])))
    
def _corr(v, w):
        vc, wc = v - np.mean(v), w - np.mean(w)
        return np.abs(np.sum(vc * wc) / np.sqrt(np.sum(vc * vc) * np.sum(wc * wc)))