import numpy as np
import pandas as pd

from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

import statsmodels.api as sm
from statsmodels.tsa.api import Holt

import warnings
warnings.filterwarnings("ignore")

def evaluate(validate, yhat_df, target_var):
    '''
    This function will compute the RMSE for each model
    '''
    rmse = round(
        sqrt(
            mean_squared_error(
                validate[target_var], yhat_df[target_var])), 0)
    return rmse

def plot_and_eval(train, validate, yhat_df, target_var):
    '''
    This function will use the evaluate function and also plot 
    train and test values with the predicted values in order to 
    compare performance.
    '''
    # set figure size
    plt.figure(figsize = (12,4))
    # plot the target variable for train
    plt.plot(train[target_var], label = 'Train', linewidth = 1)
    # plot the target variable for validate
    plt.plot(validate[target_var], label = 'Validate', linewidth = 1)
    # plot the predictions
    plt.plot(yhat_df[target_var])
    # set the title to the target variable
    plt.title(target_var)
    # set RMSE using the evaluate function
    rmse = evaluate(validate, yhat_df, target_var)
    # print the target var and rmse
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()

def append_eval_df(eval_df, validate, yhat_df, model_type, target_var):
    '''
    This function will store rmse for comparison purposes
    '''
    # set RMSE using the evaluate function    
    rmse = evaluate(validate, yhat_df, target_var)
    # use a dictionary to set columns to respective values
    d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
    # turn the dictionary into a dataframe
    d = pd.DataFrame(d)
    # return the data frame with the new data added
    return eval_df.append(d, ignore_index = True)

def make_predictions(d, validate):
    '''
    This function creates yhat_df which is the dataframe 
    that contains the predictions on the validate dataset.
    '''
    yhat_df = pd.DataFrame(d, 
                       index = validate.index)
    return yhat_df