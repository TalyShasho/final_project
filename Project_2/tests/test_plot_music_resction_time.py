import os
import unittest
from pathlib import Path
import functions.data_analysis.music_type_to_rt as plot_music_reaction_times  

class TestPlotMusicReactionTimes(unittest.TestCase):
    def setUp(self):
        self.file_path = r"C:\Users\Home\Desktop\Studies\Phyton\projects 2024-2025\Project_2\data\trial_mean_values.xlsx"
        os.makedirs(Path(self.file_path).parent, exist_ok=True)

    def tearDown(self):
        if Path(self.file_path).exists():
            os.remove(self.file_path)

    def test_plot(self):
        reaction_data = [
            {"participant_id": 1, "music_type": "tonal", "RT": 500},
            {"participant_id": 1, "music_type": "discord", "RT": 700},
            {"participant_id": 1, "music_type": "atonal", "RT": 900},
        ]
        plot_music_reaction_times(self.file_path)
