import pandas as pd
from enum import Enum
# classifications

TALIK = "talik"
PERMAFROST = "permafrost"
ACTIVE_LAYER = "active layer"
UNKNOWN = "unknown"
UNFROZEN = "unfrozen ground"

# Values 

DATA_COMPLETENESS = 0.90


# Resampling offsets
class YearDef(Enum):
    
    @staticmethod
    def list():
        return list(map(lambda c: c.value, YearDef))
    
    CALENDAR = "calendar_year"
    HYDRO = "hydrological_year"


def get_resample_offset(year=YearDef.CALENDAR):
    if year == YearDef.CALENDAR:
        return pd.offsets.YearEnd()
    elif year == YearDef.HYDRO:
        return pd.offsets.YearEnd(month=9)
    else:
        raise ValueError(f"year must be one of {YearDef.list()}")
