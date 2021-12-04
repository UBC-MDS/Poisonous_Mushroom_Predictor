"""Preprocess and transform the train data using 
`make_column_transformer` and `make_pipeline` and output a pickle file called
preprocessor.pkl using `joblib`

Usage: preprocessor.py --X_train_input=<X_train_input> --y_train_input=<y_train_input> --out_pkl=<out_pkl> 

Options: 
--X_train_input=<X_train_input>        Path (including filename) to train data with "X_train"
--y_train_input=<y_train_input>        Path (including filename) to raw train data with "y_train"
--out_pkl=<out_pkl>                    Path (including filename) to where the preprocessor.pkl should be written

"""

# Example:
# python src/preprocessor.py --X_train_input='data/processed/X_train.csv' --y_train_input='data/processed/X_train.csv' --out_pkl='data/processed/preprocessor.pkl'

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer, make_column_transformer
from docopt import docopt
import joblib

opt = docopt(__doc__)


def main(X_train_input, y_train_input, out_pkl):
      """Reads data from X_train and y_train.
      Write the preprocessor to the assigned path.
    
      Parameters:
      ----------
      X_train_input: path for the X_train file
    
      y_train_input: path for the y_train file
    
      out_pkl: directory where preprocessor.pkl is saved
    
      Returns:
      --------
      preprocessor: preprocessor saved using jotlib"""

      X_train = pd.read_csv(X_train_input, encoding="utf-8")
      y_train = pd.read_csv(y_train_input, encoding="utf-8")

      preprocessor = preprocessor_pipeline(X_train, y_train)
    
      joblib.dump(preprocessor, out_pkl)
      

  

def preprocessor_pipeline(df1, df2):
      """
      Transform the X_train and y_train dataset using a pipeline with
      column transformer and output the preprocessor in jotlib format.
    
      Parameters:
      ----------
      df1 : dataframe for features
      df2:  dataframe for target

      Returns:
      --------
      pickle file which stores the preprocessor which can be reloaded easily. 
    
      """

       
      categorical_features = [
            "cap_shape",
            "cap_surface",
            "cap_color",
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
            "veil_color",
            "ring_number",
            "ring_type",
            "spore_print_color",
            "population",
            "habitat"]
      binary_features = ["bruises"] #binary
      drop_features = ["veil_type"] #only one class
    
    
      categorical_transformer = make_pipeline(
        SimpleImputer(strategy="constant", fill_value="missing"),
        OneHotEncoder(handle_unknown="ignore", sparse=False))

      binary_transformer = make_pipeline(
         OneHotEncoder(drop="if_binary", dtype=int))


      preprocessor = make_column_transformer(
         (binary_transformer, binary_features),
         (categorical_transformer, categorical_features),
         ("drop", drop_features))
    
      #preprocessor.fit_transform(df1, df2)
    
      return preprocessor
      
    
  
  
if __name__ == "__main__":
      main(opt['--X_train_input'], opt['--y_train_input'], opt['--out_pkl'])  
