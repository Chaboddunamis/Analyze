from Analyze import analyze, get_dist
import pandas as pd
import numpy as np
import scipy.stats as stats
data = pd.read_csv('train.csv')

result = analyze(data)
result.analyze()
