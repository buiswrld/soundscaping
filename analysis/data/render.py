from IPython.display import display, HTML
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

def show(df: DataFrame) -> None:
    if isinstance(df, Series):
        df = df.to_frame().T 
    display(HTML(df.to_html(index=False)))