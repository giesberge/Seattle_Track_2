"""
"""
import numpy as np


def infer_vessel_type(status):
    """
    Built on the assumption it will be used to apply over a pandas Series
    (column in pandas DataFrame). Given a vessel's status, returns all
    possible types based on previous observations within the data.

    Note: sets are weird to have as a column type
    """
    possible_types = {
        'at anchor': {1004, 1005, 1010, 1012, 1018, 1019, 1024, 1025},
        'moored': {31, 35, 52, 70, 90, 1004, 1005, 1010, 1011, 1012, 1013, 1018,
                   1019, 1020, 1022, 1024, 1025},
        'not under command': {0},
        'power-driven vessel towing astern': {1025},
        'reserved for future use': {1025, 1005},
        'restricted maneuverability': {52, 1005, 1010, 1018, 1024},
        'undefined': {0, 30, 50, 51, 60, 99, 1003, 1005, 1012, 1018, 1019, 1024, 1025},
        'under way using engine': {0, 23, 30, 31, 32, 35, 37, 50, 52, 53, 60, 70, 79, 90, 1001, 1004, 1005, 1010, 1011, 1012, 1013, 1018, 1019, 1020, 1022, 1025}
        }
    try:
        return str(possible_types[status])
    except KeyError:
        return np.nan


def infer_vessel_status(vessel_type):
    """
    Inverse of infer_vessel_type. Returns vessel status based on presence
    within the types set.
    """
    possible_statuses = {0: {'not under command', 'undefined', 'under way using engine'},
                         23: {'under way using engine'},
                         30: {'undefined', 'under way using engine'},
                         31: {'moored', 'under way using engine'},
                         32: {'under way using engine'},
                         35: {'moored', 'under way using engine'},
                         37: {'under way using engine'},
                         50: {'undefined', 'under way using engine'},
                         51: {'undefined'},
                         52: {'moored', 'restricted maneuverability', 'under way using engine'},
                         53: {'under way using engine'},
                         60: {'undefined', 'under way using engine'},
                         70: {'moored', 'under way using engine'},
                         79: {'under way using engine'},
                         90: {'moored', 'under way using engine'},
                         99: {'undefined'},
                         1001: {'under way using engine'},
                         1003: {'undefined'},
                         1004: {'at anchor', 'moored', 'under way using engine'},
                         1005: {'at anchor',
                                'moored',
                                'reserved for future use',
                                'restricted maneuverability',
                                'undefined',
                                'under way using engine'},
                         1010: {'at anchor',
                                'moored',
                                'restricted maneuverability',
                                'under way using engine'},
                         1011: {'moored', 'under way using engine'},
                         1012: {'at anchor', 'moored', 'undefined', 'under way using engine'},
                         1013: {'moored', 'under way using engine'},
                         1018: {'at anchor',
                                'moored',
                                'restricted maneuverability',
                                'undefined',
                                'under way using engine'},
                         1019: {'at anchor', 'moored', 'undefined', 'under way using engine'},
                         1020: {'moored', 'under way using engine'},
                         1022: {'moored', 'under way using engine'},
                         1024: {'at anchor', 'moored', 'restricted maneuverability', 'undefined'},
                         1025: {'at anchor',
                                'moored',
                                'power-driven vessel towing astern',
                                'reserved for future use',
                                'undefined',
                                'under way using engine'}
                         }
    try:
        return str(possible_statuses[vessel_type])
    except KeyError:
        return np.nan


def replace_status_and_vesseltypes(df, inferred_vessels_col, inferred_status_col):
    """
    We only need to infer vessel type if the type is null but status is present.
    We only need to infer vessel status if the status is null but type is present.

    This function is very hardcoded.
    """
    new_df = df.copy()
    new_df['VesselType'][df['VesselType'].isnull()] = inferred_vessels_col
    new_df['Status'][df['Status'].isnull()] = inferred_status_col

    return new_df
