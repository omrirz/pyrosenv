import logging
import os
import sys
import importlib


class _HiddenPrints:
    """ Disable prints in import """

    def __init__(self):
        pass

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


# suppress the loggers
pyros_setup_level = logging.getLogger('pyros_setup').getEffectiveLevel()
rosout_level = logging.getLogger('rosout').getEffectiveLevel()
logging.getLogger('pyros_setup').setLevel(20000)
logging.getLogger('rosout').setLevel(20000)

with _HiddenPrints():
    try:
        import rospy
        import rosbag
        import roslaunch
        import rosgraph
        import rosnode
        import roslib
        import genpy
        import cv_bridge
    except ImportError:  # if ROS environment is not setup, we emulate it.
        import pyros_setup
        # this will use mysetup.cfg from pyros-setup instance folder
        pyros_setup.configurable_import().configure().activate()
        import rospy
        import rosbag
        import roslaunch
        import rosgraph
        import rosnode
        import roslib
        import genpy
        import cv_bridge
    finally:
        sys.modules['pyrosenv.std_msgs'] = std_msgs = importlib.import_module('std_msgs')
        sys.modules['pyrosenv.std_msgs.msg'] = std_msgs.msg = importlib.import_module('std_msgs.msg')
        sys.modules['pyrosenv.sensor_msgs'] = sensor_msgs = importlib.import_module('sensor_msgs')
        sys.modules['pyrosenv.sensor_msgs.msg'] = sensor_msgs.msg = importlib.import_module('sensor_msgs.msg')
        sys.modules['pyrosenv.sensor_msgs.point_cloud2'] = sensor_msgs.point_cloud2 = importlib.import_module(
            'sensor_msgs.point_cloud2')
        sys.modules['pyrosenv.rospy'] = rospy = importlib.import_module('rospy')
        sys.modules['pyrosenv.rosbag'] = rosbag = importlib.import_module('rosbag')
        sys.modules['pyrosenv.roslaunch'] = roslaunch = importlib.import_module('roslaunch')
        sys.modules['pyrosenv.rosgraph'] = rosgraph = importlib.import_module('rosgraph')
        sys.modules['pyrosenv.rosnode'] = rosnode = importlib.import_module('rosnode')
        sys.modules['pyrosenv.roslib'] = roslib = importlib.import_module('roslib')
        sys.modules['pyrosenv.genpy'] = genpy = importlib.import_module('genpy')
        sys.modules['pyrosenv.cv_bridge'] = cv_bridge = importlib.import_module('cv_bridge')

# get the loggers to their initial state
logging.getLogger('pyros_setup').setLevel(pyros_setup_level)
logging.getLogger('rosout').setLevel(rosout_level)

__all__ = [
    'rospy',
    'rosbag',
    'roslaunch',
    'rosgraph',
    'rosnode',
    'roslib',
    'genpy',
    'cv_bridge',
    'std_msgs',
    'sensor_msgs'
]
