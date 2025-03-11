import numpy as np
import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline as Interp
from functools import singledispatch

from tspmetrics.classification import in_permafrost
from tsp import TSP


def _tdd(depths, values, dz=0.01) -> float:
    """ Thaw depth duration increment for a single day 

    Parameters
    ----------
    depths : np.ndarray
        Depths of the temperature values
    values : np.ndarray
        Temperature values
    dz : float
        Depth increment for discretizing temperature profile
    
    Returns
    -------
    float
        Thaw depth duration increment for the day
    """
    T = Interp(depths, values, k=1, ext='const')
    z = np.arange(0, depths[-1], dz)
    Tz = T(z)
    thawed = np.heaviside(Tz, 0)
    
    return sum(thawed) * dz


@singledispatch
def thaw_depth_duration(depths: np.ndarray, times: "pd.DatetimeIndex", values:np.ndarray):
    """ 
    Calculate annual thaw depth duration

    Parameters
    ----------
    depths : np.ndarray
        Depths of the temperature values
    times : pd.DatetimeIndex
        Time axis of the temperature values
    values : np.ndarray
        Temperature values
    
    Returns
    -------
    pd.Series
        Thaw-depth duration for each year in the data frame

    Description
    -----------
    Based on Harp et al. (2016) doi:10.5194/tc-10-341-2016
    """
    # Ignore anything below permafrost table
    df = pd.DataFrame(index=times, columns=depths, data=values)
    in_pf = in_permafrost(depths,times,values)
    first_pf_node = in_pf.values.argmax(axis=1)
    df.insert(0, 'first_pf_node', first_pf_node)
    
    def skip_below(S):
        # Set temperatures below the top permafrost node to the same temperature as that node
        # This makes sure bottom taliks are not counted.
        S1 = S.iloc[1:]
        S1.iloc[int(S.iloc[0]):] = S1.iloc[int(S.iloc[0])]
        return S1

    cleaned = df.apply(skip_below, axis=1)

    r = cleaned.apply(lambda S: _tdd(S.ffill().index, S.ffill().values, name=S.name), axis=1)
    
    # If there's no permafrost, set to nan
    invalid = in_pf.apply(lambda S: ~S.any(), axis=1)
    r[invalid] = pd.NA
    # interpolate missing ffill
    Dbar = r.groupby(r.index.year).sum(min_count=365) / 365

    return Dbar


@thaw_depth_duration.register
def _(df: "pd.DataFrame"):
    depths = df.columns.astype('float64')
    times = df.index
    values = df.values
    return thaw_depth_duration(depths, times, values)


def tsp_tdd(t: TSP):
    """ Calculate thaw depth duration for a TSP object

    Parameters
    ----------
    t : TSP
        A TSP object
    
    Returns
    -------
    pd.Series
        Thaw-depth duration for each year in the data frame
    """
    return thaw_depth_duration(t.depths, t.times, t.values)