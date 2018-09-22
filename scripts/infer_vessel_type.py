"""
"""
import numpy as np


vessel_groups = {
    30: 'Fishing',
    1001: 'Fishing',
    1002: 'Fishing',
    35: 'Military',
    1021: 'Military',
    0: 'Not available',
    20: 'Other',
    23: 'Other',
    24: 'Other',
    25: 'Other',
    26: 'Other',
    27: 'Other',
    28: 'Other',
    29: 'Other',
    33: 'Other',
    34: 'Other',
    38: 'Other',
    39: 'Other',
    40: 'Other',
    41: 'Other',
    42: 'Other',
    43: 'Other',
    44: 'Other',
    45: 'Other',
    46: 'Other',
    47: 'Other',
    48: 'Other',
    49: 'Other',
    50: 'Other',
    51: 'Other',
    53: 'Other',
    54: 'Other',
    55: 'Other',
    56: 'Other',
    57: 'Other',
    58: 'Other',
    59: 'Other',
    36: 'Pleasure Craft/Sailing',
    37: 'Pleasure Craft/Sailing',
    21: 'Tug Tow',
    22: 'Tug Tow',
    31: 'Tug Tow',
    32: 'Tug Tow',
    52: 'Tug Tow',
    1003: 'Cargo',
    1004: 'Cargo',
    1016: 'Cargo',
    1018: 'Other',
    1020: 'Other',
    1022: 'Other',
    1012: 'Passenger',
    1013: 'Passenger',
    1014: 'Passenger',
    1015: 'Passenger',
    1019: 'Pleasure Craft/Sailing',
    1017: 'Tanker',
    1024: 'Tanker',
    1023: 'Tug Tow',
    1025: 'Tug Tow'
}

vessel_groups.update({num: 'Other' for num in range(1, 20)})
vessel_groups.update({num: 'Cargo' for num in range(70, 80)})
vessel_groups.update({num: 'Other' for num in range(90, 100)})
vessel_groups.update({num: 'Other' for num in range(1005, 1012)})
vessel_groups.update({num: 'Other' for num in range(100, 1000)})
vessel_groups.update({num: 'Tanker' for num in range(80, 90)})

vessel_groups_mod = {str(num): value for num, value in vessel_groups.items()}


def group_vessels(num):
    """
    Applies a group to a vessel depending on its vessel type.
    """
    x = str(num)
    try:
        return vessel_groups_mod[x[:2]]
    except KeyError:
        return np.nan
