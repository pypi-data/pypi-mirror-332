from metabolism.CorrelationAnalyzer import CorrelationAnalyzer
from metabolism.Helper import Helper

class Network:
    def __init__(self):
        self.ERROR_ICON = '❌'
        self.SUCCESS_ICON = '✅'
        self.RUNNING_ICON = '⏳'
        self.INFO_ICON = '➤'
        self.correlationAnalyzer = CorrelationAnalyzer()
        self.helper = Helper()
    def process(self,dataset1,dataset2,modelname):
        pass
class GroupLevelNetwork(Network):
    def process(self,dataset1,dataset2,modelname):
        df1 = self.correlationAnalyzer.dataset2df(dataset1,modelname)
        df2 = self.correlationAnalyzer.dataset2df(dataset2,modelname)
        print(f"[{self.INFO_ICON}] dataset1:",dataset1)
        print(f"[{self.SUCCESS_ICON}] dataset1 count:{len(df1)}")
        print(f"[{self.INFO_ICON}] dataset2:",dataset2)
        print(f"[{self.SUCCESS_ICON}] dataset2 count:{len(df2)}")
        pcorr1 = self.correlationAnalyzer.compute_partial_correlation_matrix(df1,z=['Age', 'Sex', 'Weight'])
        pcorr2 = self.correlationAnalyzer.compute_partial_correlation_matrix(df2,z=['Age', 'Sex', 'Weight'])
        numerator = pcorr1 - pcorr2
        denominator = pcorr1 + pcorr2
        denominator[denominator == 0] = 1e-6
        diffgroup = numerator / denominator
        print(f"[{self.SUCCESS_ICON}] group-level metabolic network is returned !!")
        return diffgroup