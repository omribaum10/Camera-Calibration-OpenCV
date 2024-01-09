import pickle
from pathlib import Path


with open('calibration.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)
