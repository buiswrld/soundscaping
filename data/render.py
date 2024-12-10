from IPython.display import display, HTML
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.ticker import PercentFormatter

class DataRenderer:
    def __init__(self):
        sns.set_palette('pastel')

    def show(self, df: DataFrame) -> None:
        if isinstance(df, Series):
            df = df.to_frame().T 
        display(HTML(df.to_html(index=False)))

    def plot(self, df: DataFrame, x_col: str, y_col: str, reverse=False) -> None:

        # Setup
        plt.figure(figsize=(8, 4))
        plt.scatter(df[x_col], df[y_col], alpha=0.6)

        # Label
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{x_col} vs {y_col}')

        # Format
        if reverse:
            plt.gca().invert_yaxis()

        # Show
        plt.show()

    def plot_bar(self, df: DataFrame, column: str) -> None:

        # Preprocess
        value_counts = df[column].value_counts().sort_index()

        # Setup
        plt.figure(figsize=(8, 4))
        value_counts.plot(kind='bar', color='skyblue')

        # Label
        plt.title(f'Frequencies of {column}')
        plt.xlabel(column)
        plt.ylabel("Frequency")

        # Show
        plt.show()

    def plot_density(self, df: DataFrame, column: str, title=None, scaled=True) -> None:

        # Preprocess
        if not title:
            title = column
        
        # Setup
        plt.figure(figsize=(8, 4))
        sns.kdeplot(df[column], fill=True, bw_adjust=0.1, cut=1)

        # Label
        plt.title(f'Density Distribution of {title}')
        plt.xlabel(title)
        plt.ylabel('Density')

        # Format
        if not scaled:
            plt.xlim(0, df[column].max() + 10)
        else:
            plt.xlim(0, 100)
        plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))

        # Show
        plt.show()

    def plot_key_frequency(self, data_dict: dict, title: str) -> None:

        # Preprocess
        key_counts = pd.Series({key: len(df) for key, df in data_dict.items()})
        key_counts = key_counts.sort_index()

        # Setup
        plt.figure(figsize=(8, 4))
        key_counts.plot(kind='bar', color='skyblue')

        # Label
        plt.title(f'Frequencies of {title}')
        plt.xlabel(title)
        plt.ylabel('Frequency')

        # Format
        plt.xticks(rotation=45)

        # Show
        plt.show()

    def plot_year_frequency(self, df: DataFrame, date_col: str, year_range: range) -> None:

        # Preprocess
        if pd.api.types.is_string_dtype(df[date_col]):
            df['year'] = df[date_col].str[-4:].astype(int)
        
        year_counts = {year: 0 for year in year_range}
        for year in df['year']:
            if year in year_counts:
                year_counts[year] += 1

        year_counts_series = pd.Series(year_counts).sort_index()

        # Setup
        plt.figure(figsize=(8, 4))
        year_counts_series.plot(kind='bar', color='skyblue')

        # Label
        plt.title('Frequency of Song Release Years')
        plt.xlabel('Year')
        plt.ylabel('Frequency')

        # Format
        plt.xticks(rotation=45)

        if len(year_range) > 50:
            tick_positions = np.linspace(0, len(year_range) - 1, num=20, dtype=int)
            tick_labels = [year_range[i] for i in tick_positions]
            plt.xticks(tick_positions, tick_labels, rotation=45)
        else:
            plt.xticks(rotation=45)

        # Show
        plt.show()