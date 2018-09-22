"""
"""
type_hierarchy = {
    30: 4,
    36: 5
}

status = {
    'under way using engine(s)': 6,
    'not under command': 1,
    'at anchor': 1,
    'engaged in fishing': 4,
    'restricted maneuverability': 1,
    'under way sailing': 5,
    'power driven vessel towing astern': 6,
}


def hierarchy_row(ship1, ship2):
    """
    """
    try:
        vessel_type_1 = ship1['VesselType']
    except KeyError:
        vessel_type_1 = 6

    try:
        vessel_type_2 = ship2['VesselType']
    except KeyError:
        vessel_type_2 = 6

    place_1 = min(type_hierarchy[vessel_type_1], status[ship1['Status']])
    place_2 = min(type_hierarchy[vessel_type_2], status[ship2['Status']])

    if place_1 < place_2:
        return "Ship 1 stand on vessel, ship 2 give way vessel"
    if place_1 > place_2:
        return "Ship 1 give way vessel, ship 2 stand on vessel"
    else:
        return "Determine COLREGs interaction"
