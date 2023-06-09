"""
A framework for both tracking and trajectory prediction using bounding boxes.
Given number of future frames of the trajectory is calculated by Kalman filtering from given number of past frames.

by DMTM Samaradiwakara
2023/06/10
based on SORT algorithm
"""

import numpy as np
import collections

from filterpy.kalman import KalmanFilter