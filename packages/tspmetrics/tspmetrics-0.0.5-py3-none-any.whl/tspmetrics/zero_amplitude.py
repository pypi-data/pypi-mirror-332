import pandas as pd
import numpy as np

from scipy.interpolate import interp1d
from tsp import TSP

from tspmetrics.amplitude import tsp_amplitude

""" Functions for calculating zero annual amplitude """


def dzaa_interpolated(amplitudes, zero_amplitude=0.1, dz=0.05):
    """ Calculate DZAA using (max-min)/2 as the amplitude.

    Parameters
    ----------
    amplitudes : pandas.DataFrame
        A DataFrame with depths as the columns and amplitudes as the values.
    zero_amplitude: float

    dz: float
        discretization interval for interpolating soil profile

    Returns
    -------
    pd.Series
        Series of depths of zero annual amplitude for each year in df.
    """
    def get_dzaa(S) -> float:
        ''' interpolate to get the amplitude at the zero_amplitude value '''
        f = interp1d(S.index, S.values)
        _z = np.arange(min(S.index), max(S.index), dz)
        _A = f(_z)
        dzaa = _z[np.argmin(np.abs(_A - zero_amplitude))]
        
        return dzaa
    
    return amplitudes.apply(get_dzaa, axis=1)


def dzaa_regressed(amplitudes: pd.DataFrame,
                   zero_amplitude=0.1,
                   cutoff=0.5) -> pd.Series:
    """Regresses the log of the amplitude ratios against the log of the depths.
    
    Parameteres
    ----------
    amplitudes : pandas.DataFrame
        A DataFrame with depths as the columns and amplitudes as the values.
    zero_amplitude : float
        The amplitude value at which we consider the amplitude to be zero.
    cutoff : float
        The minimum amplitude to be used in the regression.

    Returns
    -------
    pd.Series : Series of depths of zero annual amplitude for each year in df

    Method from Bonnaventure et al. 2015 'The ground thermal regime across the Mackenzie Valley Corridor'
    """
    return amplitudes.apply(lambda S: _regress_dzaa(S.index.values, S.values, zero_amplitude=zero_amplitude, cutoff=cutoff), axis=1)


def _regress_dzaa(depths, amplitudes, zero_amplitude=0.1, cutoff=0.5) -> float:
    """Regresses the log of the amplitude ratios against the log of the depths.

    Parameters
    ----------
    depths : array-like
        The depths of the amplitude measurements.
    amplitudes : array-like
        The amplitude at each depth.
    zero_amplitude : float
        The amplitude value at which we consider the amplitude to be zero.
    cutoff : float
        The minimum amplitude to be used in the regression.

    Returns
    -------
    float : Depth of zero annual amplitude. Depths always positive
    
    Method from Bonnaventure et al. 2015 'The ground thermal regime across the Mackenzie Valley Corridor'
    """
    if np.all(np.isnan(amplitudes)):
        return np.nan
    depths = np.abs(np.array(depths))  # require positive depths
    y = np.log(amplitudes[amplitudes > cutoff])
    x = depths[amplitudes > cutoff].astype('float64')  # depths column can be str sometimes
    x0, x1 = np.polynomial.polynomial.polyfit(x, y, 1)  # y = x0 + x1 * x
    zaa = (np.log(zero_amplitude) - x0) / x1
    
    return zaa


def tza(annual_means: pd.DataFrame, dzaa: pd.Series) -> pd.Series:
    """ Calculate the temperature at the depth of zero annual amplitude
    
    Parameters
    ----------
    annual_means: DataFrame
        Dataframe of annual temperature means with DatetimeIndex
    dzaa: Series
        Series of depths of zero annual amplitude for each year in annual_means
    """
    dzaa = np.abs(dzaa)
    depths = annual_means.columns.astype('float64')
    ix = dzaa.apply(func=lambda V: np.argmin(np.abs(V-depths)))
    t_dzaa = pd.Series(index=annual_means.index, data={"dzaa":np.nan}, name='dzaa')
    
    for i in range(ix.shape[0]):
        j = ix.iloc[i]
        if j == 0:
            continue
        t_dzaa.iloc[i] = annual_means.iloc[i,j]
    
    return t_dzaa

def get_dzaa_method(method: str):
    """ Return the function for calculating DZAA """
    
    methods = ['interpolated', 'regressed']
    
    if method not in methods:
        raise ValueError(f"method must be one of {methods}")
    elif method == 'interpolated':
        return dzaa_interpolated
    elif method == 'regressed':
        return dzaa_regressed
    else:
        raise ValueError(f"Unknown method {method}")
    

def dzaa(amplitudes, dzaa_method='interpolated', **kwargs) -> pd.Series:
    if dzaa_method == 'interpolated':
        return dzaa_interpolated(amplitudes, **kwargs)
    elif dzaa_method == 'regressed':
        return dzaa_regressed(amplitudes, **kwargs)
    else:
        raise ValueError(f"Unknown method {dzaa_method}")
    

def tsp_dzaa(t:TSP, dzaa_method='interpolated', amplitude_method='simple-all', **kwargs) -> pd.Series:
    """ Calculate the depth of zero annual amplitude for a TSP object
    
    Parameters
    ----------
    t : TSP
        A TSP object
    
    Returns
    -------
    pd.Series : Series of depths of zero annual amplitude for each year  
    """
    func_dzaa = get_dzaa_method(dzaa_method)
    amp = tsp_amplitude(t, method=amplitude_method)
    dzaa = func_dzaa(amp, **kwargs)
    
    return dzaa


def tsp_tza(t:TSP, dzaa_method='interpolated') -> pd.Series:
    """ Calculate the temperature at the depth of zero annual amplitude for a TSP object
    
    Parameters
    ----------
    t : TSP
        A TSP object
    
    Returns
    -------
    pd.Series : Series of temperatures at the depth of zero annual amplitude for each year
    """
    func_dzaa = get_dzaa_method(dzaa_method)
    amp = tsp_amplitude(t, method=amplitude_method)
    dzaa = func_dzaa(amp, **kwargs)

    t_dzaa = tza(t.yearly(), dzaa)
    
    return t_dzaa