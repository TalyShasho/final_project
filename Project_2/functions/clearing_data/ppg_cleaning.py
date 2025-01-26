"""Import necessary libraries for file handling and data processing"""

import os
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

# Paths to directories
ppg_folder =r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\PPG_data"
trial_folder = r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\trial_data"
output_file = r"C:\Users\tshas\OneDrive\Documentos\python 2\proyecto\Project_2\data\combined_data_trial.xlsx"


def process_ppg_and_trial_data_to_excel(ppg_folder, trial_folder, output_file):
    """
    Process PPG and trial data to calculate IS scores and save a consolidated Excel file.

    Parameters:
        ppg_folder (str): Path to the folder containing PPG files.
        trial_folder (str): Path to the folder containing trial files.
        output_file (str): Path to save the consolidated Excel file.

    Returns:
        None
    """
    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Function to calculate heartbeats in a given interval
    def calculate_heartbeats(ppg, start_time, end_time):
        # Filter PPG data within the time interval
        interval_data = ppg[(ppg['time'] >= start_time) & (ppg['time'] <= end_time)]
        print(f"Calculating heartbeats between {start_time} and {end_time}, found {len(interval_data)} data points.")
        # Detect peaks (heartbeats) in the PPG signal
        peaks, _ = find_peaks(interval_data['PPG'], height=0)  # Adjust height threshold as needed
        return len(peaks)

    # Initialize a list to store data for all participants
    all_participants_data = []

    # Get all PPG and trial files
    ppg_files = [f for f in os.listdir(ppg_folder) if f.endswith('.csv') and '_PPG' in f]
    trial_files = [f for f in os.listdir(trial_folder) if f.endswith('.csv') and 'trial_data' in f]

    # Try to read the existing Excel file to avoid overwriting
    if os.path.exists(output_file):
        with pd.ExcelFile(output_file) as existing_file:
            existing_sheets = existing_file.sheet_names
            # Read existing data into a dictionary of DataFrames (one per sheet)
            existing_data = {sheet: existing_file.parse(sheet) for sheet in existing_sheets}


    # Initialize Excel writer
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # Process each trial file
        for trial_file in trial_files:
            # Load trial data
            trial_data_path = os.path.join(trial_folder, trial_file)
            trial_data = pd.read_csv(trial_data_path)

            # Extract subject ID from the file name
            subject_id = trial_file.split('_')[0]
            print(f"Processing trial data for subject {subject_id}...")

            # Create a list to store this participant's data
            participant_data = []

            # Process PPG data for session 1 and session 2
            for session in [1, 2]:
                # Match PPG file for this subject and session
                ppg_file = f"{subject_id}_sess{session}_PPG.csv"
                ppg_path = os.path.join(ppg_folder, ppg_file)

                # Debugging output to ensure PPG file is correctly matched
                if not os.path.exists(ppg_path):
                    print(f"PPG file for subject {subject_id}, session {session} not found: {ppg_file}")
                    continue

                # Load PPG data (do not modify this data, just read for calculations)
                ppg_data = pd.read_csv(ppg_path)
                ppg_data = ppg_data.sort_values(by='time')  # Ensure PPG data is sorted

                # Loop through trial rows to calculate IA
                for index, row in trial_data.iterrows():
                    # Debugging output to check session and time matching
                    print(f"Checking row {index} for session {session}...")
                    if row['session'] == session:
                        start_time = row['PPG_response_start']
                        end_time = row['PPG_ITI_start']
                        print(f"Start time: {start_time}, End time: {end_time}")

                        # Calculate recorded heartbeats
                        nbeatrecorded = calculate_heartbeats(ppg_data, start_time, end_time)

                        # If no data points found in the PPG data, skip this entry
                        if nbeatrecorded == 0:
                            print(f"No heartbeats found for subject {subject_id}, session {session}. Skipping.")
                            continue

                        # Placeholder for participant-reported heartbeats
                        nbeatreported = nbeatrecorded + np.random.randint(-5, 5)  # Placeholder

                        # Calculate IA score
                        if nbeatrecorded > 0:
                            IA = 1 - (abs(nbeatreported - nbeatrecorded) / nbeatrecorded)
                        else:
                            IA = 0  # Handle edge case of no recorded heartbeats

                        # Average PPG value per reaction time
                        mean_ppg_data = ppg_data[(ppg_data['time'] >= start_time) & (ppg_data['time'] <= end_time)]['PPG'].mean()

                        # Append to participant data
                        participant_data.append({
                            'session': session,
                            'music_type': row.get('music_type', np.nan),
                            'valence_rating': row.get('valence_rating', np.nan),
                            'RT': row.get('RT', np.nan),
                            'PPG_response_start': start_time,
                            'participant_id': subject_id,
                            'PPG_data': mean_ppg_data,  
                            'IS': IA  # Ensure IS is added here
                        })

            # Check if participant data has been added
            if participant_data:
                print(f"Adding data for participant {subject_id}, session {session}: {len(participant_data)} rows")
            else:
                print(f"No data for participant {subject_id}, session {session}")

            # Append participant data to the overall list
            all_participants_data.extend(participant_data)

            # Write all participants' data to the summary sheet
            if all_participants_data:
                all_data_df = pd.DataFrame(all_participants_data)

                # Write the summary sheet only if it doesn't already exist
                if 'Summary' not in existing_sheets:
                    all_data_df.to_excel(writer, sheet_name='Summary', index=False)
                    print("Summary sheet written.")
                else:
                    print("Summary sheet already exists. Skipping write.")

            # Save existing data to the writer (preserve original sheets)
            for sheet, data in existing_data.items():
                data.to_excel(writer, sheet_name=sheet, index=False)

    print(f"Consolidated data saved to {output_file}")


