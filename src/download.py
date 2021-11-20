# author: UBC MDS Block 3 Group 4
# date: 2021-11-18

"""This script downloads data from a url and saves it to a local filepath as a csv.

Usage: download.py --url=<url> --out_file=<out_file> 

Options:
--url=<url>                        URL from where to download the csv data
--out_file=<out_file>              Path of where to write the file locally with the filename included
""" 

import os
import pandas as pd
from docopt import docopt


opt = docopt(__doc__)

def main(url, out_file):
  data = pd.read_csv(url)
  try:
    data.to_csv(out_file, index=False)
  except:
    os.makedirs(os.path.dirname(out_file))
    data.to_csv(out_file, index=False)
    
if __name__ == "__main__":
  main(opt["--url"],opt["--out_file"])
