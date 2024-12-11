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
        plt.style.use('seaborn-v0_8-pastel')
        plt.rcParams['font.family'] = 'Osaka'
        plt.rcParams['font.size'] = 10

    # Reference: (10)
    def show(self, df: DataFrame) -> None:
        """
        Displays the DataFrame in an HTML table format.
        
        Parameters:
        df (DataFrame or Series): The DataFrame or Series to display.
        """
        # Reference: (16)
        if isinstance(df, Series):
            df = df.to_frame().T 
        display(HTML(df.to_html(index=False)))

    # Reference: (3)
    def split_show(self, df1, df2, title1, title2) -> None:
        """
        Renders two DataFrames side by side in HTML table format.
        args:
            df1 (DataFrame): First dataframe to display on the left side
            df2 (DataFrame): Second dataframe to display on the right side
            title1: A title for the first DataFrame
            title2: A title for the second DataFrame
        return:
            None
        """
        jsx = f"""
        <div style="display: flex; justify-content: space-around;">
            <div>
                <h3>{title1}</h3>
                {df1.to_html(index=False)}
            </div>
            <div>
                <h3>{title2}</h3>
                {df2.to_html(index=False)}
            </div>
        </div>
        """
        # Reference: (10)
        display(HTML(jsx))

    # Reference: (11)
    def plot(self, df: DataFrame, x_col: str, y_col: str, reverse=False) -> None:
        """
        Plots a scatter plot of two columns from a given DataFrame.
        
        Parameters:
        df (DataFrame): The DataFrame containing the data.
        x_col (str): The name of the column to use for the x-axis.
        y_col (str): The name of the column to use for the y-axis.
        reverse (bool): Whether to reverse the y-axis. Useful for rank data (1 > 100).
        
        Returns:
        None
        """
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

    # Reference: (11)
    def plot_bar(self, df: DataFrame, column: str) -> None:
        """
        Plots a bar graph of the frequency of values in a column.
        
        Parameters:
        df (DataFrame): The DataFrame containing the data.
        column (str): The name of the column to plot.
        
        Returns:
        None
        """
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

    # Reference: (11, 12)
    def plot_density(self, df: DataFrame, column: str, title=None, scaled=True) -> None:
        """
        Plots a density graph of the values in a column.
        
        Parameters:
        df (DataFrame): The DataFrame containing the data.
        column (str): The name of the column to plot.
        title (str): The title of the plot. If no title is provided, the column name is used.
        scaled (bool): Whether to scale the x-axis to a range 0-100.
        
        Returns:
        None
        """
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

    # Reference: (11)
    def plot_key_frequency(self, data_dict: dict, title: str) -> None:
        """
        Plot a bar graph of the frequency of keys in a dictionary of DataFrames.
        
        Parameters:
        data_dict (dict): A dictionary where keys are labels and values are DataFrames.
        title (str): The title of the plot.
        
        Returns:
        None
        """
        # Preprocess
        key_counts = pd.Series({key: len(df) for key, df in data_dict.items()})
        key_counts = key_counts.sort_index()

        # Setup
        plt.figure(figsize=(8, 4))
        key_counts.plot(kind='bar')

        # Label
        plt.title(f'{title} Frequency Distribution')
        plt.xlabel(title)
        plt.ylabel('Count')

        # Format
        plt.xticks(rotation=45)

        # Show
        plt.show()

    # Reference: (11)
    def plot_year_frequency(self, df: DataFrame, date_col: str, year_range: range) -> None:
        """
        Plot a bar graph of the frequency of years that songs were released.
        
        Parameters:
        df (DataFrame): The DataFrame containing the data.
        date_col (str): The name of the column containing the dates. Can accept both raw year (e.g. 2021) or full date, if year is the last 4 characters (e.g. 01/01/2021, Jan 1 2025).
        year_range (range): The range of years to include in the plot.
        
        Returns:
        None
        """
        # Preprocess
        # Reference: (13)
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

        # Reference: (14, 15)
        if len(year_range) > 50:
            tick_positions = np.linspace(0, len(year_range) - 1, num=20, dtype=int)
            tick_labels = [year_range[i] for i in tick_positions]
            plt.xticks(tick_positions, tick_labels, rotation=45)
        else:
            plt.xticks(rotation=45)

        # Show
        plt.show()