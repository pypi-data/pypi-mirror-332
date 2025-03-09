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

class IndividualNetwork(Network):
    def __init__(self,control,dataset2,modelname):
        super().__init__()
        self.dataset1 = control
        self.dataset2 = dataset2
        self.modelname = modelname
    def process(self,referencenumber,covariate=['Age', 'Sex', 'Weight']):
        dataset1 = self.dataset1
        dataset2 = self.dataset2
        modelname = self.modelname
        df1 = self.correlationAnalyzer.dataset2df(dataset1,modelname)
        df2 = self.correlationAnalyzer.dataset2df(dataset2,modelname)
        self.df1 = df1
        self.df2 = df2
        print(f"[{self.INFO_ICON}] dataset1:",dataset1)
        print(f"[{self.SUCCESS_ICON}] dataset1 count:{len(df1)}")
        print(f"[{self.INFO_ICON}] dataset2:",dataset2)
        print(f"[{self.SUCCESS_ICON}] dataset2 count:{len(df2)}")
        df1_referece,df1_control = self.helper.split_dataframe(df1,referencenumber,random_seed=42)
        refnet = self.correlationAnalyzer.compute_partial_correlation_matrix(df1_referece,z=['Age', 'Sex', 'Weight'])

        edge_significant_counts = np.zeros_like(refnet, dtype=int)
        df2_zscores = []
        for i, row_dict in df2.iterrows():
            df1_referece_ = df1_referece.copy()
            current_row = pd.DataFrame([row_dict])
            combined = pd.concat([df1_referece_, current_row], ignore_index=True)
            # Perturbed network
            pnet = self.correlationAnalyzer.compute_partial_correlation_matrix(combined,z=['Age', 'Sex', 'Weight'])
            delta_pnet = pnet - refnet
            se = (1 - refnet**2) / (referencenumber - len(covariate) - 1)
            z_scores = delta_pnet / se
            df2_zscores.append(z_scores)

            p_values = 2 * norm.sf(np.abs(z_scores))
            num_edges = p_values.size - np.isnan(p_values).sum()
            alpha_corrected = 0.05 / num_edges
            significant_edges = p_values < alpha_corrected
            edge_significant_counts[significant_edges] += 1

        control_zscores = []
        for i, row_dict in df1_control.iterrows():
            df1_referece_ = df1_referece.copy()
            current_row = pd.DataFrame([row_dict])
            combined = pd.concat([df1_referece_, current_row], ignore_index=True)
            # Perturbed network
            pnet = self.correlationAnalyzer.compute_partial_correlation_matrix(combined,z=['Age', 'Sex', 'Weight'])
            delta_pnet = pnet - refnet
            se = (1 - refnet**2) / (referencenumber - len(covariate) - 1)
            z_scores = delta_pnet / se
            control_zscores.append(z_scores)
        self.control_zscores = control_zscores
        self.df2_zscores = df2_zscores
        self.edge_significant_counts = edge_significant_counts
        print(f"[{self.SUCCESS_ICON}SUCCESS] return dataset: control_zscores,df2_zscores,edge_significant_counts")
        return control_zscores,df2_zscores,edge_significant_counts
    def analyze_multiorgan(self):
        print(f"[{self.INFO_ICON}] multiorgan analyze starting")
        edge_significant_counts = self.edge_significant_counts
        df2_zscores = self.df2_zscores
        control_zscores = self.control_zscores
        
        mask_lower = np.triu(np.ones_like(edge_significant_counts, dtype=bool), k=1)
        edge_significant_counts[mask_lower] = 0
        rows, cols = np.where(edge_significant_counts != 0)
        values = self.edge_significant_counts[rows, cols]
        edges = list(zip(values, rows, cols))
        sorted_edges = sorted(edges, key=lambda x: x[0], reverse=True)

        columns = [x for x in self.df1.columns if x not in ['Age', 'Sex', 'Weight']]
        control_zscore_mean = np.mean(control_zscores,axis=0)
        df2_zscore_mean = np.mean(df2_zscores,axis=0)
        control_zscore_std = np.std(control_zscores,axis=0)
        df2_zscore_std = np.std(df2_zscores,axis=0)
        data_list = []
        
        for count,row,col in sorted_edges:
            if count < len(self.df2) * 0.2:
                continue
            roi1 = columns[row]
            roi2 = columns[col]
            meanz1 = df2_zscore_mean[row,col]
            stdz1 = df2_zscore_std[row,col]
            meanz2 = control_zscore_mean[row,col]
            stdz2 = control_zscore_std[row,col]
            data_list.append({"SignificantCount":count,"roi1":roi1,"roi2":roi2,"patient_z_mean":meanz1,
                 "patient_z_std":stdz1,"control_z_mean":meanz2,"control_z_std":stdz2})
        df = pd.DataFrame(data_list)
        print(f"[{self.SUCCESS_ICON}SUCCESS] return dataframe: SignificantCount,roi1,roi2,patient_z_mean,patient_z_std,control_z_mean,control_z_std")
        return df

    def analyze_singleorgan(self):
        print(f"[{self.INFO_ICON}] singleorgan analyze starting...")
        df2_zscores = self.df2_zscores
        control_zscores = self.control_zscores
        control_zscores = np.abs(np.array(control_zscores))
        df2_zscores = np.abs(np.array(df2_zscores))
        
        columns = [x for x in self.df1.columns if x not in ['Age', 'Sex', 'Weight']]
        data_list = []
        for i in range(len(columns)):
            roi = columns[i]
            control_degree = np.sum(control_zscores[:,i],axis=1)
            df2_degree = np.sum(df2_zscores[:,i],axis=1)
            df2_degree_max = np.max(df2_degree)
            df2_degree_mean = np.mean(df2_degree)
            control_degree_max = np.max(control_degree)
            control_degree_mean = np.mean(control_degree)
            data_list.append({"roi":roi,"patient_degree_max":df2_degree_max,"patient_degree_mean":df2_degree_mean,
                              "control_degree_max":control_degree_max,"control_degree_mean":control_degree_mean})
        df = pd.DataFrame(data_list)
        df = df.sort_values(by="patient_degree_mean", ascending=False)
        print(f"[{self.SUCCESS_ICON}SUCCESS] return dataframe: roi,patient_degree_max,patient_degree_mean,control_degree_max,control_degree_mean")
        return df