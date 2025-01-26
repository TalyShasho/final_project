import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from functions.data_analysis.ppg_by_IS import plot_pulse_rate_by_interoception  # Replace with your module name

def create_test_excel(file_name, sheet_name):
    """
    Creates a test Excel file with sample data for testing.
    """
    data = {
        'participant_id': [f'P{i}' for i in range(1, 21)],
        'IS': np.random.choice(range(0, 101, 10), 20),  # Random IS values (0 to 100)
        'PPG_data': np.random.uniform(60, 100, 20)  # Simulated pulse rate data
    }
    df = pd.DataFrame(data)
    with pd.ExcelWriter(file_name) as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    return file_name, sheet_name

def test_plot_pulse_rate_by_interoception():
    # Create a temporary test Excel file
    test_file, test_sheet = create_test_excel('test_data.xlsx', 'Sheet1')

    try:
        # Test the function with valid input
        plot_pulse_rate_by_interoception(test_file, test_sheet)
        print("Test Passed: Function ran successfully with valid input.")
    except Exception as e:
        print(f"Test Failed: Function raised an error with valid input: {e}")

    # Test with a missing column
    missing_column_file, _ = create_test_excel('missing_column_data.xlsx', 'Sheet1')
    df_missing_col = pd.read_excel(missing_column_file, sheet_name='Sheet1')
    df_missing_col = df_missing_col.drop(columns=['PPG_data'])
    df_missing_col.to_excel(missing_column_file, index=False, sheet_name='Sheet1')

    try:
        plot_pulse_rate_by_interoception(missing_column_file, test_sheet)
        print("Test Failed: Function did not raise an error for missing column 'PPG_data'.")
    except KeyError as ke:
        print("Test Passed: Function correctly raised KeyError for missing column 'PPG_data'.")
    except Exception as e:
        print(f"Test Failed: Unexpected error for missing column test: {e}")

if __name__ == "__main__":
    test_plot_pulse_rate_by_interoception()
