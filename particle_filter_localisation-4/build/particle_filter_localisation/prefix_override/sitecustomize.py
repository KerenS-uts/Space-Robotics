import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/student/git/Space-Robotics/particle_filter_localisation-4/install/particle_filter_localisation'
