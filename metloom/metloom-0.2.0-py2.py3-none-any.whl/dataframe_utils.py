from logging import getLogger
from typing import List, Optional

import pandas as pd

from .variables import SensorDescription

LOG = getLogger("metloom.dataframe_utils")


def join_df(
    df: Optional[pd.DataFrame], new_df: Optional[pd.DataFrame], how="left",
    on=None, filter_unused=False
):
    """
    join two dataframes handling None
    Args:
        df: optional dataframe
        new_df: optional dataframe
        how: method for merging
        on: optional kwarg for DataFrame.join
        filter_unused: boolean, whether to filter out columns with _unused in
            then name

    Returns:
        The joined dataframes. This method prefers values from the first if
        columns are overlapping and renames the overlapping values from
        the `new_df` to <column>_unused
    """
    if df is None:
        result_df = new_df
    elif new_df is None:
        result_df = df
    else:
        try:
            result_df = df.join(new_df, how=how, on=on, rsuffix="_unused")
            if filter_unused:
                columns = result_df.columns
                final_columns = [c for c in columns if "_unused" not in c]
                result_df = result_df.filter(final_columns)
        except Exception as e:
            LOG.error("failed joining dataframes.")
            raise e

    return result_df


def merge_df(
    df: Optional[pd.DataFrame], new_df: Optional[pd.DataFrame], how="left"
):
    """
    join two dataframes. Assumes the dataframes are indexed on datetime
    Args:
        df: optional dataframe
        new_df: optional dataframe
    Returns:
        The merged dataframe
    """
    if df is None:
        result_df = new_df
    elif new_df is None:
        result_df = df
    else:
        try:
            result_df = pd.merge_ordered(df.reset_index(), new_df.reset_index())
            result_df.set_index("datetime", inplace=True)
            result_df.sort_index(inplace=True)
            if len(result_df.index.unique()) != len(result_df.index):
                LOG.error("Merging did not result in unique indexes. Killing"
                          " to avoid missing data")
                raise ValueError("Issue merging")
        except Exception as e:
            LOG.error("failed joining dataframes.")
            raise e

    return result_df


def append_df(df: Optional[pd.DataFrame], new_df: Optional[pd.DataFrame]):
    """
    append 2 dfs handling Nones
    Args:
        df: optional dataframe
        new_df: optional dataframe
    Returns:
        dataframe or None
    """
    if df is None:
        result_df = new_df
    elif new_df is None:
        result_df = df
    else:
        result_df = df.append(new_df)
    return result_df


def resample_df(raw_df: pd.DataFrame,
                variables: List[SensorDescription], interval: str = 'H'):
    """
    Resample an datatime indexed pandas dateframe to hourly or daily timer
    intervals.

    Args:
        raw_df: Pandas Dataframe containing a datetime index at an interval
            smaller than hourly.
        variables: List of SensorDescriptions to be found in the dataframe
        interval: Interval to resample to. Options are H = Hourly, D=Daily

    Returns:
        df: Pandas dataframe containing all the columns as raw_df but resampled
            to the requested interval
    """
    df = raw_df.copy()
    for sensor in variables:
        name = sensor.name
        if sensor.accumulated:
            df[name] = df[name].resample(interval).sum()
        else:
            df[name] = df[name].resample(interval).mean()

    df = df.dropna()
    return df
