# author: UBC MDS Block 3 Group 4
# date: 2021-11-18

"""This script outputs the EDA report of the data.
Usage: preliminary_pandas_eda.py --data=<data> --out_html=<out_html>

Options:
--data=<data>                    Any data file that you want to render EDA html pandas profile
--out_html=<out_html>            Save the rendered EDA html file locally to data folder with the filename included
""" 

import pandas as pd
from docopt import docopt
from pandas_profiling import ProfileReport



opt = docopt(__doc__)

def main(data, out_html):
  df = pd.read_csv(data, encoding="utf-8")
  profile = ProfileReport(df, title="EDA")
  profile.to_file(out_html)
  

if __name__ == "__main__":
    main(opt["--data"], opt["--out_html"])
