import numpy as np
import pandas as pd

from typing import Union, Optional
from functools import singledispatch

from tsp import TSP
from tspmetrics.classification import in_active_layer


""" Active layer thickness, top of permafrost, and thaw depth estimation """


def envelope_extrapolate(depths: Union[np.ndarray, pd.Series],
                         times: pd.DatetimeIndex,
                         values: np.ndarray, 
                         kind: str = 'alt') -> pd.Series:
    """ Extrapolate depth of 0 C isotherm using last two thawed nodes in a profile 
    using the maximum temperature at each depth over the year
    
    Parameters
    ----------
    depths : Union[np.ndarray, pd.Series]
        Depths of temperature observations
    times : pd.DatetimeIndex
        Times of temperature observations
    values : np.ndarray 
        Temperature observations
        
    Returns
    -------
    pd.Series
        The estimated depth of the 0 C isotherm at each time
    """
    df = pd.DataFrame(values, index=times, columns=depths)
    max_t = df.groupby(df.index.year).max()
    alt_max = max_t.apply(extrapolate_envelope_year, axis=1)
    min_t = -df.groupby(df.index.year).min()  # negative sign to use same function as alt_max
    alt_min = min_t.apply(extrapolate_envelope_year, axis=1)
    alt = pd.concat([alt_min,alt_max],axis=1).min(axis=1)  # shallowest intersection w/ 0C
    ttop = alt_max
    if kind == 'alt':
        return alt
    elif kind == 'ttop':
        return ttop
    else:
        raise ValueError("kind must be 'alt' or 'ttop'")


def envelope_interpolate(depths: Union[np.ndarray, pd.Series],
                         times: pd.DatetimeIndex,
                         values: np.ndarray,
                         kind='alt') -> pd.Series:
    """ Interpolate depth of 0 C isotherm between thawed and frozen nodes in a profile 
    using the maximum temperature at each depth over the year
    
    Parameters
    ----------
    depths : Union[np.ndarray, pd.Series]
        Depths of temperature observations
    times : pd.DatetimeIndex
        Times of temperature observations
    values : np.ndarray 
        Temperature observations
    kind : str
        either 'ttop' or 'alt', whether to return active layer thickness or top of permafrost
        
    Returns
    -------
    pd.Series
        The estimated depth of the 0 C isotherm at each time
    """
    df = pd.DataFrame(values, index=times, columns=depths)
    max_t = df.groupby(df.index.year).max()
    alt_max = max_t.apply(interpolate_envelope_year, axis=1)
    min_t = -df.groupby(df.index.year).min()  # negative sign to use same function as alt_max
    alt_min = min_t.apply(interpolate_envelope_year, axis=1)
    alt = pd.concat([alt_min,alt_max],axis=1).min(axis=1)  # shallowest intersection w/ 0C
    ttop = alt_max
    if kind == 'ttop':
        return ttop
    elif kind == 'alt':
        return alt
    else:
        raise ValueError("kind must be 'alt' or 'ttop'")


def interpolate_envelope_year(profile: pd.Series) -> pd.DataFrame:
    """ Interpolate depth of 0 C isotherm between thawed and frozen nodes in a profile
    
    Parameters
    ----------
    profile : pd.Series
        A profile of annual maximum temperatures with depth as the index

    Returns
    -------
    float
        The depth of the 0 C isotherm interpolated between the last thawed and first frozen nodes
    """
    W = np.where(profile < 0)
    if len(W[0]) == 0:
        return np.nan
    else:
        i_first_frozen = W[0][0]
    i_last_thawed = i_first_frozen - 1

    if i_last_thawed < 0:
        return np.nan

    d0 = profile.index[i_last_thawed]
    d1 = profile.index[i_first_frozen]
    t0 = profile[d0]
    t1 = profile[d1]

    dTdz =  (t1 - t0) / (d1 - d0) 

    d_zero = d0 + (0 - t0) / dTdz

    if np.sign(d_zero) != np.sign(d1):
        return np.nan
    
    return d_zero


def extrapolate_envelope_year(profile: pd.Series) -> pd.DataFrame:
    """ Extrapolate depth of 0C isotherm from last two thawed nodes in a profile
    Parameters
    ----------
    profile : pd.Series
        A profile of annual maximum temperatures with depth as the index

    Returns
    -------
    float
        The depth of the 0 C isotherm extrapolated using the last two thawed nodes
    """
    W = np.where(profile < 0)
    
    if len(W[0]) == 0:  # no frozen nodes
        return np.nan
    else:
        i_first_frozen = W[0][0]
    
    i_last_thawed = i_first_frozen - 1
    i_second_thawed = i_last_thawed - 1
    
    if i_second_thawed < 0:
        return np.nan
    
    d0 = profile.index[i_second_thawed]
    d1 = profile.index[i_last_thawed]
    t0 = profile[d0]
    t1 = profile[d1]
    
    dTdz =  (t1 - t0) / (d1 - d0) 
    
    d_zero = d1 + (0 - t1) / dTdz
    
    if np.sign(d_zero) != np.sign(d1):
        return np.nan
    
    return d_zero


def _thermal_gradients(depths, values) -> np.ndarray:
    return np.diff(values, axis=1) / np.diff(depths)


def deepest_al_node(depths, times, values, index=False, infer_start=False) -> pd.DataFrame:
    """ Determine deepest active layer node for each time step 
    
    np.nan if it can't find one
    """
    al = in_active_layer(depths, times, values, infer_start=infer_start).to_numpy()
    al[al != True] = False
    d = np.ma.array(np.repeat(np.atleast_2d(depths), repeats=al.shape[0], axis=0), mask=~al.astype('boolean'))
    deepest = np.apply_along_axis(lambda r: _get_deepest(r, depths, index=index), axis=1, arr=d)
    df = pd.DataFrame(data = deepest, index=times)
    return df


def _get_deepest(seq, depths, index):  
    if len(seq) == 0:  # possibly empty
        return np.nan
    else:
        i = np.argmax(seq)
        
        if index:
            return i
        
        return depths[i]  # an index


def deepest_thawed_al_node(depths, times, values, index=False, infer_start=False):
    """ The deepest thawed node in the active layer at each time  """
    al = in_active_layer(depths, times, values, infer_start=infer_start).to_numpy()
    al_thawed = al * (values > 0)
       
    deepest = np.apply_along_axis(lambda r: _get_deepest(np.where(r==1)[0], depths, index), axis=1, arr=al_thawed)
   
    return deepest


def shallowest_frozen_al_node(depths, times, values):
    """ The shallowest frozen node in the active layer at each time  """
    al = in_active_layer(depths, times, values).to_numpy()
    al_frozen = al * (values < 0)

    def get_shallowest(seq):  
        if len(seq) == 0:  # possibly empty
            return np.nan
        else:
            i = np.argmin(seq)
            return depths[i]  # an index
    
    shallowest = np.apply_along_axis(lambda r: get_shallowest(np.where(r==1)[0]), axis=1, arr=al_frozen)

    return shallowest


def instantaneous_zero_degree_isotherm(depths, times, values, method="extrapolate") -> pd.Series:
    """ Estimate the depth of the instantaneous zero-degree isotherm using either interpolation or extrapolation
    
    Parameters
    ----------
    depths : array-like
        Depths of the nodes in the profile
    times : pd.DatetimeIndex
        Times for each measurement
    values : array-like
        Temperature values for each node at each time
    method : str
        Method to use for estimating the zero-degree isotherm. Must be 'interpolate' or 'extrapolate'

    Returns
    -------
    pd.Series  
        Estimated depth of the instantaneous zero-degree isotherm for each time

    Extrapolation from the 2 thawed nodes above the zero degree isotherm is more accurate when there is 
    extensive phase change going on in permafrost (Riseborough, 2008)
    """
    dTdz = _thermal_gradients(depths, values)
    
    d = np.repeat(np.atleast_2d(depths[1:]), repeats=values.shape[0], axis=0)
    
    if method=='extrapolate':
        intercept = d + (0 - values[:, 1:]) / dTdz
    elif method=='interpolate':
        intercept = d + (0 - values[:, :-1]) / dTdz
    else:
        raise ValueError(f"Method {method} not recognized. Must be 'interpolate' or 'extrapolate'")

    df = pd.DataFrame(intercept, index=times, columns=depths[1:])

    # Identify the deepest positive-temperature observation within the AL
    o = deepest_thawed_al_node(depths, times, values, index=True, infer_start=True)
    o[o==0] = np.nan  # require 2 observations to extrapolate
    df['node'] = o

    freezeback_mask = shallowest_frozen_al_node(depths, times, values) < deepest_thawed_al_node(depths, times, values)
    df['freezeback'] = freezeback_mask

    def f(row):
        if row['freezeback']:  # possibly unreliable
            return np.nan
        if np.isnan(row['node']):  # no thawed nodes
            return np.nan
        else:
            i = int(row['node'])
            isotherm = row[depths[i]]

            if isotherm < depths[i]:
                return np.nan

            if (len(depths) > (i + 1)) and (isotherm > depths[i + 1]):
                return np.nan
        
        return isotherm
    
    result = df.apply(f, axis=1)
    result = result.groupby(result.index.year).max()

    return result


def zero_intercept(d1:float, d2:float, T1:float, T2:float, d3:Optional[float]=None) -> float:
    """ Calculate the zero-intercept of a thermal gradient
    
    @Parameters
    -----------
    d1 : float
        Depth at the first (uppermost) temperature measurement. Positive downwards.
    d2: float
        Depth at the second (second uppermost) temperature measurement. Positive downwards.
    T1 : float
        Temperature at d1
    T2 : float
        Temperature at d2
    d3 : float
        Depth at the third (lowermost) temperature measurement. Used as a check for the zero-intercept
    
    Returns
    -------
    float
        The depth at which the extrapolated thermal gradient crosses 0C. NaN if the intercept is below d2 or d3
    
    _____________________
    ----------|------o---
    ----------|-----/----
    -------d1-|----o-----
    ----------|---/------
    -------d2-|--o-------
    ----------|-/--------
    ----------|/---------
    ----------x----------
    ---------/|----------
    ---d3---o-|----------
    """
    dTdz =  (T2 - T1) / (d2 - d1) 
    zero_intercept = d2 + (0 - T2) / dTdz

    if zero_intercept < d2:
        return np.nan
    
    if d3 is not None:
        if zero_intercept > d3:
            zero_intercept = np.nan
    
    return zero_intercept


def top_of_permafrost(depths: Union[np.ndarray, pd.Series],
                      times: pd.DatetimeIndex,
                      values: np.ndarray,
                      estimation='extrapolate') -> pd.Series:
    """ Estimate the top of permafrost using the zero-degree isotherm 
    
    Parameters
    ----------
    depths : Union[np.ndarray, pd.Series]
        Depths of temperature observations
    times : pd.DatetimeIndex    
        Times of temperature observations
    values : np.ndarray
        Temperature observations
    estimation : str
        Method for estimating the top of permafrost. Options are 'extrapolate' and 'interpolate'

    Returns
    -------
    pd.Series
        The estimated top of permafrost at each time
    """
    if estimation == 'extrapolate':
        res = envelope_extrapolate(depths, times, values, kind='ttop')
    elif estimation == 'interpolate':
        res = envelope_interpolate(depths, times, values, kind='ttop')
    else:
        raise ValueError("estimation must be 'extrapolate' or 'interpolate'")
    
    return res


def active_layer_thickness(depths: Union[np.ndarray, pd.Series],
                      times: pd.DatetimeIndex,
                      values: np.ndarray,
                      estimation='extrapolate',
                      instantaneous=False) -> pd.Series:
    """ Estimate the active layer thickness using the zero-degree isotherm 
    
    Parameters
    ----------
    depths : Union[np.ndarray, pd.Series]
        Depths of temperature observations
    times : pd.DatetimeIndex    
        Times of temperature observations
    values : np.ndarray
        Temperature observations
    estimation : str
        Method for estimating the top of permafrost. Options are 'extrapolate' and 'interpolate'
    instantaneous : bool
        Whether to use instantaneous zero-degree isotherm estimation. Otherwise annual temperature envelope is used.

    Returns
    -------
    pd.Series
        The estimated top of permafrost at each time
    """
    if instantaneous:   
        res = instantaneous_zero_degree_isotherm(depths, times, values, method=estimation)
    else:
        if estimation == 'extrapolate':
            res = envelope_extrapolate(depths, times, values, kind='alt')
        elif estimation == 'interpolate':
            res = envelope_interpolate(depths, times, values, kind='alt')
        else:
            raise ValueError("estimation must be 'extrapolate' or 'interpolate'")
    
    return res


def tsp_top_of_permafrost(t:TSP, estimation='extrapolate') -> pd.Series:
    return top_of_permafrost(t.depths, t.times, t.values, estimation=estimation)


def tsp_active_layer_thickness(t:TSP, estimation='extrapolate', instantaneous=False) -> pd.Series:
    return active_layer_thickness(t.depths, t.times, t.values, estimation=estimation, instantaneous=instantaneous)
