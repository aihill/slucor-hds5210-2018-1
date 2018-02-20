"""
This module defines a series of useful unit conversion functions.
"""

def lbs2kgs(lbs):
    """
    Convert pounds to kilograms.
    """
    return lbs * .454

def inches2ms(inches):
    """
    Convert inches to meters.
    """
    return inches * 2.54 / 100

def tsp2ml(tsp):
    """
    Convert teaspoons to milliliters
    """
    return tsp * 4.93

def mg_per_hour2g_per_day(mg_per_hour):
    """
    Convert milligrams per hour to grams per day
    """
    mg_per_day = mg_per_hour * 24
    g_per_day = mg_per_day / 1000
    return g_per_day

def los_points(days):
    """
    Return the LOS points based on days
    """
    if days <= 1:
        points = 0
    elif days >= 14:
        points = 7
    else:
        points = days
    
    return days
