import pandas as pd
import numpy as np
import glob
import sys
import subprocess
import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

# ==========================================
# 1. Global Parameter Configuration
# ==========================================
@dataclass
class RiskConfig:
    # Baseline workload/wattage reference
    BASELINE_WORKLOAD: float = 1400.0   
    
    # Allowed exertion fluctuation percentage (Fatigue tolerance)
    EXERTION_TOLERANCE_PCT: float = 50.0 
    
    # Stability standard deviation threshold 
    # (Values > 300 indicate high sway/fall risk)
    STABILITY_THRESHOLD_SD: float = 300.0 
    
    # Volume threshold to be considered "silent" or "pause"
    SILENCE_THRESHOLD: float = 100.0     
    
    # Maximum allowed pause ratio during speech (30%)
    SILENCE_RATIO_LIMIT: float = 0.3     

class RehabRiskAgent:
    def __init__(self, patient_id: str, data_dir: Path, config: RiskConfig = RiskConfig()):
        self.patient_id = patient_id
        self.data_dir = data_dir
        self.config = config
        self.risks: List[str] = []

    def _load_and_clean(self, file_keyword: str, col_index: int) -> Optional[pd.DataFrame]:
        """
        Dynamic File Loading: 
        Prioritizes files containing [Patient_ID] in the filename.
        """
        pattern = self.data_dir / f"*{self.patient_id}*{file_keyword}*.csv"
        files = glob.glob(str(pattern))

        if not files:
            pattern = self.data_dir / f"*{file_keyword}*.csv"
            files = glob.glob(str(pattern))

        if not files:
            return None

        latest_file = max(files, key=lambda f: Path(f).stat().st_mtime)
        
        try:
            df = pd.read_csv(latest_file, header=None)
            if df.shape[1] <= col_index: 
                return None
            
            df.iloc[:, col_index] = pd.to_numeric(df.iloc[:, col_index], errors='coerce')
            clean_df = df[df.iloc[:, col_index] > 10].copy()
            return clean_df
        except Exception:
            return None

    def analyze(self):
        print(f"\nAnalyzing Folder: {self.data_dir.name}")
        print(f"Identified Patient ID: {self.patient_id}")
        print("-" * 40)
        
        # --- 1. Respiratory Analysis (Speak) ---
        df_speak = self._load_and_clean("speak", col_index=2)
        if df_speak is not None:
            gap_ratio = (df_speak.iloc[:, 2].abs() < self.config.SILENCE_THRESHOLD).sum() / len(df_speak)
            print(f"   Speak Pause Ratio: {gap_ratio:.1%}")
            if gap_ratio > self.config.SILENCE_RATIO_LIMIT:
                self.risks.append(f"Respiratory Risk ({gap_ratio:.1%})")
        else:
            print("   Warning: Speak file not found or invalid format")

        # --- 2. Fatigue/Exertion Analysis (Bike) ---
        df_bike = self._load_and_clean("bike_level1", col_index=2)
        if df_bike is not None:
            avg_load = df_bike.iloc[:, 2].mean()
            delta = ((avg_load - self.config.BASELINE_WORKLOAD) / self.config.BASELINE_WORKLOAD) * 100
            print(f"   Bike Load Variation: {delta:.1f}%")
            if delta > self.config.EXERTION_TOLERANCE_PCT:
                self.risks.append(f"PEM Risk ({delta:.0f}%)")
        else:
            print("   Warning: Bike file not found or invalid format")

        # --- 3. Stability Analysis (Static) ---
        df_static = self._load_and_clean("static_level1", col_index=3)
        if df_static is not None:
            if df_static.shape[1] > 4:
                df_static.iloc[:, 4] = pd.to_numeric(df_static.iloc[:, 4], errors='coerce')
                max_std = max(df_static.iloc[:, 3].std(), df_static.iloc[:, 4].std())
                print(f"   Static Stability (SD): {max_std:.1f}")
                if max_std > self.config.STABILITY_THRESHOLD_SD:
                    self.risks.append(f"Neuro Risk ({max_std:.0f})")
            else:
                print("   Warning: Static data missing Y-axis column")
        else:
            print("   Warning: Static file not found or invalid format")

    def get_result(self) -> str:
        if not self.risks:
            return "PASS (Healthy Data)"
        else:
            return f"FAIL ({'; '.join(self.risks)})"

# ==========================================
# 2. Independent Window Selector (Spyder Safe)
# ==========================================
def pick_folder_safely():
    print("Opening selection window, please wait...")
    popup_script = """
import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw() 
root.attributes('-topmost', True) 
path = filedialog.askdirectory(title='Select Patient Data Folder')
print(path) 
"""
    try:
        result = subprocess.run(
            [sys.executable, "-c", popup_script], 
            capture_output=True, 
            text=True
        )
        folder_path = result.stdout.strip()
        return folder_path if folder_path else None
    except Exception as e:
        print(f"Error: Window launch failed: {e}")
        return None

# ==========================================
# 3. Main Execution Block
# ==========================================
if __name__ == "__main__":
    print("--- Starting Generic Rehab Risk Agent ---")

    selected_path = pick_folder_safely()

    if selected_path:
        target_folder = Path(selected_path)
        
        # UNIVERSAL ID EXTRACTION:
        # Uses re.search to find the first sequence of digits anywhere in the name.
        # Example: "data84468686868685data" -> "84468686868685"
        # Example: "patient_999_test" -> "999"
        id_match = re.search(r'(\d+)', target_folder.name)
        
        if id_match:
            patient_id = id_match.group(1)
        else:
            # Fallback to full name if no numbers are found
            patient_id = target_folder.name
            
        agent = RehabRiskAgent(patient_id, target_folder)
        agent.analyze()
        
        print("\n" + "="*40)
        print(f"Final Result (ID: {patient_id}): {agent.get_result()}")
        print("="*40)
    else:
        print("Error: No folder selected.")