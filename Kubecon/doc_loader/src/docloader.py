import os
import pandas as pd
import argparse


# Defining and parsing the command-line arguments
parser = argparse.ArgumentParser(description='My program description')
parser.add_argument('--data', type=str,
                    help='Path of the local file or GCS blob containing the Input 1 data.')

parser.add_argument('--outputdata', type=str, help='')
args = parser.parse_args()

data = pd.read_csv("https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/new/Kubecon/data/data.csv")
outputdata = pd.read_csv('https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/new/Kubecon/data/outputdata.csv')
logger = logger or logging.getLogger('The data has successfully downloded')
print(logger)
