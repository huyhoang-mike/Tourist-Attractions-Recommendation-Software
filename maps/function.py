import numpy as np
R = 6371
def deg2rad(deg):
    return deg*(np.pi/180)

def dist(lat1, long1, lat2, long2):
    d_lat = deg2rad(lat2 - lat1)
    d_long = deg2rad(long2 - long1)
    a = np.sin(d_lat/2)**2 + np.cos(deg2rad(lat1)) * np.cos(deg2rad(lat2)) * np.sin(d_long/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return float("{:.2f}".format(R * c))

