"""Call the preprocessor.pkl that we stored, 
Conduct a cross validation with Logistic Regression Classifier,
Output the cross validation score table, the confusion matrix table and a pipe_lr.pkl 
that will be passed to the model testing script

Usage: cross_validation.py --X_train_input=<X_train_input> --y_train_input=<y_train_input> --out_cv=<out_cv> --out_matrix=<out_matrix> --out_pkl=<out_pkl>

Options: 
--X_train_input=<X_train_input>                  Path (including filename) to train data with "X_train"
--y_train_input=<y_train_input>                  Path (including filename) to raw train data with "y_train"
--out_cv=<out_cv>                                Path (including filename) to where the cross validation results should be written
--out_matrix=<out_matrix>                        Path (including filename) to where the confusion matrix of linear regression classifier should be written
--out_pkl=<out_pkl>                              Path (including filename) to where the pipe_lr.pkl should be written
"""

# Example:
# python src/cross_validation.py --X_train_input='data/processed/X_train.csv' --y_train_input='data/processed/y_train.csv' --out_cv='results/cv_score.csv' --out_matrix='results/lr_confusion_matrix.csv' --out_pkl='data/processed/pipe_lr.pkl'

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


def main(X_train_input, y_train_input, out_cv, out_matrix,out_pkl):
    """
    Read data from X_train and y_train and read preprocessor,
    Write the cross validation scores df and confusion matrix df to the assigned path.
    
    Parameters:
    ----------
    X_train_input: path for the X_train file
    
    y_train_input: path for the y_train file
    
    out_cv: directory where the cross validation score is saved
    
    out_matrix: directory where confusion matrix of logical regression classifier is saved
    
    out_pkl: directory where pipe_lr.pkl is saved
    
    Returns:
    --------
    cv_results: dataframe of the cross validation scores
    lr_matrix_df: dataframe of the confusion matrix
    
    """
    preprocessor_from_joblib = joblib.load('data/processed/preprocessor.pkl')
    X_train = pd.read_csv(X_train_input, encoding="utf-8")
    y_train = pd.read_csv(y_train_input, encoding="utf-8")
    
    #preprocessed_df = pd.DataFrame(preprocessor.fit_transform(X_train, y_train), columns = column_names)
  
    pipe_dummy = make_pipeline(preprocessor_from_joblib, DummyClassifier(random_state=123))
  
    pipe_lr = make_pipeline(
      preprocessor_from_joblib, LogisticRegression(max_iter=1000, random_state=123))
  
    scoring_metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc', 'average_precision']
  
    results={}
  
    results["Dummy Classifier"] = mean_std_cross_val_scores(
      pipe_dummy, X_train, y_train, scoring=scoring_metrics)
  
    results["Logistic Regression Classifier"] = mean_std_cross_val_scores(
      pipe_lr, X_train, y_train, scoring=scoring_metrics)
    
    #output cross validation scores
    cv_results = pd.DataFrame(results)
  
    cv_results.to_csv(out_cv, index=True)
    
    #output confustion matrix dataframe
    matrix_lr = pd.DataFrame(data=confusion_matrix(y_train, cross_val_predict(pipe_lr, X_train, y_train)))
    
    lr_matrix_df = matrix_lr.rename(columns={0:'edible', 1:'poisonous'}, index={0:'edible', 1:'poisonous'})
    
    lr_matrix_df.to_csv(out_matrix, index=True)
    
    #output the final model which can be passed to the test_results.py
    joblib.dump(pipe_lr, out_pkl)
    
  
    
  
def mean_std_cross_val_scores(model, X_train, y_train, **kwargs):
    """
    Returns mean and std of cross validation

    Parameters
    ----------
    model :
        scikit-learn model
    X_train : numpy array or pandas DataFrame
        X in the training data
    y_train :
        y in the training data

    Returns
    ----------
        pandas Series with mean scores from cross_validation
    """

    scores = cross_validate(model, X_train, y_train, **kwargs)

    mean_scores = pd.DataFrame(scores).mean()
    std_scores = pd.DataFrame(scores).std()
    out_col = []

    for i in range(len(mean_scores)):
        out_col.append((f"%0.3f (+/- %0.3f)" % (mean_scores[i], std_scores[i])))

    return pd.Series(data=out_col, index=mean_scores.index)

if __name__ == "__main__":
    main(opt['--X_train_input'], opt['--y_train_input'], opt['--out_cv'], opt['--out_matrix'],opt['--out_pkl']) 
