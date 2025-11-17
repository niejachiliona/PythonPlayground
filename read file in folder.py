# read file in folder
import pandas as pd
import os
from pathlib import Path
folder_path = Path(__file__).parent
file_path = folder_path / 'data.csv'
df = pd.read_csv(file_path) 
print(df.head())