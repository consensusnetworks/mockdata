from faker import Faker
import pandas as pd

from scipy.stats import norminvgauss
import matplotlib.pyplot as plt

import numpy as np

np.random.seed(0)

def create_df():
    
    plt = {'mu': 35.55, 'sigma': 4.53}

    dates = pd.date_range(start='1/1/2013', end='1/01/2015')
    x = np.random.normal(plt['mu'], plt['sigma'], (len(dates), 1)).round(decimals=2)
    df = pd.DataFrame(x, columns=['Plt_tranfused'])
    df = df.set_index(dates)
    
    return df

def fill_df():
    
    sigma = [17.16, 16.58, 46.17, 16.3, 
            32.22, 25.05, 16.41, 2.11, 12.38]
    
    mu = [255.88, 200.77, 651.95, 198.3,
        198.25, 185.19, 56.66, 9.4, 131.35]
    
    cols = ['PLT', 'WBC', 'RBC', 'HGB', 
            'MCV', 'MCH', 'MCHC', 'RDW', 'ALYM']
    
    df = create_df().reindex(columns=create_df().columns.tolist() + cols)
    
    
    for i in range(len(mu)):
        
        new_vals = np.random.normal(mu[i], sigma[i], (len(create_df()), 1)).round(decimals=2)
        df[cols[i]] = new_vals

    
    df.to_csv('healthnet_mockdata.csv')

    
fill_df()