# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/gyc/catkin_ws_lidar_slam/devel_isolated/joy;/home/gyc/catkin_ws_lidar_slam/devel_isolated/rplidar_ros;/home/gyc/catkin_ws_lidar_slam/devel_isolated/delta_lidar;/home/gyc/catkin_ws_lidar_slam/devel_isolated/autolabor_pro1_driver;/home/gyc/catkin_ws_lidar_slam/devel_isolated/autolabor_keyboard_control;/home/gyc/catkin_ws_lidar_slam/devel_isolated/autolabor_description;/home/gyc/catkin_ws_lidar_slam/devel_isolated/autolabor_box_launch;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/gyc/catkin_ws_lidar_slam/devel_isolated/autolabor_box_launch/env.sh')

output_filename = '/home/gyc/catkin_ws_lidar_slam/build_isolated/autolabor_box_launch/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
