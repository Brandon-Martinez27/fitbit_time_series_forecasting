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

def final_eval(eval_df):
    '''
    This function takes the eval_df to helo determine which 
    model is best to move on to 'TEST' by grouping by
    target variable and model type to find lowest rmse for each
    '''
    pd.set_option('display.max_rows', None)
    final_eval = eval_df.groupby(['target_var', 'model_type'])[['rmse']].min()
    return final_eval

def final_plot(train, test, yhat_df, target_var):
    '''
    This function will plot the final model and also plot 
    train and test values with the predicted values in order to 
    compare performance on test.
    '''
    plt.figure(figsize=(12,4))
    plt.plot(train[target_var], label='train')
    plt.plot(test[target_var], label='test')
    plt.plot(yhat_df[target_var], alpha=.5)
    plt.title(target_var)
    plt.show()

def model_improvement(eval_df, final_eval):
    '''
    This function uses Last Observed Value as a baseline, then 
    calculates the final model's % improvement in performance.
    '''
    # Define baseline as last observed value
    baseline = pd.DataFrame(eval_df[eval_df.model_type == 'last_observed_value'])

    # Calcuating % improvement
    # First: work out the difference (increase) between the two numbers you are comparing
    base_error = baseline.rmse.sum()
    test_error = final_eval[final_eval.model_type =='30d_moving_avg'].rmse.sum()
    difference = (base_error - test_error)
    # Then: divide the increase by the original number and multiply the answer by 100
    percent_improve = round((difference / base_error) * 100, 2)
    print(f'The % improvement for our model is {percent_improve}%')

def predict_plot(df, yhat_df, target_var):
    '''
    This function plots the full data set with the prediction 
    of next two weeks based on the 30 day moving average model.
    '''
    plt.figure(figsize=(12,4))
    plt.plot(df[target_var], label='train')
    plt.plot(yhat_df[target_var], alpha=.5)
    plt.title(target_var)
    plt.show()
################################ Models ################################

def last_observed_value(train):
    '''
    This function stores Last Obsevered Value in a dictionary. 
    Keys are target variables, values are the Last Obsevered Value.
    '''
    d = {}
    for col in train.columns:
        if type(col) == 'int':
            d[col] = train[col][-1:][0]
        else:
            d[col] = round(train[col][-1:][0],2)
    return d

def simple_avg(train):
    '''
    This function stores Simple Average in a dictionary. 
    Keys are target variables, values are the Simple Average.
    '''
    d = {}
    for col in train.columns:
        d[col] = round(train[col].mean(),2)
    return d


def moving_avg(train):
    '''
    This function stores 30 day Moving Average in a dictionary. 
    Keys are target variables, values are the 30 day Moving Average.
    '''
    period = 30
    d = {}
    for col in train.columns:
        d[col] = round(train[col].rolling(period).mean().iloc[-1], 2)
    return d

def holts(train, validate, yhat_df):
    '''
    This function sets default parameters for Holt's model. 
    yhat_items makes predictions based on model.
    '''
    for col in train.columns:
        model = Holt(train[col], exponential = False, damped=True)
        model = model.fit(smoothing_level = .1, 
                        smoothing_slope = .1, 
                        optimized = True)
        yhat_items = model.predict(start = validate.index[0], 
                                end = validate.index[-1])
        yhat_df[col] = round(yhat_items, 2)
    return yhat_df

def prev_cycle(train2, validate2):
    '''
    This function makes the last two weeks from train the predictions
    for the next two weeks.
    '''
    yhat_df = train2['2018-10-27':'2018-11-09'] + train2.diff(14).mean()
    yhat_df.index = validate2.index
    return yhat_df

