import os
import pandas as pd
import argparse
import logging  
import json
from pathlib import Path

# Defining and parsing the command-line arguments
parser = argparse.ArgumentParser(description='My program description')
parser.add_argument('--data', type=str,help='Path of the local file or GCS blob containing the Input 1 data.')

parser.add_argument('--outputdata', type=str ,  help= '')
parser.add_argument('--output-path-file', help='')
known_args, pipeline_args = parser.parse_known_args(argv)
args = parser.parse_args()
# print(os.path.dirname(args.outputdata))

print(args.data)
print(args.outputdata)

data = pd.read_csv("https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/86a4b712940a8e1296fc7156b62c07cff3a2c0ee/Kubecon/data/data.txt")
outputdata = pd.read_csv('https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/48f1681a89282870dfbdad926a3210877e22d1a8/Kubecon/data/outputdata.txt')
logger = logging.getLogger('The data has successfully downloded')
print(logger)

Path(known_args.output_path_file).parent.mkdir(parents=True, exist_ok=True)
Path(known_args.output_path_file).write_text(known_args.output) 
