import os
import pandas as pd
import argparse
import logging  

def doctype_processor(argv=None):
  # Defining and parsing the command-line arguments
  parser = argparse.ArgumentParser(description='My program description')
  parser.add_argument('--outputdata', type=str,
                      help='Path of the local file or GCS blob containing the Input 1 data.')
  parser.add_argument('--vectorized', type=str, help='')
  parser.add_argument('--image', type=str, help='')
  parser.add_argument('--worddoc', type=str, help='')
  parser.add_argument('--output_dir', type=str, help='')
  parser.add_argument('--output-path-file', help='')
  known_args, pipeline_args = parser.parse_known_args(argv)
  args = parser.parse_args()

  a = "hello world"
  b = "hello world"
  c = "hello world"
  d = "hello world"
  
  print(a,b,c,d)
  
  
  Path(known_args.output_path_file).parent.mkdir(parents=True, exist_ok=True)
  Path(known_args.output_path_file).write_text(known_args.outputdata) 
  
  
if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  doctype_processor()
