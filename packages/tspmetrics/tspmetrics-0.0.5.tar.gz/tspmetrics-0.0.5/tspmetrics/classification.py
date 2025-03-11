from tsp import TSP
import pandas as pd
import numpy as np


from tspmetrics.labels import DATA_COMPLETENESS
from tspmetrics import labels as lbl


def in_active_layer(depths, times, values, infer_start=True) -> pd.DataFrame:
    """ Whether a depth node is in the active layer
    
    Parameters
    ----------
    depths : list
        List of depths
    times : pd.DatetimeIndex
        Time axis of the temperature values
    values : np.ndarray
        Temperature values at daily resolution or better
    infer_start : bool
        Infer status before first valid data

    Returns
    -------
    pd.DataFrame
        Dataframe of type 'boolean' with the same shape as the input data

    Description
    -----------
    Active layer is defined using a purely thermal definition, (e.g. ).
    """
    df = pd.DataFrame(values, index=times, columns=depths)
    has_pos = df.rolling("365D").max() > 0  # require temperatures above zero
    # 2-year for cryotic catches edge cases where ground might be below zero but partially thawed 
    # (and where there's no permafrost because it thawed) 
    has_neg = df.rolling("730D").min() < 0  # require temperatures below zero
    both = (has_pos & has_neg).astype('boolean')

    # missing data mask
    completeness = (~df.isna()).rolling("365D").sum() / 365 
    mdm = (completeness > DATA_COMPLETENESS).astype('boolean')
    both[~mdm] = pd.NA

    # stop AL classification when first non-AL, non-NA depth is encountered
    both = both.cummin(axis=1, skipna=True)

    # interpolate between missing datas 
    d_interp = boolean_interpolate_(both, axis=1)
    t_interp = boolean_interpolate_(both, axis=0)

    inferred = d_interp & t_interp

    # infer status before valid data
    if infer_start:
        for depth in both.columns:
            fvi = both[depth].first_valid_index()
            if fvi is not None:
                both.loc[:fvi, depth] = both.loc[fvi,depth]
                inferred.loc[:fvi, depth] = True

    return both


def in_talik(depths, times, values, inal=None, inpf=None):
    """ Determine which depth nodes are within a talik.

    """
    in_pf = inpf if inpf is not None else in_permafrost(depths, times, values)
    below_pf_table = in_pf.cummax(axis=1)
    in_al = inal if inal is not None else in_active_layer(depths, times, values)
    na_mask = in_al.isna() | below_pf_table.isna()
    df = pd.DataFrame(values, index=times, columns=depths)
    thawed_allyear = df.rolling("365D", min_periods=1).min() > 0
    talik = ~(in_al | below_pf_table) & thawed_allyear
    talik[na_mask] = pd.NA

    return talik


def in_permafrost(depths, times, values, infer_start=True) -> pd.DataFrame:
    """ Determine which depth nodes are within permafrost.
     Data must be daily averages 
    Returns
    -------
    pd.DataFrame
        Dataframe of type 'boolean' with the same shape as the input data
    """
    df = pd.DataFrame(values, index=times, columns=depths)
    cryotic_2years = (df.rolling("730D").max() < 0).astype("boolean")

    # missing data mask
    completeness = (~df.isna()).rolling("730D").sum() / 730 
    mdm = completeness > DATA_COMPLETENESS 
    cryotic_2years[~mdm] = pd.NA

    # 'sufficient time' mask (2 yr since first valid observation) 
    valid_obs = (~df.isna()).astype('int64')
    valid_times = valid_obs.apply(lambda col: col*(valid_obs.index.astype('int64')), axis=0)
    dt = valid_times.apply(lambda col: col - col[col.first_valid_index()]) * 1e-9
    adequate_span = dt.cummax(axis=1) > (730 * 24 * 60 * 60) 
    #import pdb;pdb.set_trace()
    cryotic_2years[~adequate_span] = pd.NA

    # interpolate between missing data
    inferred = boolean_bilinear_interpolate_(cryotic_2years)

    # infer status before valid data
    if infer_start:
        for depth in cryotic_2years.columns:
            fvi = cryotic_2years[depth].first_valid_index()
            if fvi is not None:
                cryotic_2years.loc[:fvi, depth] = cryotic_2years.loc[fvi,depth]
                inferred.loc[:fvi, depth] = True

    return cryotic_2years


def tsp_warm_pf(t: TSP) -> pd.DataFrame:
    """ Warm permafrost estimation """
    return in_warm_permafrost(t.depths, t.times, t.values, infer_start=True)


def tsp_classification(t: TSP, infer_start=False) -> pd.DataFrame:
    """ Classify a profile as active layer, permafrost, talik or unfrozen ground """
    is_pf = in_permafrost(t.depths, t.times, t.values, infer_start=infer_start)
    is_al = in_active_layer(t.depths, t.times, t.values, infer_start=infer_start)
    is_talik = in_talik(t.depths, t.times, t.values)

    classfication = is_pf.copy()
    classfication[is_pf.fillna(False)] = lbl.PERMAFROST
    classfication[is_al.fillna(False)] = lbl.ACTIVE_LAYER
    classfication[is_talik.fillna(False)] = lbl.TALIK

    classfication[~is_pf.fillna(False) & ~is_al.fillna(False) & ~is_talik.fillna(False)] = lbl.UNFROZEN
    classfication[is_pf.isna() & is_al.isna() & is_talik.isna()] = lbl.UNKNOWN

    # talik w/ no permafrost ? unfrozen
    uf = classfication.apply(lambda S: set(S.unique()) == set([lbl.ACTIVE_LAYER, lbl.TALIK]), axis=1)
    return classfication


## Ready
def boolean_interpolate_(df: pd.DataFrame, axis=0) -> pd.DataFrame:
    """ Interpolate IN PLACE between boolean values along a single axis

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with boolean values
    axis : int
        Axis along which to interpolate (0 for rows, 1 for columns)
    
    Returns
    -------
    pd.DataFrame 
        Dataframe of indicating which values were interpolated (not the values themselves)

    Description
    -----------
    Will only interpolate beween values that are equal in both directions.
    """
    f = df.ffill(axis=axis)
    b = df.bfill(axis=axis)

    modified = (f==b) & (df.isna())

    df[f==b] = f[f==b]

    return modified


def boolean_bilinear_interpolate_(df: pd.DataFrame, strict=False) -> pd.DataFrame:
    """ Interpolate between boolean dataframe values IN PLACE considering both directions
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with boolean values and missing data (pandas.NA)
    strict : bool
        If True, only interpolate when both vertical and horizontal values are equal

    Returns
    -------
    pd.DataFrame
        boolean dataframe of which values were interpolated (not the values themselves)
    """
    if not df.dtypes.eq('boolean').all():
        raise ValueError("DataFrame must have boolean dtype for all columns")
    
    # Evaluate filling in all directions
    Vf = df.ffill(axis=0)
    Vb = df.bfill(axis=0)
    Hf = df.ffill(axis=1)
    Hb = df.bfill(axis=1)

    Veq = (Vf == Vb)  # verticals equal
    Heq = (Hf == Hb)  # horizontals equal
    
    is_na = df.isna()  # data we're interested in filling
    
    if strict:
        modified = (Veq & Heq) & (Vf == Hf) & is_na  # logically implies Vb == Hb
        df[modified] = Vf[modified]  # Vf could be anything here
    
    else:
        vf_isna = Vf.isna()
        hf_isna = Hf.isna()
        vb_isna = Vb.isna()
        hb_isna = Hb.isna()

        mod_V = Veq & ((Hf == Vf) | hf_isna) & ((Hb == Vf) | hb_isna) & is_na
        mod_H = Heq & ((Vf == Hf) | vf_isna) & ((Vb == Hf) | vb_isna) & is_na
        
        modified = mod_H | mod_V
        try:
            df[mod_V] = Vf[modified]
            df[mod_H] = Hf[modified]
        except:
            print("badbadbad")

    return modified


def in_warm_permafrost(depths, times, values, infer_start=False, cutoff=-2, inpf=None) -> pd.DataFrame:
    """ Whether permafrost is classified as warm for each depth and year"""
    permafrost = inpf if inpf is not None else in_permafrost(depths, times, values, infer_start=infer_start)
    permafrost = permafrost.resample("YE").min()
    df = pd.DataFrame(index=times, columns=depths, data=values)
    magt = df.resample("YE").mean()
    warm = (magt > cutoff).astype('boolean')
    warm_permafrost = warm & permafrost

    return warm_permafrost


def frozen_active_layer(depths, times, values):
    """ Whether active layer is completely frozen """
    al = in_active_layer(depths, times, values).to_numpy()
    al_thawed = al * (values > 0)

    return np.apply_along_axis(np.any, axis=1, arr=al_thawed).astype('boolean')
