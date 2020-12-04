import Levenshtein as lev
import pandas as pd


def symbol(x):
    sym = ["(", ")", " ", "\s+", "ซอย", "ถนน", "-", ".", "ฯ"]
    for i in sym:
        x = x.replace(i, "")
    return x


# Import data files
file_A = pd.read_csv('project_name_comp.csv')
file_B = pd.read_csv('project_name_subj.csv')

file_A = file_A.head(10)
file_B = file_B.head(10)
result = pd.DataFrame(columns=['project_name_th', 'project_name', 'edit_distance', 'ratio'])

for i in file_A['project_name_th']:
    for j in file_B['project_name']:
        result = result.append({'project_name_th': i, 'project_name': j, 'edit_distance': lev.distance(i, j), 'ratio': lev.ratio(i, j)}, ignore_index=True)
        print(i, j)

result.to_csv("lev_RESULT.csv", index=None, encoding='utf-8-sig')
