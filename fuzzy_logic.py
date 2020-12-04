import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime

# Fuzzy Logic
def symbol(x):
    sym = ["(", ")", " ", "\s+", "ซอย", "ถนน", "-", ".", "ฯ"]
    for i in sym:
        x = x.replace(i, "")
    return x


def fuzzy_match(row):
    try:
        matched_str, ratio, index = process.extractOne(row['FILE_A_sym'], FILE_B['FILE_B_sym'])
        row['FILE_B_sym'] = matched_str
        row['RAW_FILE_B'] = FILE_B[COL_B][index]
        row['score'] = ratio
        return row
    except:
        pass

start = datetime.now()
print("start at : ", start)

FILE_A = pd.read_csv('project_name_comp.csv')
FILE_B = pd.read_csv('project_name_subj.csv')

# FILE_A = FILE_A.head(10)
FILE_B = FILE_B.head(10)

COL_A = 'project_name_th'
COL_B = 'project_name'

FILE_A['FILE_A_sym'] = FILE_A[COL_A].apply(symbol)
FILE_B['FILE_B_sym'] = FILE_B[COL_B].apply(symbol)

FILE_A = FILE_A.apply(fuzzy_match, axis=1)
FILE_A.to_csv("RESULT.csv", index=None, encoding='utf-8-sig')
end = datetime.now()
print("end at : ", end)
print("------- ",end-start," -------")
