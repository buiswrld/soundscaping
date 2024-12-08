from IPython.display import display, HTML
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

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