import os
import pandas as pd
import argparse
import logging  

def doctype_processor() -> str:
  return "Hello Word"
  
if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  doctype_processor()
