import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu
from scipy.stats import ks_2samp
from scipy.stats import brunnermunzel
from scipy.stats import permutation_test
from scipy.stats import ttest_ind
class Analyzer:
    def __init__(self):
        self.ERROR_ICON = '❌'
        self.SUCCESS_ICON = '✅'
        self.RUNNING_ICON = '⏳'
        self.INFO_ICON = '➤'

    def intersubject_dissimilarity(self,matrixs,roi_names):
        print(f"[{self.INFO_ICON}] Dissimilarity -1 to 1.")
        matrixs = np.array(matrixs)
        dissimilarity_mean = np.zeros_like(roi_names)
        dissimilarity_std = np.zeros_like(roi_names)
        for i,roi_name in enumerate(roi_names):
            corr = np.corrcoef(matrixs[:,i])
            dissimilarity_mean[i] = np.mean(-corr)
            dissimilarity_std[i] = np.std(-corr)
        df = pd.DataFrame({"roi":roi_names,"dissimilarity_mean":dissimilarity_mean,"dissimilarity_std":dissimilarity_std})
        print(f"[{self.SUCCESS_ICON}] df columns: roi, dissimilarity_mean, dissimilarity_std")
        return df

    def roi_pair_compare(self,matrixs1,matrixs2,roi_names,pmethod="mannwhitneyu"):
        print(f"[{self.INFO_ICON}] If roi-roi pair has significant difference between two groups.")
        matrixs1 = np.array(matrixs1)
        matrixs2 = np.array(matrixs2)
        results = []
        for i in range(len(roi_names)):
            for j in range(i+1,len(roi_names)):
                data1 = matrixs1[:,i,j]
                data2 = matrixs2[:,i,j]
                if pmethod == "mannwhitneyu":
                    stat, p = mannwhitneyu(data1, data2, alternative='two-sided')
                elif pmethod == "kolmogoerov_smirnov":
                    stat, p = ks_2samp(data1, data2)
                elif pmethod == "brunnermunzel":
                    stat, p = brunnermunzel(data1, data2)
                elif pmethod == "t":
                    stat, p = ttest_ind(data1,data2, equal_var=False)
                row = {
                    'roi1': roi_names[i],
                    'roi2': roi_names[j],
                    'group1':np.mean(data1),
                    'group2':np.mean(data2),
                    'p': p,
                }
                results.append(row)
        df = pd.DataFrame(results)
        total_comparisons = len(df)  # ROI对的总数
        corrected_alpha = 0.05 / total_comparisons
        df['significant'] = df['p'] < corrected_alpha
        return df
    # def group_similarity(self,matrixs)