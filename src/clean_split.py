"""Clean, split and pre-processe the raw data;
Write the training and test data to separate csv files

Usage: clean_split.py --input_csv=<input_csv> --out_dir=<out_dir>

Options: 
--input_csv=<input_csv>   Path (including filename) to raw data with name "mushrooms"
--out_dir=<out_dir>       Path to directory folder where the processed data should be written
"""

# Example:
# python src/clean_split.py --input_csv="data/raw/mushrooms.csv" --out_dir="data/processed/"

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from docopt import docopt

opt = docopt(__doc__)


def main(input_csv, out_dir):
    """
    Reads data from raw data file. Do some data cleaning.
    And write to the assigned path.
    
    Parameters:
    ----------
    input_csv: path for the raw data file `data/raw/mushrooms.csv`
    
    out_dir: directory  where output files are saved
    
    Returns:
    --------
    train_df, test_df : csv files for train_df, test_df
    X_train, X_test, y_train, y_test : csv files for X_train, X_test, y_train, y_test
  
  
    """
    mushrooms = pd.read_csv(input_csv, encoding="utf-8")
    
    #change the label of raw csv for later benefits
    mushrooms.columns = ["class",
            "cap_shape",
            "cap_surface",
            "cap_color",
            "bruises",
            "odor",
            "gill_attachment",
            "gill_spacing",
            "gill_size",
            "gill_color",
            "stalk_shape",
            "stalk_root",
            "stalk_surface_above_ring",
            "stalk_surface_below_ring",
            "stalk_color_above_ring",
            "stalk_color_below_ring",
            "veil_type",
            "veil_color",
            "ring_number",
            "ring_type",
            "spore_print_color",
            "population",
            "habitat"]
            
    mushrooms = mushrooms.replace('?', np.nan)
    
    mushrooms["class"] = [1 if i == "p" else 0 for i in mushrooms["class"]] #Changing class values to "1" and "0"s.
    
    train_df, test_df = train_test_split(mushrooms, test_size=0.2, random_state=123)
    
    X_train = train_df.drop(columns=['class'])
    X_test = test_df.drop(columns=['class'])
    y_train = pd.DataFrame(train_df['class'])
    y_test = pd.DataFrame(test_df['class'])
    
    assert len(X_train) == len(y_train), "train feature and target dataframes do not have the same number of records"
    assert len(X_test) == len(y_test), "test feature and target dataframes do not have the same number of records"
    
    #Writing to csv files:
    write_to_csv(train_df, out_dir, 'train_df.csv')
    write_to_csv(test_df,  out_dir, 'test_df.csv')
    write_to_csv(X_train, out_dir, 'X_train.csv')
    write_to_csv(X_test, out_dir, 'X_test.csv')
    write_to_csv(y_train, out_dir, 'y_train.csv')
    write_to_csv(y_test, out_dir, 'y_test.csv')

    
def write_to_csv(df, out_dir, out_csv):
    """
    Check whether folder with preprocessed data exists. If exists, write the train and test dataframes in csv format.
    If not, create the directory folder and write the train and test dataframes in csv format.
    
    Parameters:
    ----------
    df : dataframe such as train_df or test_df
    out_dir: directory where output files should be saved

    Returns:
    --------
    csv files in the assigned folder. 
    
    """
    #Example: write_to_csv(train_df, "data/processed/")
    out_full = out_dir + out_csv
    
    try:
        df.to_csv(out_full, index=False)
    except:
        os.makedirs(os.path.dirname(out_full))
        df.to_csv(out_full, index=False)

    
if __name__ == "__main__":
    main(opt['--input_csv'], opt['--out_dir'])    
