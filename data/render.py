from IPython.display import display, HTML
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def show(df: DataFrame) -> None:
    if isinstance(df, Series):
        df = df.to_frame().T 
    display(HTML(df.to_html(index=False)))

def plot(df: DataFrame, x_col: str, y_col: str, reverse = False) -> None:
    plt.figure(figsize=(8, 4))
    plt.scatter(df[x_col], df[y_col], alpha=0.6)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{x_col} vs {y_col}')
    if reverse:
        plt.gca().invert_yaxis()
    plt.show()

def plot_bar(df: DataFrame, column: str) -> None:
    value_counts = df[column].value_counts().sort_index()
    plt.figure(figsize=(8, 4))
    value_counts.plot(kind='bar', color='skyblue')
    plt.title(f'Frequencies of {column}')
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_density(df: DataFrame, column: str, scaled=True) -> None:
    plt.figure(figsize=(8, 4))
    sns.kdeplot(df[column], fill=True, color='skyblue')
    plt.title(f'Frequency Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Density')
    if not scaled:
        plt.xlim(0, df[column].max()+10)
    else:
        plt.xlim(0, 100) 
    plt.show()

def plot_key_frequency(data_dict: dict, title: str) -> None:
    key_counts = pd.Series({key: len(df) for key, df in data_dict.items()})
    key_counts = key_counts.sort_index()
    
    plt.figure(figsize=(8, 4))
    key_counts.plot(kind='bar', color='skyblue')
    plt.title(f'Frequencies of {title}')
    plt.xlabel(title)
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()