# Split the raw data
# Save it in data/processed folder
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_saved_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_data"]
    train_data_path = config["split_data"]["train_data"]
    raw_data_path = config["load_data"]["raw_dataset.csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]


    df = pd.read_csv(raw_data_path, sep = ",")

    train, test = train_test_split(
        df, 
        test_size = split_ratio, 
        random_state = random_state
        )

    train.to_csv(train_data_path, sep = ",", index = False, encoding = "utf-8")
    test.to_csv(test_data_path, sep = ",", index = False, encoding = "utf-8")
    
