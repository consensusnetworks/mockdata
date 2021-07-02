from faker import Faker
import pandas as pd

from scipy.stats import norminvgauss
import matplotlib.pyplot as plt

import numpy as np

save_state = np.random.get_state()

np.random.set_state(save_state)

def create_df():

    'Creates pandas dataframe from scratch. Also index is set as the date'
    
    plt = {'mu': 35.55, 'sigma': 4.53}

    dates = pd.date_range(start='1/1/2013', end='1/01/2015')
    x = np.random.normal(plt['mu'], plt['sigma'], (len(dates), 1)).round(decimals=0)
    df = pd.DataFrame(x, columns=['Plt_tranfused'])
    df = df.set_index(dates)
    
    return df

def fill_df():
    ''' 
    Columns 2-10 values are the number of patients in the hospital with abnormal
    lab readings according to the column title. For example on January 1, 2013
    there were 36.8 patients with abnormal PLT (platelets) values. 

    The Stanford paper provides hospital census information including
    both daily mean and stdv for the census for each hospital unit. We will
    add these covariates to our mock dataset.  
    '''
    
    mu = [255.88, 200.77, 651.95, 198.3, 198.25, 185.19, 56.66, 9.4, 131.35, 
        15.19, 22.74, 22.36, 2.61, 17.86, 23.33, 12.68, 23.59, 26.33, 20.13, 
        26.49, 20.79, 22.95, 20.36, 32.77, 19.72, 11.22, 9.9, 13.5]

    sigma = [17.16, 16.58, 46.17, 16.3, 32.22, 25.05, 16.41, 2.11, 12.38,
            1.84, 2.17, 2.24, 2.35, 2.88, 2.03, 1.22, 1.83, 5.17, 1.44, 
            3.5, 2.53, 2.51, 3.79, 2.11, 3.56, 1.94, 8.89, 1.49]

    cols = ['PLT', 'WBC', 'RBC', 'HGB', 'MCV', 'MCH', 'MCHC', 'RDW', 'ALYM',
            'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D2', 'D3', 'DGR', 'E1', 
            'E2.ICU', 'E29.ICU', 'E3', 'F3', 'FGR', 'G1', 'G2P', 'H1', 'H2']
    
    df = create_df().reindex(columns=create_df().columns.tolist() + cols)
    
    
    for i in range(len(mu)):
        
        new_vals = np.random.normal(mu[i], sigma[i], (len(create_df()), 1)).round(decimals=0)
        df[cols[i]] = new_vals

    df.to_csv('healthnet_mockdata.csv', index=True)

    return df