import numpy as np
import pandas as pd

import cv2
from mapsource import MapSource

if __name__ == "__main__":
    df = pd.read_csv('datasets/data/time-series-19-covid-combined.txt')
    map_source = MapSource(df)
    map_source.date_world_map('2020-01-22')
    map_source.date_world_map('2020-03-22')
    map_source.date_world_map('2020-05-11')

    map_source.date_world_map('2020-01-22', status='Deaths', color='r')
    map_source.date_world_map('2020-03-22', status='Deaths', color='r')
    map_source.date_world_map('2020-05-11', status='Deaths', color='r')




