CLEANING DATA FORMULAS
match_ppg_dat
  This function matches PPG data to the trial data by comparing participant IDs and session numbers.

    Args:
    trial_combined_path (str): Path to the Excel file containing trial data.
    input_folder (str): Path to the folder containing the PPG CSV files.


process_ppg_and_trial_data_to_excel
    Process PPG and trial data to calculate IS scores and to calculate PPG maen and save a consolidated Excel file.

    Parameters:
        ppg_folder (str): Path to the folder containing PPG files.
        trial_folder (str): Path to the folder containing trial files.
        output_file (str): Path to save the consolidated Excel file.



ANALISIS DATA FORMULAS

analyze_music_type_vs_IS
         Analyze the relationship between 'music_type' and 'IS'. returns a wiskers plot for each type of music.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing 'music_type' and 'IS' columns.



plot_average_rt
    Plots the average reaction times (RT) for each music type.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing columns 'participant_id', 'music_type', and 'RT'.



plot_pulse_rate_by_interoception
     Analyzes and plots changes in pulse rate grouped by interoceptive sensitivity (IS).

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet containing the data.

calculate_spearman_correlation
    calculate spearman correlation between valence rating and average PPG.

plot_valence_vs_interoception
    Plots the relationship between average valence rating and interoceptive sensitivity (IS).

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet containing the data.

analyze_rt_by_music_type
  Analyzes reaction time (RT) differences between music types and performs ANOVA.

    Parameters:
        file_path (str): Path to the Excel file containing the data.


        
