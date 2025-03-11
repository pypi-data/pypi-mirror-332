"""
This module contains utility functions.
"""
import pandas as pd

def say(name: str) -> None:
    """
    Say hello to NAME.
    """
    print(f"Hello {name}!")
    
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def fillna_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces NaN values in numerical columns of the DataFrame with the mean value of the respective columns.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame that may contain NaN values in numerical
        columns.
    
    Returns
    -------
    pd.DataFrame
        A pandas DataFrame where NaN values in numerical columns have been replaced
        by the mean of their respective columns.
        
    Examples
    --------
    >>> df = pd.DataFrame({"A": [1, 2, None], "B": [3, None, 5]})
    >>> fillna_with_mean(df)
       A    B
    0  1.0  3.0
    1  2.0  4.0
    2  1.5  5.0
    
    """
    df = df.fillna(df.mean())
    return df

def fillna_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces NaN values in numerical columns of the DataFrame with the mean value of the respective columns.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame that may contain NaN values in numerical columns.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame where NaN values in numerical columns have been replaced
        by the mean of their respective columns.

    Examples
    --------
    >>> df = pd.DataFrame({"A": [1, 2, None], "B": [3, None, 5]})
    >>> fillna_with_mean(df)
       A    B
    0  1.0  3.0
    1  2.0  4.0
    2  1.5  5.0

    """
    df = df.fillna(df.mean())
    return df


from loguru import logger
import sys
logger.add(sys.stderr, level="DEBUG")
logger.info(f" {__name__=}")
logger.info("Running utils.py as a script.")
say("world")
logger.debug("Pls Help ! ")
logger.error(add(1, 1))
