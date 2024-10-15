class LPoint():
    def __init__(self, lon:float, lat:float):
        if isinstance(lon, float) == False:
            raise ValueError('lon must be float')
        if isinstance(lat, float) == False:
            raise ValueError('lon must be float')
        self.lat = lat
        self.lon = lon
