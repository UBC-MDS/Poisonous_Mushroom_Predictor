"""Test the final model (pipe_lr.pkl) we have tuned using the test data.
Output the confusion matrix of predication on test data,
precision-recall curve with average precision score and ROC curve with AUC.

Usage: cross_validation.py --X_test_input=<X_test_input> --y_test_input=<y_test_input> --out_matrix_test=<out_matrix_test> 

Options: 
--X_test_input=<X_test_input>                    Path (including filename) to train data with "X_test"
--y_test_input=<y_test_input>                    Path (including filename) to raw train data with "y_test"
--out_matrix_test=<out_matrix_test>              Path (including filename) to where the cross validation results on test data should be written

"""

# Example:
# python src/test_lr_model_results.py --X_test_input='data/processed/X_test.csv' --y_test_input='data/processed/y_test.csv' --out_matrix_test='results/confusion_matrix_test.csv' 


import pandas as pd
import numpy as np
import joblib
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    make_scorer,
    precision_score,
    recall_score,
    average_precision_score, 
    auc
)

from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    cross_val_score,
    cross_validate,
    train_test_split,
)
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression, Ridge
from docopt import docopt
from sklearn.model_selection import cross_val_predict

opt = docopt(__doc__) 




def main(X_test_input, y_test_input, out_matrix_test):
    """
    Read data from X_test and y_test and read in pipe_lr preprocessor,
    Test model fitting on test data and output the confusion matrix on test data and print out the classification report.
    
    Parameters:
    ----------
    X_test_input: path for the X_test file
    
    y_test_input: path for the y_test file
    
    out_matrix_test: directory where confusion matrix of logical regression classifier on test data is saved
    
    Returns:
    --------
    matrix_test_df: dataframe of the confusion matrix on test data
    
    """
    preprocessor = joblib.load('data/processed/preprocessor.pkl')
    pipe_lr = joblib.load('data/processed/pipe_lr.pkl')
    X_test = pd.read_csv(X_test_input, encoding="utf-8")
    y_test = pd.read_csv(y_test_input, encoding="utf-8")
    
    pipe_lr.fit(X_test,y_test)
    preds = pipe_lr.predict(X_test)
    TN,FP,FN,TP = confusion_matrix(y_test, preds).ravel()
    
    d = {'edible': [TN,FN], 'poisonous': [FP, TP]}
    matrix_test_df = pd.DataFrame(data=d, index={'edible', 'poisonous'})
    #write confusion matrix
    matrix_test_df.to_csv(out_matrix_test, index=True)
    
    
    #print out classification report
    print(classification_report(y_test, pipe_lr.predict(X_test), target_names=["edible", "poisonous"]))
    
if __name__ == "__main__":
    main(opt['--X_test_input'], opt['--y_test_input'], opt['--out_matrix_test']) 
    
    
