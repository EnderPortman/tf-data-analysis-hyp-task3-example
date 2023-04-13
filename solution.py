import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

chat_id = 192196854  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # историч, новое
    
    return stats.mannwhitneyu(x, y, alternative="less").pvalue <= 0.1
