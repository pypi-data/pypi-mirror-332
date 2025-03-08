from sklearn import preprocessing
import numpy as np
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

def discretize(dataset, n_bins = 2, strategy = 'kmeans'):
    """
    Discretizes data into N bins.
    
    :param dataset: The dataset object to be discretized.
    :type dataset: :class:`bioscience.base.models.Dataset`
    
    :param n_bins: Number of bins to produce, defaults to 2.
    :type n_bins: int, optional
    
    :param strategy: Strategy used to define the widths of the bins. Options (kmeans, quantile, uniforme). Defaults to 'kmeans'.
    :type strategy: str, optional
        
    """
    if dataset is not None and n_bins > 1:
        dataset.data = np.array(preprocessing.KBinsDiscretizer(n_bins, encode = 'ordinal', strategy = strategy).fit_transform(dataset.data))

def standardize(dataset):
    """
    Standardize a dataset
    
    :param dataset: The dataset object to be standarized.
    :type dataset: :class:`bioscience.base.models.Dataset`
        
    """
    if dataset is not None:
        dataset.data = np.array(preprocessing.StandardScaler().fit_transform(dataset.data))

def scale(dataset):
    """
    Scale a dataset
    
    :param dataset: The dataset object to be scaled.
    :type dataset: :class:`bioscience.base.models.Dataset`
        
    """
    if dataset is not None:
        dataset.data = np.array(preprocessing.MinMaxScaler().fit_transform(dataset.data))

def normalDistributionQuantile(dataset, quantiles = 1000):
    """
    Use Normal Distribution Quantile to preprocess a dataset.
    
    :param dataset: The dataset object to be normal distribution quantile.
    :type dataset: :class:`bioscience.base.models.Dataset`
    
    :param quantiles: Number of quantiles to be computed., defaults to 1000.
    :type quantiles: int, optional        
    """
    if dataset is not None:
        dataset.data = np.array(preprocessing.QuantileTransformer(n_quantiles=quantiles, output_distribution='normal').fit_transform(dataset.data))
        
def outliers(dataset, view=True, mode=1, replace=3):
    """
    Detects and modifies outliers in a dataset.
    
    :param dataset: The dataset object to be checked.
    :type dataset: :class:`bioscience.base.models.Dataset`
    
    :param view: Graphical visualisation through BoxPlot to identify outliers in the columns of the dataset.
    :type view: boolean, optional
    
    :param mode: Type of outlier to be detected. If mild outliers are to be detected the value is 1. For extreme outliers the value is 2. Defaults to 1.
    :type mode: int, optional
    
    :param replace: Treatment of outliers. If the value is 1, rows containing outliers are deleted. If the value is 2, it shall be replaced by the maximum value when they are outliers above the maximum threshold and the minimum value when they are outliers below the minimum threshold. If the value is 3, outliers shall be replaced by the median. Defaults to 3.
    :type mode: int, optional
    """
    
    if view:
        sns.boxplot(data=dataset.data)
        plt.show()
    
    for i in range(dataset.data.shape[1]):
        columnData = dataset.data[:,i]        
        Q1, Q3 = np.percentile(columnData, [25, 75])
        IQR = Q3 - Q1
        
        if mode == 1:
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
        else:
            lower = Q1 - 3 * IQR
            upper = Q3 + 3 * IQR
        
        upperArray = np.where(columnData >= upper)[0]
        lowerArray = np.where(columnData <= lower)[0]
        
        if replace == 1:
            columnOutliers = np.concatenate((upperArray, lowerArray), axis=None)
            dataset.data = np.delete(dataset.data, columnOutliers, axis=0)
            
            if dataset.geneNames is not None:                
                dataset.geneNames = np.delete(dataset.geneNames, columnOutliers, axis=0)
            
            if dataset.lengths is not None:
                dataset.lengths = np.delete(dataset.lengths, columnOutliers, axis=0) 
        elif replace == 2:
            maxNonOutlier = columnData[columnData <= upper].max()
            minNonOutlier = columnData[columnData >= lower].min()            
            dataset.data[upperArray, i] = maxNonOutlier
            dataset.data[lowerArray, i] = minNonOutlier
        else:
            columnOutliers = np.concatenate((upperArray, lowerArray), axis=None)
            median = np.median(np.delete(columnData, columnOutliers))
            dataset.data[columnOutliers, i] = median