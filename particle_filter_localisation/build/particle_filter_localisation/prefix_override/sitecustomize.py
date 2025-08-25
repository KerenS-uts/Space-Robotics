import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/student/ros_ws/src/particle_filter_localisation/install/particle_filter_localisation'
