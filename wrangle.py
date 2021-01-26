import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def prep_fitbit():
    '''
    This function reads in the data from a csv to a dataframe,
    then cleans and prepares it for exploration.
    '''
    ###### DATA CLEANING ######

    # Read data: CSV --> Pandas DataFrame
    df = pd.read_csv('fitbit/fitbit_time_series.csv')
    # drop last 22 days since we will be predicting them
    df = df[:-22]

    # lowercase the features, use a '_' to replace whitespace
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # change 'date' --> datetime type
    df.date = pd.to_datetime(df.date)

    # change the index --> date, sort by date
    df.set_index(df.date, inplace=True)
    df = df.sort_index()
    
    # change the commas in 'calories_burned, steps, 
    # minutes_sedentary, activity_calories' --> '_'
    # change columns to int type
    df['calories_burned'] = df['calories_burned'].str.replace(',', '_').astype('int')
    df['steps'] = df['steps'].str.replace(',', '_').astype('int')
    df['minutes_sedentary'] = df['minutes_sedentary'].str.replace(',', '_').astype('int')
    df['activity_calories'] = df['activity_calories'].str.replace(',', '_').astype('int')

    ###### DATA PREPROCESSING ######

    # creates a month column in integer form
    df['month'] = df.date.dt.month
    # creates a day of the week column in string form
    df['weekday'] = df.date.dt.day_name()

    # drop remaining date column
    df.drop(columns='date', inplace=True)
    return df

def split_fitbit(df):
    '''
    Splits the df into 70% train, 30% test,
    then plots the visualization for the split
    using the calories_burned variable
    '''
    # 70% of the data will be train
    train_size = .70
    # n is set to the number of rows in the data (225)
    n = df.shape[0]
    # number of rows used to index for train data set
    test_start_index = round(train_size * n)

    train = df[:test_start_index] # everything up (not including) to the test_start_index
    test = df[test_start_index:] # everything from the test_start_index to the end

    # visulaize the split using calories burned as the y variable
    plt.plot(train.index, train.calories_burned)
    plt.plot(test.index, test.calories_burned)
    return train, test