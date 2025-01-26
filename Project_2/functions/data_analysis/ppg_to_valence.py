
import pandas as pd
from scipy.stats import spearmanr


#spearman correlation between valence rating and average PPG.
def calculate_spearman_correlation(data):
    # Clean column names
    data.columns = data.columns.str.strip()
    
    # Remove NaN values
    data_clean = data.dropna(subset=['valence_rating', 'PPG_data'])
    
    # Calculate Spearman's correlation
    corr, p_value = spearmanr(data_clean['valence_rating'], data_clean['PPG_data'])
    
    return print(f'Spearman’s correlation coefficient: {corr:.3f}, 'f'p-value: {p_value:.3f}')






