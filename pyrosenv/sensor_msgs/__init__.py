import sensor_msgs.msg
from sensor_msgs.msg import *
from . import point_cloud2

import importlib
msg = importlib.import_module('sensor_msgs.msg')
point_cloud2 = importlib.import_module('sensor_msgs.point_cloud2')

__all__ = ['msg', 'point_cloud2']
