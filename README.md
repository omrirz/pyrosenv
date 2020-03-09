# pyrosenv

Set an environment for easy work with ROS in python without setting things up

## Installation

```console
pip install pyrosenv
```

## Usage

For easy working with ROS in Python 3 in your IDE (Pycharm, VSCode, etc.) Do one or more of the following imports.
Actually after import pyrosenv you can import anything that you would import in ROS environemnt.

```python
# set things up and then import
import pyrosenv
import rospy
# ...

#import ros libraries
from pyrosenv import rospy
from pyrosenv import rosbag
from pyrosenv import roslaunch
from pyrosenv import rosgraph
from pyrosenv import roslib

# import std msgs
from pyrosenv.std_msgs.msg import Int16
from pyrosenv.std_msgs.msg import Bool
# ...

# import sensor msgs
from pyrosenv.sensor_msgs.msg import PointCloud2
msg = PointCloud2()
from pyrosenv.sensor_msgs import point_cloud2
point_cloud2.read_points(msg)
# ...
```

Then you can just use rospy, rosbag, std_msgs, sensor_msgs, etc. as you would in ROS environment.
