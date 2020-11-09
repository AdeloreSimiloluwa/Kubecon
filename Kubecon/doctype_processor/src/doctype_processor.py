import os
import pandas as pd
import argparse
import logging  

# Defining and parsing the command-line arguments
parser = argparse.ArgumentParser(description='My program description')
parser.add_argument('--outpudata', type=str,
                    help='Path of the local file or GCS blob containing the Input 1 data.')

parser.add_argument('--vectorized', type=str, help='')
parser.add_argument('--image', type=str, help='')
parser.add_argument('--worddoc', type=str, help='')
args = parser.parse_args()

outputdata = pd.read_csv('https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/48f1681a89282870dfbdad926a3210877e22d1a8/Kubecon/data/outputdata.txt')
vectorized = pd.read_csv('https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/3a5e6ef279a621de8c38666b1ef5ac943a0739a1/Kubecon/data/vectorized.txt')
image = pd.read_csv('https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/760fe86e6dd07e53e1edf1d931f4ba5dcdaaa27c/Kubecon/data/images.txt')
worddoc = pd.read_csv('https://raw.githubusercontent.com/AdeloreSimiloluwa/Kubecon/461a614b498543fce07f0c1d24f2bd47e76fea48/Kubecon/data/worddoc.txt')
logger = logging.getLogger('Report an error if a document was skipped')
print(logger)
