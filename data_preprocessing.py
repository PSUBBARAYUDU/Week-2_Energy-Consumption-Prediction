import pandas as pd

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    print("Data loaded successfully!")
    return data
