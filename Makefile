# Poisonous Mushroom Predictor data pipe
# Authors: Kyle Maj, Dongxiao Li, Mahmoodur Rahman
# date: 2021.12.01

# example usage:
# make all


all : results/eda_plot.png results/cv_score.csv results/lr_confusion_matrix.csv results/confusion_matrix_test.csv doc/Poisonous_Mushroom_Predictor_Report.md doc/Poisonous_Mushroom_Predictor_Report.html


# download the raw data
data/raw/mushrooms.csv : src/download.py
	python src/download.py --url="https://raw.githubusercontent.com/kanchitank/Mushroom-Classification/master/mushrooms.csv" --out_file=data/raw/mushrooms.csv
 
# clean and split the raw data    
data/processed/test_df.csv data/processed/train_df.csv data/processed/X_test.csv data/processed/X_train.csv data/processed/y_test.csv data/processed/y_train.csv : src/clean_split.py data/raw/mushrooms.csv
	python src/clean_split.py --input_csv="data/raw/mushrooms.csv" --out_dir="data/processed/"
		
# preliminary eda
doc/pandas_preliminary_eda_mushrooms.html : src/preliminary_pandas_eda.py data/processed/train_df.csv
	python src/preliminary_pandas_eda.py --data=data/processed/train_df.csv --out_html=doc/pandas_preliminary_eda_mushrooms.html
		
# eda plot
results/eda_plot.png : src/eda.R data/processed/train_df.csv
	Rscript src/eda.R --train='data/processed/train_df.csv' --out_dir='results/eda_plot.png'

# create preprocessor
data/processed/preprocessor.pkl : src/preprocessor.py data/processed/X_train.csv data/processed/y_train.csv
	python src/preprocessor.py --X_train_input='data/processed/X_train.csv' --y_train_input='data/processed/y_train.csv' --out_pkl='data/processed/preprocessor.pkl'
		
# perform cross validation and create confusion matrix
data/processed/pipe_lr.pkl results/cv_score.csv results/lr_confusion_matrix.csv : src/cross_validation.py data/processed/preprocessor.pkl data/processed/X_train.csv data/processed/y_train.csv
	python src/cross_validation.py --X_train_input='data/processed/X_train.csv' --y_train_input='data/processed/y_train.csv' --out_cv='results/cv_score.csv' --out_matrix='results/lr_confusion_matrix.csv' --out_pkl='data/processed/pipe_lr.pkl'
		
# test model and output
results/confusion_matrix_test.csv : src/test_lr_model_results.py data/processed/X_test.csv data/processed/y_test.csv data/processed/pipe_lr.pkl data/processed/preprocessor.pkl
	python src/test_lr_model_results.py --X_test_input='data/processed/X_test.csv' --y_test_input='data/processed/y_test.csv' --out_matrix_test='results/confusion_matrix_test.csv' 
		
# final report
doc/Poisonous_Mushroom_Predictor_Report.md doc/Poisonous_Mushroom_Predictor_Report.html : doc/Poisonous_Mushroom_Predictor_Report.Rmd doc/poisonous_mushroom_refs.bib
	Rscript -e "rmarkdown::render('doc/Poisonous_Mushroom_Predictor_Report.Rmd')"

clean :  

	rm -rf data/raw/mushrooms.csv
	rm -rf data/processed/test_df.csv
	rm -rf data/processed/train_df.csv
	rm -rf data/processed/X_test.csv
	rm -rf data/processed/X_train.csv
	rm -rf data/processed/y_test.csv
	rm -rf data/processed/y_train.csv
	rm -rf doc/pandas_preliminary_eda_mushrooms.html
	rm -rf results/eda_plot.png
	rm -rf data/processed/preprocessor.pkl
	rm -rf data/processed/pipe_lr.pkl
	rm -rf results/cv_score.csv
	rm -rf results/lr_confusion_matrix.csv
	rm -rf results/confusion_matrix_test.csv
	rm -rf doc/Poisonous_Mushroom_Predictor_Report.md
	rm -rf doc/Poisonous_Mushroom_Predictor_Report.html

