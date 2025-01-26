"""This script is the main code with all the functions neede to filter the data.

It uses the combine_ppg_averages function to calculate PPG averages and the filter_to_new_excel function
to filter the trial data based on selected columns.
"""

# Import the functions
from functions.clearing_data.adding_ppg_to_trial_comb import match_ppg_data
from functions.clearing_data.trial_combined import filter_to_new_excel
from functions.clearing_data.ppg_cleaning import process_ppg_and_trial_data_to_excel
from functions.data_analysis.ai_to_music_type import analyze_music_type_vs_IS
from functions.data_analysis.music_type_to_rt import analyze_rt_by_music_type
from functions.data_analysis.IS_ti_music_type import analyze_music_type_vs_IS
from functions.data_analysis.ppg_to_valence import calculate_spearman_correlation
from functions.data_analysis.ppg_by_IS import plot_pulse_rate_by_interoception
from functions.data_analysis.valence_to_IS import plot_valence_vs_interoception
from functions.data_analysis.music_type_to_rt_2 import plot_average_rt
import pandas as pd

# Path to the folder with trial data
folder_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\trial_data"
# Path to the folder with PPG file
input_folder = r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\PPG_data"
# Columns for combined_trial
selected_columns = ["session", "music_type", "valence_rating", "RT", "PPG_response_start"]
# Path to the final data folder
final_data_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data"
# Columns for PPG_combined data
needed_columns = ["valence_rating", "RT"]
# Path to the trial_combined
trial_combined_path = (
    r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\combined_data_trial.xlsx"
)


sheet_name="Summary"
df = pd.read_excel(trial_combined_path)

# Call the function from functions.py
'''
    CLEANING

filter_to_new_excel(folder_path, selected_columns, final_data_path)
match_ppg_data(trial_combined_path, input_folder)
process_ppg_and_trial_data_to_excel(input_folder, folder_path, trial_combined_path)'''


'''ANALISIS'''
analyze_rt_by_music_type(trial_combined_path)
analyze_music_type_vs_IS(df)
plot_pulse_rate_by_interoception(trial_combined_path,sheet_name)
analyze_music_type_vs_IS(df)
calculate_spearman_correlation(df)
plot_valence_vs_interoception(trial_combined_path, sheet_name)
plot_average_rt(df)
