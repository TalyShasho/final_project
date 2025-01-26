import pandas as pd
import matplotlib.pyplot as plt

def plot_average_rt(data):
    """
    Plots the average reaction times (RT) for each music type.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing columns 'participant_id', 'music_type', and 'RT'.

    Raises:
    - ValueError: If the required columns are not present in the DataFrame.
    """
    # Ensure the required columns are present
    required_columns = ["participant_id", "music_type", "RT"]
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"The input file must contain the following columns: {required_columns}")

    # Plot the data
    plt.figure(figsize=(10, 6))
    for music_type in data["music_type"].unique():
        music_data = data[data["music_type"] == music_type]
        plt.plot(music_data["participant_id"], music_data["RT"], label=music_type)

    plt.xlabel("Participant ID")
    plt.ylabel("Average RT")
    plt.title("Average RT for Each Music Type")
    plt.legend(title="Music Type")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the graph
    plt.show()





