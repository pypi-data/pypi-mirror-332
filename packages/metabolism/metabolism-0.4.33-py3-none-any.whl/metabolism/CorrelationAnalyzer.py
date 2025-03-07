import SimpleITK as sitk
import numpy as np
import os,json
from pathlib import Path
import pandas as pd
from scipy import stats, linalg

class CorrelationAnalyzer:
    def __init__(self):
        pass
    def compute_partial_correlation_matrix(self,df,z=['Age', 'Sex', 'Weight']):
        '''partial correlation matrix: parital correlation between X and Y after removing linear effects of Z'''
        regions = [col for col in df.columns if col not in z]
        X = df[regions].values
        cover = []
        for zz in z:
            cover.append(df[zz].values)
        cover.append(np.ones(len(df)))
        covar = np.column_stack(cover)
        
        covar = (covar - covar.mean(axis=0)) / (covar.std(axis=0) + 1e-8)
        residuals = []
        for i in range(X.shape[1]):
            try:
                beta = linalg.lstsq(covar, X[:,i], cond=1e-6)[0]
            except LinAlgError:
                beta = np.dot(np.linalg.pinv(covar), X[:,i])
            resid = X[:,i] - np.dot(covar, beta)
            residuals.append(resid)
        
        residuals = np.array(residuals).T
        residuals += np.random.normal(0, 1e-8, residuals.shape)
        pcorr = np.corrcoef(residuals, rowvar=False)
        np.fill_diagonal(pcorr, 0)
        return pcorr