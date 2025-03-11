
import pandas as pd
import numpy as np

from tsp import TSP


def thermal_integral(depths, times, values, dn=None, d0=None):
    """ Thermal integral for each year 
    Parameters
    ----------
    depths : array-like
        Depths of the nodes in the profile
    times : pd.DatetimeIndex
        Times for each measurement
    values : array-like
        Temperature values for each node at each time
    T0 : float
        Temperature offset
    d0 : int
        Starting depth
    dn : int
        maximum depth
    """
    _ix = [i for i, d in enumerate(depths) if (d0 is None or d0 <= d) and (dn is None or d <= dn)]
    _depths = np.atleast_1d(depths)[_ix]
    _values = np.atleast_2d(values)[:, _ix]
    norm = max(_depths) - min(_depths)  # normalize to mean C/year
    df = pd.DataFrame(index=times, columns=_depths, data=_values)
    df = df.resample("YE").mean()
    # subset only permafrost depths?

    def _integrate(S):
        isnan = S.isna()
        if isnan.iloc[-1] or isnan.all():
            return np.nan
        else:
            clean = S.dropna()
            return np.trapezoid(clean.values, clean.index)
    # strict na policy
    #df = df.apply(lambda S: np.trapz(S.values, S.index), axis=1)
   
    # relaxed na policy
    df = df.apply(_integrate, axis=1)
    
    return df / norm


def tsp_thermal_integral(t:TSP, dn: float, d0:float=0):
    return thermal_integral(t.depths, t.times, t.values, d0=d0, dn=dn)