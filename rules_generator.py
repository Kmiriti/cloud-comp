import os
import pandas as pd
from fpgrowth_py import fpgrowth
import pickle


playlists = pd.read_csv("/home/datasets/spotify/2023_spotify_ds1.csv")
transactions = playlists.groupby('pid')['track_uri'].apply(list).tolist()

freq_itemsets, rules = fpgrowth(transactions, minSupRatio=0.1, minConf=0.5)

model_path = os.getenv("MODEL_PATH", "model.pkl")  # save to local by default if persistent volume not set

# Save the generated rules
with open(model_path, "wb") as f:
    pickle.dump(rules, f)

print(f"Rules generated and saved to {model_path}!")