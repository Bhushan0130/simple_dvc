# read the data from data source
# save it in the data/raw for further process

import os
from get_data import read_params, get__data
import argparse


def load_and_save(config_path):
    config = read_params(config_path)
    df = get__data(config_path)
    new_columns = [col.replace(' ' ,'_') for col in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']

    df.to_csv(raw_data_path, sep=',', index=False, header=new_columns)
    print(new_columns)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args =  args.parse_args()
    load_and_save(config_path=parsed_args.config)
