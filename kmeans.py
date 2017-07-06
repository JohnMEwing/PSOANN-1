import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn.cluster import KMeans
from scipy.cluster.vq import whiten

MY_FILE = '/Users/mihail/Desktop/yourprojectfilename.xlsx'
OUT_FILE = '/Users/mihail/Desktop/yourprojectfilename-km.xlsx'

# this function reads your Excel file and stores it in Data Frame object
df = pd.read_excel(MY_FILE)

# this function scales your data and stores in a new Data Frame object
norm_df = pd.DataFrame(whiten(df), columns=df.columns)

# this function makes a KMeans algorithm object
estimator = KMeans(n_clusters=2, random_state=0)

# this function runs KMeans on scaled Data Frame object
cluster = estimator.fit_predict(norm_df)

# this function puts the cluster labels in last column of orig. Data Frame obj.
df['cluster'] = cluster

# this functions writes thei orig. Data Frame object to Excel file
df.to_excel(OUT_FILE)

# prints truncated version of Data Frame to screen
print df

