import pandas as pd
from functools import singledispatch
from tsp import TSP

from tspmetrics.labels import YearDef, get_resample_offset
"""
Functions for calculating annual amplitude
"""


@singledispatch
def annual_amplitude(depths, times, values, method='simple-all', year_definition=YearDef.CALENDAR) -> pd.DataFrame:
    """ Calculate annual amplitude 
    Parameters
    ----------
    depths : list
        List of depths
    times : list
        List of times
    values : list
    method : str
        Method for calculating annual amplitude. Options are 'simple-all' (extrema using all values) 
        and 'simple-mm' (extrema of monthly means)
    year_definition : str
        Definition of a year. Valid options are provided in labels.YearDef

    Returns
    -------
    pd.DataFrame : DataFrame with annual amplitudes
    """
    valid_options = ['simple-all', 'simple-mm']
    if method == 'simple-all':
        A = simple_annual_maxmin(depths, times, values, year_definition=year_definition)
    elif method == 'simple-mm':
        A = monthly_mean_annual_maxmin(depths, times, values, year_definition=year_definition)
    else:
        raise ValueError(f'method must be one of {"".join(valid_options)}')
    
    return A


@annual_amplitude.register
def _(df: "pd.DataFrame", method='simple-all', year_definition=YearDef.CALENDAR) -> pd.DataFrame:
    depths = df.columns
    times = df.index
    values = df.values
    aa = annual_amplitude(depths,
                          times,
                          values, method=method,
                          year_definition=year_definition)
    
    return aa


def simple_annual_maxmin(depths, times, values, year_definition=YearDef.CALENDAR) -> pd.DataFrame:
    """ Amplitude over year, based on all available data """
    df = pd.DataFrame(index=pd.DatetimeIndex(times), columns=depths, data=values)
    df_annual = df.resample(get_resample_offset(year_definition))
    _range = df_annual.max() - df_annual.min()
    A = _range / 2

    return A



def monthly_mean_annual_maxmin(depths, times, values, year_definition=YearDef.CALENDAR) -> pd.DataFrame:
    """ Amplitude over year, based on monthly means """
    df = pd.DataFrame(index=times, columns=depths, data=values)
    monthly = df.resample("ME").mean()
    annual = df.resample(get_resample_offset(year_definition))
    _range = annual.max() - annual.min()
    A = _range / 2
    return A


def tsp_amplitude(t:TSP, method: str='simple-all', year_definition=YearDef.CALENDAR) -> pd.DataFrame:
    """ Calculate annual amplitude for a TSP object
    Parameters
    ----------
    t : TSP
        A TSP object
    method : str
        Method for calculating annual amplitude. Options are 'simple-all' and 'simple-mm'
    
    Returns
    -------
    pd.DataFrame : DataFrame with annual amplitudes
    """
    return annual_amplitude(t.depths, t.times, t.values, method, year_definition)