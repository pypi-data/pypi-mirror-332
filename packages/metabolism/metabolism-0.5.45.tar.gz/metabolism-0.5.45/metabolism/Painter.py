import matplotlib
import matplotlib.pyplot as plt
class Painter:
    def __init__(self):
        pass
    def hotmap_zscore(self,matrix):
        plt.figure(figsize=(4,4))
        mask = np.triu(np.ones_like(matrix,dtype=bool))
        sns.heatmap(
            matrix,
            annot=False,          # 在格子中显示数值
            fmt=".2f",           # 数值格式（保留两位小数）
            mask=mask,
            cmap='coolwarm',     # 颜色映射
            vmin=-3, vmax=3,     # 颜色范围
            square=True,         # 保持格子为正方形
            linewidths=0.5,      # 格子间线宽
            cbar=True,
            cbar_kws={'label': 'Correlation'}
        )
        plt.tight_layout()
        plt.show()
    def hotmap_zscore2(self,matrix1,matrix2):
        plt.figure(figsize=(4,4))
        mask_lower = np.triu(np.ones_like(matrix1, dtype=bool), k=1)  # 隐藏上三角（含对角线）
        mask_upper = np.tril(np.ones_like(matrix2, dtype=bool), k=-1)  # 隐藏下三角（含对角线）
        fig, ax = plt.subplots(figsize=(8, 6))

        sns.heatmap(
            matrix1,
            mask=mask_lower,          # 隐藏上三角和对角线
            cmap='coolwarm',             # 下三角用蓝色系
            vmin=-3, vmax=3,     # 颜色范围
            annot=False,
            fmt=".2f",
            square=True,
            linewidths=0.5,
            cbar=False,
            ax=ax
        )
        
        sns.heatmap(
            matrix2,
            mask=mask_upper,          # 隐藏下三角和对角线
            cmap='coolwarm',              # 上三角用红色系
            vmin=-3, vmax=3,     # 颜色范围
            annot=False,
            fmt=".2f",
            square=True,
            linewidths=0.5,
            cbar=False,
            ax=ax
        )
        
        ax.plot(
            [matrix1.shape[0] + 1, 0],
            [matrix1.shape[0] + 1, 0],          # x从i到i+1
            color='red',         # 红色
            linewidth=2,         # 线宽
            transform=ax.transData,  # 使用数据坐标系
            clip_on=False,         # 避免边缘裁剪
            alpha=0.5
        )
        
        plt.tight_layout()
        plt.show()
    def hotmap_edge(self,matrix):
        plt.figure(figsize=(4,4))
        mask = np.triu(np.ones_like(matrix,dtype=bool))
        vmax = np.max(matrix)  # 获取数据最大值
        sns.heatmap(
            matrix,
            annot=False,          # 在格子中显示数值
            fmt=".2f",           # 数值格式（保留两位小数）
            mask=mask,
            cmap='coolwarm',     # 颜色映射
            square=True,         # 保持格子为正方形
            linewidths=0.5,      # 格子间线宽
            cbar=True,
            cbar_kws={'label': 'Correlation'}
        )
        plt.tight_layout()
        plt.show()