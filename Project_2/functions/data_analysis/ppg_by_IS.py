import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter

def plot_pulse_rate_by_interoception(is_file,sheet_name):
    """
    Analyzes and plots changes in pulse rate grouped by interoceptive sensitivity (IS).

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet containing the data.
    
    Returns:
        None
    """
    # Load data
    data = pd.ExcelFile(is_file)
    sheet_data = data.parse(sheet_name)

    # Group data by participant_id and IS to calculate changes in pulse rate
    # 'PPG_data' represents pulse rate data and changes are calculated as standard deviation
    grouped_data = sheet_data.groupby(['participant_id', 'IS']).agg({
        'PPG_data': 'std'
    }).reset_index()

    # Rename columns for clarity
    grouped_data.rename(columns={'PPG_data': 'Pulse Rate Changes'}, inplace=True)

    # Plotting the grouped data
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='IS', y='Pulse Rate Changes', data=grouped_data, palette='viridis')

    formatter = FuncFormatter(lambda x, pos: '{:.0f}'.format(x))
    plt.gca().xaxis.set_major_formatter(formatter)


    # Customize the plot
    plt.title('Changes in Pulse Rate Grouped by Interoceptive Sensitivity', fontsize=14)
    plt.xlabel('Interoceptive Sensitivity (IS)', fontsize=12)
    plt.ylabel('Pulse Rate Changes', fontsize=12)
    plt.xlim(0,100)
    plt.xticks(np.arange(0, 101, 5), rotation=45)
    plt.grid(alpha=0.3)
    plt.tight_layout()

    # Show the plot
    plt.show()

trial_combined_path = (
    r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\combined_data_trial.xlsx"
)


sheet_name="Summary"
plot_pulse_rate_by_interoception(trial_combined_path,sheet_name)