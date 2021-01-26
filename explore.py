import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_dist(train):
    '''
    This function plots the histograms for each of the 9
    target variables in the fitbit dataset
    '''
    count=0
    for i in train.drop(columns=['weekday','month']):
        plt.rc('figure', figsize=(16,9))
        count+=1
        plt.subplot(3, 3, count)
        sns.histplot(data=train.drop(columns=['weekday','month']), x=i, kde=True)
    plt.tight_layout()

def plot_avg_monthly(train):
    '''
    This function plots the average for each of the 9
    target variables in the fitbit dataset for each month
    '''
    count=0
    for i in train.drop(columns=['weekday','month']):
        plt.rc('figure', figsize=(16,9))
        count+=1
        plt.subplot(3, 3, count)
        I = i.upper().replace('_', ' ')
        ax = train[i].groupby(train.index.month).mean().plot.bar(width=.9, ec='black')
        plt.xticks(rotation=0)
        ax.set(title=f'Average {I} by Month', xlabel='Month')
    plt.tight_layout()

def plot_avg_weekday(train):
    '''
    This function plots the average for each of the 9
    target variables in the fitbit dataset for each day of the week
    '''
    count=0
    for i in train.drop(columns=['weekday','month']):
        plt.rc('figure', figsize=(16,9))
        count+=1
        plt.subplot(3, 3, count)
        I = i.upper().replace('_', ' ')
        ax = train[i].groupby(train.index.day_name()).mean().plot.bar(width=.9, ec='black')
        plt.xticks(rotation=20)
        ax.set(title=f'Average {I} by Weekday', xlabel='Weekday')
    plt.tight_layout()

def boxplot_weekday(train):
    '''
    This function visualizes boxplots for each of the 9
    target variables in the fitbit dataset for each day of the week
    '''
    count=0
    for i in train.drop(columns=['weekday','month']):
        plt.rc('figure', figsize=(16,9))
        count+=1
        plt.subplot(3, 3, count)
        I = i.upper().replace('_', ' ')
        train[i].reset_index()\
        .assign(weekday=lambda train: train.date.dt.day_name())\
        .pipe((sns.boxplot, 'data'), y=i, x='weekday')
    plt.tight_layout()