import pandas as pd
import numpy as np
from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

customer = pd.read_csv("CustomerList2.txt",sep='\t')
customerProfile = pd.read_csv("CustomerProfiles.txt",sep='\t')
def plot_mean(data,attri):    
    data.groupby(attri).annualvolume.describe()
    data.groupby(attri).annualvolume.mean().plot(kind='bar', title="Scores", rot=0)
    plt.show()
plot_mean(customer,'plc')