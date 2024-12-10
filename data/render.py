from IPython.display import display, HTML
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class DataRenderer:
    def show(self, df: DataFrame) -> None:
        if isinstance(df, Series):
            df = df.to_frame().T 
        display(HTML(df.to_html(index=False)))

    def plot(self, df: DataFrame, x_col: str, y_col: str, reverse = False) -> None:
        plt.figure(figsize=(8, 4))
        plt.scatter(df[x_col], df[y_col], alpha=0.6)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{x_col} vs {y_col}')
        if reverse:
            plt.gca().invert_yaxis()
        plt.show()

    def plot_bar(self, df: DataFrame, column: str) -> None:
        value_counts = df[column].value_counts().sort_index()
        plt.figure(figsize=(8, 4))
        value_counts.plot(kind='bar', color='skyblue')
        plt.title(f'Frequencies of {column}')
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def plot_density(self, df: DataFrame, column: str, scaled=True) -> None:
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

    def plot_key_frequency(self, data_dict: dict, title: str) -> None:
        key_counts = pd.Series({key: len(df) for key, df in data_dict.items()})
        key_counts = key_counts.sort_index()
        
        plt.figure(figsize=(8, 4))
        key_counts.plot(kind='bar', color='skyblue')
        plt.title(f'Frequencies of {title}')
        plt.xlabel(title)
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()

    def plot_year_frequency(self, df: DataFrame, date_col: str, year_range: range) -> None:
        if pd.api.types.is_string_dtype(df[date_col]):
            df['year'] = df[date_col].str[-4:].astype(int)
        
        year_counts = {year: 0 for year in year_range}

        for year in df['year']:
            if year in year_counts:
                year_counts[year] += 1

        year_counts_series = pd.Series(year_counts).sort_index()
        plt.figure(figsize=(8, 4))
        year_counts_series.plot(kind='bar', color='skyblue')
        plt.title('Frequency of Song Release Years')
        plt.xlabel('Year')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        if len(year_range) > 50:
            tick_positions = np.linspace(0, len(year_range) - 1, num=20, dtype=int)
            tick_labels = [year_range[i] for i in tick_positions]
            plt.xticks(tick_positions, tick_labels, rotation=45)
        else:
            plt.xticks(rotation=45)
        plt.show()