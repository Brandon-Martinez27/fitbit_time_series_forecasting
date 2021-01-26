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
    Splits the df into 50% train, 30% validate, 
    and 20% test
    '''
    # set the percentage/size for each split
    train_size = int(len(df) * .5)
    validate_size = int(len(df) * .3)
    test_size = int(len(df) - train_size - validate_size)
    validate_end_index = train_size + validate_size

    # split into train, validation, test
    train = df[: train_size]
    validate = df[train_size : validate_end_index]
    test = df[validate_end_index : ]
    return train, validate, test
    
def visualize_split(train, validate, test):
    '''
    Shows the plot for each variable and respective split
    '''
    for col in train.drop(columns=['month', 'weekday']).columns:
        plt.figure(figsize=(12,4))
        plt.plot(train[col])
        plt.plot(validate[col])
        plt.plot(test[col])
        plt.ylabel(col)
        plt.title(col)
        plt.show()
