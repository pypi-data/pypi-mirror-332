# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from digitaleye_msgs/Constants.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Constants(genpy.Message):
  _md5sum = "954bc0046723ceea48ee103bf92aca13"
  _type = "digitaleye_msgs/Constants"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# STATE CONSTANTS
uint32 STATE_OFF=1000
uint32 STATE_STOP=1001
uint32 STATE_INIT=1002
uint32 STATE_SETUP=1003
uint32 STATE_CALIBRATING=1004
uint32 STATE_TRACKING=1005
uint32 STATE_EMERGENCY=1006

# STATUS CONSTANTS
uint32 STATUS_OFF=2000
uint32 STATUS_STARTING=2001
uint32 STATUS_HEALTHY=2002
uint32 STATUS_FAILED=2003

# SUBSYSTEM IDENTIFIERS
uint32 SYSTEM_DIGITALEYE=3000
uint32 SYSTEM_MACHINE_VISION=3001
uint32 SYSTEM_IOT_GATEWAY=3002
uint32 SYSTEM_DEMS=3003
uint32 SYSTEM_POSITION=3004
uint32 SYSTEM_C2=3005

# MICROSERVICE IDENTIFIERS
uint32 MICROSERVICE_SYSTEM_CONFIG=4000
uint32 MICROSERVICE_STATUS_MANAGER=4001
uint32 MICROSERVICE_MVC_ADAPTER=4002
uint32 MICROSERVICE_IOT_ADAPTER=4003
uint32 MICROSERVICE_BOOKINGS_MANAGER=4004
uint32 MICROSERVICE_LOGGER=4005
uint32 MICROSERVICE_SENSOR_FUSION=4006
uint32 MICROSERVICE_MGS_MONITORING=4007
uint32 MICROSERVICE_MGS_MANAGER=4008
uint32 MICROSERVICE_MVC_CAMERA_MANAGER=4009
uint32 MICROSERVICE_MVC_LIDAR_MANAGER=4010
uint32 MICROSERVICE_MVC_ZONE_MANAGER=4011
uint32 MICROSERVICE_POSITION_ADAPTER=4012
uint32 MICROSERVICE_C2_ADAPTER=4013
uint32 MICROSERVICE_ALLOCATIONS_MANAGER=4014
uint32 MICROSERVICE_UAV_MANAGER=4015
uint32 MICROSERVICE_UAV_CONFORMANCE=4016
uint32 MICROSERVICE_CALIBRATION_MANAGER=4017

# SENSOR TYPE IDENTIFIERS
uint32 SENSOR_CAMERA=5000
uint32 SENSOR_LIDAR=5001
uint32 SENSOR_LOCATOR=5002
uint32 SENSOR_RTK=5003
uint32 SENSOR_COMPASS=5004
uint32 SENSOR_RADAR=5005

# REFERENCE FRAMES
uint32 FRAME_GLOBAL=6000
uint32 FRAME_DIGITALEYE=6001

# POLE IDENTIFIERS
uint32 POLE_P1=7000
uint32 POLE_S1=7001
uint32 POLE_S2=7002
uint32 POLE_S3=7003
uint32 POLE_L1=7004

# POSITION ENGINE NODE IDENTIFIERS
uint32 POSENG_POLE_MANAGER=8000
uint32 POSENG_STREAMER=8001
uint32 POSENG_SOLVER=8002
uint32 POSENG_SAMPLER=8003
uint32 POSENG_SURVEYOR=8004
uint32 POSENG_PORT=13013

# GNSS STATES
uint32 GNSS_NO_FIX=8100
uint32 GNSS_TIME_FLOAT=8101
uint32 GNSS_TIME_FIX=8102
uint32 GNSS_DEAD_FLOAT=8103
uint32 GNSS_DEAD_FIX=8104
uint32 GNSS_GPS_DEAD_FLOAT=8105
uint32 GNSS_GPS_DEAD_FIX=8106
uint32 GNSS_2D_FLOAT=8107
uint32 GNSS_2D_FIX=8108
uint32 GNSS_3D_FLOAT=8109
uint32 GNSS_3D_FIX=8110
uint32 GNSS_RTK_FLOAT=8111
uint32 GNSS_RTK_FIX=8112

# CORRECTION SOURCE
uint32 GNSS_NO_CORR=8200
uint32 GNSS_BASE_CORR=8201
uint32 GNSS_NTRIP_CORR=8202

# UAV IDENTIFIERS
uint32 UAV_UOBX1=8100
uint32 UAV_UOBX2=8101

# NOTIFICATION PRIORITIES
uint32 NOTIFICATION_INFO=9000
uint32 NOTIFICATION_IMPORTANT=9001
uint32 NOTIFICATION_CRITICAL=9002

# METRICS DICTIONARY
string REALSENSE_DEPTH_PROJECTOR_TEMPERATURE = Depth Projector Temp.
string REALSENSE_DEPTH_ASIC_TEMPERATURE = Depth ASIC Temp.
string REALSENSE_DEPTH_FRAME_DROPS = Depth Frame Drops

string CPU1_BOARD_USAGE = CPU1 Usage%
string CPU2_BOARD_USAGE = CPU2 Usage%
string CPU3_BOARD_USAGE = CPU3 Usage%
string CPU4_BOARD_USAGE = CPU4 Usage%
string CPU5_BOARD_USAGE = CPU5 Usage%
string CPU6_BOARD_USAGE = CPU6 Usage%

string GPU_BOARD_USAGE = GPU Usage%

string JETSON_POWER_MODE =      Jetson Power Mode
string JETSON_RAM_USAGE =       Jetson RAM Usage
string JETSON_DISK_USAGE =      Jetson Disk Usage
string JETSON_FAN_SPEED =       Jetson Fan Speed
string JETSON_CPU_TEMPERATURE = Jetson CPU Temp.
string JETSON_GPU_TEMPERATURE = Jetson GPU Temp.
string JETSON_POWER_AVERAGE =   Jetson Power Avg.
string JETSON_UP_TIME =         Jetson Up Time

# Pole Metrics
string POLE_POSITION_LAT = Pole Latitude
string POLE_POSITION_LON = Pole Longitude
string POLE_POSITION_ALT = Pole Altitude
string POLE_POSITION_ALT_MSL = Pole Altitude (MSL)
string POLE_POSITION_VDOP = VDOP
string POLE_POSITION_HDOP = HDOP
string POLE_ORIENTATION = Pole Orientation
string POLE_NUM_SATS = No. of Satellites
string POLE_FIX_TYPE = GNSS Fix Type
string POLE_CORRECTIONS = RTK Corrections
string POLE_MODE = Operation Mode

# COMPASS
uint8 CMPS12_ADDRESS = 96
string COMPASS_MAGNETOMETER_X_VALUE = Magnetometer X
string COMPASS_MAGNETOMETER_Y_VALUE = Magnetometer Y
string COMPASS_MAGNETOMETER_Z_VALUE = Magnetometer Z
string COMPASS_ROLL_VALUE = Roll
string COMPASS_PITCH_VALUE = Pitch
string COMPASS_CALIBRATION_STATUS = Inertial sensor calibration Status

# UAV metrics
string UAV_STATE = UAV State
string UAV_TOLZ = UAV TOLZ
string UAV_NAME = UAV Name

# IOT metrics
string IOT_ISSUE = Issue

string QPE_CPU_LOAD = CPU Load
string QPE_LOSS_RATE = QPE Loss Rate
string QPE_NETWORK_LOSS_RATE = Network Loss Rate

string LOC_CONNECTION = Connection Status
string LOC_TEMP = Temperature

# SENSOR FUSION IDs

uint32 FASTLOOP_ID_START =     0
uint32 OBJECTS_ID_START =      100
uint32 PS_FASTLOOP_ID_START =      1000
uint32 PS_OBJECTS_ID_START =       1100

uint32 MVC_OBJECT_ID_NN_START = 1500
uint32 MVC_OBJECT_ID_CAMERA_START = 1600
uint32 MVC_OBJECT_ID_LIDAR_START =  1800

uint32 IOT_OBJECTS_ID_START =       2000
uint32 IOT_OBJECTS_ID_END =         3000
uint32 UAV_OBJECTS_ID_START =       10000

string SENSOR_FUSION_VALID_THRESHOLD = Set the threshold for an object to become valid
string SENSOR_FUSION_DELETE_THRESHOLD = Set the threshold for deleting an object
string SENSOR_FUSION_DISTANCE_THRESHOLD = Set the threshold for object distance association

string SENSOR_FUSION_DELETE_PERIOD = Set the period in secs for an object to be deleted
string SENSOR_FUSION_FILTER_FREQ = Set the frequency in Hz of the filtering
string SENSOR_FUSION_SYSTEM_TYPE = Set the type of the sensor fusion system

# MVS CONFIGURATION CONSTANTS
string START_MVC_AS_MAIN =      Start board as main Machine Vision Computer
string START_MVC_AS_SECONDARY = Start board as secondary Machine Vision Computer
string STOP_MVC =               Stop Machine Vision Computer

string CAMERA_EUCLIDEAN_FILTER_TOLERANCE =      Euclidean Segmentation tolerance for camera pointcloud
string CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES =    Minimum number of points for camera Euclidean Segmentation
string CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES =    Maximum number of points for camera Euclidean Segmentation
string CAMERA_OUTLIERS_REMOVAL_MEAN =           Mean for camera statistical noise removal Filter
string CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION =  Standard Deviation for camera statistical noise removal Filter

string CAMERA_SPATIAL_FILTER_ALPHA =        Alpha value for Realsense Spatial Edge Preserving filter
string CAMERA_SPATIAL_FILTER_DELTA =        Delta value for Realsense Spatial Edge Preserving filter
string CAMERA_SPATIAL_FILTER_MAGNITUDE =    Magnitude value for Realsense Spatial Edge Preserving filter
string CAMERA_SPATIAL_FILTER_HOLE_FILLING = Hole filling range value for Realsense Spatial Edge Preserving filter
string CAMERA_DECIMATION_FILTER_MAGNITUDE = Magnitude value for Realsense Decimation filter

string CAMERA_NEW_GROUND_TOLERANCE_VALUE =          Threshold for ground removal algorithm in camera
string CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE = Number of point clouds for ground removal algorithm in camera

string MVS_START_RECORDING = Start data recording
string MVS_STOP_RECORDING = Stop data recording
string MVS_PLAY_RECORDING = Play recorded data

string LIDAR_EUCLIDEAN_FILTER_TOLERANCE =      Euclidean Segmentation tolerance for lidar pointcloud
string LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES =    Minimum number of points for lidar Euclidean Segmentation
string LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES =    Maximum number of points for lidar Euclidean Segmentation
string LIDAR_OUTLIERS_REMOVAL_MEAN =           Mean for lidar statistical noise removal Filter
string LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION =  Standard Deviation for lidar statistical noise removal Filter

string LIDAR_NEW_GROUND_TOLERANCE_VALUE =          Threshold for ground removal algorithm in lidar
string LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE = Number of point clouds for ground removal algorithm in lidar

string MVS_NEW_NN_RECOGNITION_TH = Threshold for object recognition neural network

string SAVE_MVS_CONFIGURATION = Save MVS configuration parameters

string START_SENSOR_CALIBRATION = Start sensors calibration
string REJECT_SENSOR_CALIBRATION = Reject the sensors calibration

# PERCEPTION SYSTEM DEFAULT CONFIGURATION VALUES

float32 TOLERANCE_BOUNDING_CYLINDER = 1.2

float32 CAMERA_EUCLIDEAN_FILTER_TOLERANCE_DEFAULT = 0.2
float32 CAMERA_EUCLIDEAN_FILTER_TOLERANCE_MIN = 0.001
float32 CAMERA_EUCLIDEAN_FILTER_TOLERANCE_MAX = 1

float32 CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES_DEFAULT = 350
float32 CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES_MIN = 1
float32 CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES_MAX = 300000

float32 CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES_DEFAULT = 150000
float32 CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES_MIN = 1
float32 CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES_MAX = 300000

float32 CAMERA_OUTLIERS_REMOVAL_MEAN_DEFAULT = 50
float32 CAMERA_OUTLIERS_REMOVAL_MEAN_MIN = 0
float32 CAMERA_OUTLIERS_REMOVAL_MEAN_MAX = 100

float32 CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION_DEFAULT = 1
float32 CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION_MIN = 1
float32 CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION_MAX = 10

float32 CAMERA_SPATIAL_FILTER_ALPHA_DEFAULT = 0.6
float32 CAMERA_SPATIAL_FILTER_ALPHA_MIN = 0.25
float32 CAMERA_SPATIAL_FILTER_ALPHA_MAX = 1

float32 CAMERA_SPATIAL_FILTER_DELTA_DEFAULT = 25
float32 CAMERA_SPATIAL_FILTER_DELTA_MIN = 1
float32 CAMERA_SPATIAL_FILTER_DELTA_MAX = 50

float32 CAMERA_SPATIAL_FILTER_MAGNITUDE_DEFAULT = 4
float32 CAMERA_SPATIAL_FILTER_MAGNITUDE_MIN = 1
float32 CAMERA_SPATIAL_FILTER_MAGNITUDE_MAX = 5

float32 CAMERA_SPATIAL_FILTER_HOLE_FILLING_DEFAULT = 3
float32 CAMERA_SPATIAL_FILTER_HOLE_FILLING_MIN = 0
float32 CAMERA_SPATIAL_FILTER_HOLE_FILLING_MAX = 5

float32 CAMERA_DECIMATION_FILTER_MAGNITUDE_DEFAULT = 3
float32 CAMERA_DECIMATION_FILTER_MAGNITUDE_MIN = 2
float32 CAMERA_DECIMATION_FILTER_MAGNITUDE_MAX = 8

float32 CAMERA_NEW_GROUND_TOLERANCE_VALUE_DEFAULT = 0.2
float32 CAMERA_NEW_GROUND_TOLERANCE_VALUE_MIN = 0.001
float32 CAMERA_NEW_GROUND_TOLERANCE_VALUE_MAX = 1

float32 CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_DEFAULT = 20
float32 CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MIN = 10
float32 CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MAX = 100


float32 LIDAR_EUCLIDEAN_FILTER_TOLERANCE_DEFAULT = 0.4
float32 LIDAR_EUCLIDEAN_FILTER_TOLERANCE_MIN = 0.001
float32 LIDAR_EUCLIDEAN_FILTER_TOLERANCE_MAX = 1

float32 LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES_DEFAULT = 5
float32 LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES_MIN = 1
float32 LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES_MAX = 300000

float32 LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES_DEFAULT = 100000
float32 LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES_MIN = 1
float32 LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES_MAX = 300000

float32 LIDAR_OUTLIERS_REMOVAL_MEAN_DEFAULT = 50
float32 LIDAR_OUTLIERS_REMOVAL_MEAN_MIN = 0
float32 LIDAR_OUTLIERS_REMOVAL_MEAN_MAX = 100

float32 LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION_DEFAULT = 1
float32 LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION_MIN = 1
float32 LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION_MAX = 10

float32 LIDAR_NEW_GROUND_TOLERANCE_VALUE_DEFAULT = 0.2
float32 LIDAR_NEW_GROUND_TOLERANCE_VALUE_MIN = 0.001
float32 LIDAR_NEW_GROUND_TOLERANCE_VALUE_MAX = 1

float32 LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_DEFAULT = 20
float32 LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MIN = 10
float32 LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MAX = 100

float32 MVS_NEW_NN_RECOGNITION_TH_DEFAULT = 0.75
float32 MVS_NEW_NN_RECOGNITION_TH_MIN = 0.5
float32 MVS_NEW_NN_RECOGNITION_TH_MAX = 1.1
"""
  # Pseudo-constants
  STATE_OFF = 1000
  STATE_STOP = 1001
  STATE_INIT = 1002
  STATE_SETUP = 1003
  STATE_CALIBRATING = 1004
  STATE_TRACKING = 1005
  STATE_EMERGENCY = 1006
  STATUS_OFF = 2000
  STATUS_STARTING = 2001
  STATUS_HEALTHY = 2002
  STATUS_FAILED = 2003
  SYSTEM_DIGITALEYE = 3000
  SYSTEM_MACHINE_VISION = 3001
  SYSTEM_IOT_GATEWAY = 3002
  SYSTEM_DEMS = 3003
  SYSTEM_POSITION = 3004
  SYSTEM_C2 = 3005
  MICROSERVICE_SYSTEM_CONFIG = 4000
  MICROSERVICE_STATUS_MANAGER = 4001
  MICROSERVICE_MVC_ADAPTER = 4002
  MICROSERVICE_IOT_ADAPTER = 4003
  MICROSERVICE_BOOKINGS_MANAGER = 4004
  MICROSERVICE_LOGGER = 4005
  MICROSERVICE_SENSOR_FUSION = 4006
  MICROSERVICE_MGS_MONITORING = 4007
  MICROSERVICE_MGS_MANAGER = 4008
  MICROSERVICE_MVC_CAMERA_MANAGER = 4009
  MICROSERVICE_MVC_LIDAR_MANAGER = 4010
  MICROSERVICE_MVC_ZONE_MANAGER = 4011
  MICROSERVICE_POSITION_ADAPTER = 4012
  MICROSERVICE_C2_ADAPTER = 4013
  MICROSERVICE_ALLOCATIONS_MANAGER = 4014
  MICROSERVICE_UAV_MANAGER = 4015
  MICROSERVICE_UAV_CONFORMANCE = 4016
  MICROSERVICE_CALIBRATION_MANAGER = 4017
  SENSOR_CAMERA = 5000
  SENSOR_LIDAR = 5001
  SENSOR_LOCATOR = 5002
  SENSOR_RTK = 5003
  SENSOR_COMPASS = 5004
  SENSOR_RADAR = 5005
  FRAME_GLOBAL = 6000
  FRAME_DIGITALEYE = 6001
  POLE_P1 = 7000
  POLE_S1 = 7001
  POLE_S2 = 7002
  POLE_S3 = 7003
  POLE_L1 = 7004
  POSENG_POLE_MANAGER = 8000
  POSENG_STREAMER = 8001
  POSENG_SOLVER = 8002
  POSENG_SAMPLER = 8003
  POSENG_SURVEYOR = 8004
  POSENG_PORT = 13013
  GNSS_NO_FIX = 8100
  GNSS_TIME_FLOAT = 8101
  GNSS_TIME_FIX = 8102
  GNSS_DEAD_FLOAT = 8103
  GNSS_DEAD_FIX = 8104
  GNSS_GPS_DEAD_FLOAT = 8105
  GNSS_GPS_DEAD_FIX = 8106
  GNSS_2D_FLOAT = 8107
  GNSS_2D_FIX = 8108
  GNSS_3D_FLOAT = 8109
  GNSS_3D_FIX = 8110
  GNSS_RTK_FLOAT = 8111
  GNSS_RTK_FIX = 8112
  GNSS_NO_CORR = 8200
  GNSS_BASE_CORR = 8201
  GNSS_NTRIP_CORR = 8202
  UAV_UOBX1 = 8100
  UAV_UOBX2 = 8101
  NOTIFICATION_INFO = 9000
  NOTIFICATION_IMPORTANT = 9001
  NOTIFICATION_CRITICAL = 9002
  REALSENSE_DEPTH_PROJECTOR_TEMPERATURE = 'Depth Projector Temp.'
  REALSENSE_DEPTH_ASIC_TEMPERATURE = 'Depth ASIC Temp.'
  REALSENSE_DEPTH_FRAME_DROPS = 'Depth Frame Drops'
  CPU1_BOARD_USAGE = 'CPU1 Usage%'
  CPU2_BOARD_USAGE = 'CPU2 Usage%'
  CPU3_BOARD_USAGE = 'CPU3 Usage%'
  CPU4_BOARD_USAGE = 'CPU4 Usage%'
  CPU5_BOARD_USAGE = 'CPU5 Usage%'
  CPU6_BOARD_USAGE = 'CPU6 Usage%'
  GPU_BOARD_USAGE = 'GPU Usage%'
  JETSON_POWER_MODE = 'Jetson Power Mode'
  JETSON_RAM_USAGE = 'Jetson RAM Usage'
  JETSON_DISK_USAGE = 'Jetson Disk Usage'
  JETSON_FAN_SPEED = 'Jetson Fan Speed'
  JETSON_CPU_TEMPERATURE = 'Jetson CPU Temp.'
  JETSON_GPU_TEMPERATURE = 'Jetson GPU Temp.'
  JETSON_POWER_AVERAGE = 'Jetson Power Avg.'
  JETSON_UP_TIME = 'Jetson Up Time'
  POLE_POSITION_LAT = 'Pole Latitude'
  POLE_POSITION_LON = 'Pole Longitude'
  POLE_POSITION_ALT = 'Pole Altitude'
  POLE_POSITION_ALT_MSL = 'Pole Altitude (MSL)'
  POLE_POSITION_VDOP = 'VDOP'
  POLE_POSITION_HDOP = 'HDOP'
  POLE_ORIENTATION = 'Pole Orientation'
  POLE_NUM_SATS = 'No. of Satellites'
  POLE_FIX_TYPE = 'GNSS Fix Type'
  POLE_CORRECTIONS = 'RTK Corrections'
  POLE_MODE = 'Operation Mode'
  CMPS12_ADDRESS = 96
  COMPASS_MAGNETOMETER_X_VALUE = 'Magnetometer X'
  COMPASS_MAGNETOMETER_Y_VALUE = 'Magnetometer Y'
  COMPASS_MAGNETOMETER_Z_VALUE = 'Magnetometer Z'
  COMPASS_ROLL_VALUE = 'Roll'
  COMPASS_PITCH_VALUE = 'Pitch'
  COMPASS_CALIBRATION_STATUS = 'Inertial sensor calibration Status'
  UAV_STATE = 'UAV State'
  UAV_TOLZ = 'UAV TOLZ'
  UAV_NAME = 'UAV Name'
  IOT_ISSUE = 'Issue'
  QPE_CPU_LOAD = 'CPU Load'
  QPE_LOSS_RATE = 'QPE Loss Rate'
  QPE_NETWORK_LOSS_RATE = 'Network Loss Rate'
  LOC_CONNECTION = 'Connection Status'
  LOC_TEMP = 'Temperature'
  FASTLOOP_ID_START = 0
  OBJECTS_ID_START = 100
  PS_FASTLOOP_ID_START = 1000
  PS_OBJECTS_ID_START = 1100
  MVC_OBJECT_ID_NN_START = 1500
  MVC_OBJECT_ID_CAMERA_START = 1600
  MVC_OBJECT_ID_LIDAR_START = 1800
  IOT_OBJECTS_ID_START = 2000
  IOT_OBJECTS_ID_END = 3000
  UAV_OBJECTS_ID_START = 10000
  SENSOR_FUSION_VALID_THRESHOLD = 'Set the threshold for an object to become valid'
  SENSOR_FUSION_DELETE_THRESHOLD = 'Set the threshold for deleting an object'
  SENSOR_FUSION_DISTANCE_THRESHOLD = 'Set the threshold for object distance association'
  SENSOR_FUSION_DELETE_PERIOD = 'Set the period in secs for an object to be deleted'
  SENSOR_FUSION_FILTER_FREQ = 'Set the frequency in Hz of the filtering'
  SENSOR_FUSION_SYSTEM_TYPE = 'Set the type of the sensor fusion system'
  START_MVC_AS_MAIN = 'Start board as main Machine Vision Computer'
  START_MVC_AS_SECONDARY = 'Start board as secondary Machine Vision Computer'
  STOP_MVC = 'Stop Machine Vision Computer'
  CAMERA_EUCLIDEAN_FILTER_TOLERANCE = 'Euclidean Segmentation tolerance for camera pointcloud'
  CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES = 'Minimum number of points for camera Euclidean Segmentation'
  CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES = 'Maximum number of points for camera Euclidean Segmentation'
  CAMERA_OUTLIERS_REMOVAL_MEAN = 'Mean for camera statistical noise removal Filter'
  CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION = 'Standard Deviation for camera statistical noise removal Filter'
  CAMERA_SPATIAL_FILTER_ALPHA = 'Alpha value for Realsense Spatial Edge Preserving filter'
  CAMERA_SPATIAL_FILTER_DELTA = 'Delta value for Realsense Spatial Edge Preserving filter'
  CAMERA_SPATIAL_FILTER_MAGNITUDE = 'Magnitude value for Realsense Spatial Edge Preserving filter'
  CAMERA_SPATIAL_FILTER_HOLE_FILLING = 'Hole filling range value for Realsense Spatial Edge Preserving filter'
  CAMERA_DECIMATION_FILTER_MAGNITUDE = 'Magnitude value for Realsense Decimation filter'
  CAMERA_NEW_GROUND_TOLERANCE_VALUE = 'Threshold for ground removal algorithm in camera'
  CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE = 'Number of point clouds for ground removal algorithm in camera'
  MVS_START_RECORDING = 'Start data recording'
  MVS_STOP_RECORDING = 'Stop data recording'
  MVS_PLAY_RECORDING = 'Play recorded data'
  LIDAR_EUCLIDEAN_FILTER_TOLERANCE = 'Euclidean Segmentation tolerance for lidar pointcloud'
  LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES = 'Minimum number of points for lidar Euclidean Segmentation'
  LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES = 'Maximum number of points for lidar Euclidean Segmentation'
  LIDAR_OUTLIERS_REMOVAL_MEAN = 'Mean for lidar statistical noise removal Filter'
  LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION = 'Standard Deviation for lidar statistical noise removal Filter'
  LIDAR_NEW_GROUND_TOLERANCE_VALUE = 'Threshold for ground removal algorithm in lidar'
  LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE = 'Number of point clouds for ground removal algorithm in lidar'
  MVS_NEW_NN_RECOGNITION_TH = 'Threshold for object recognition neural network'
  SAVE_MVS_CONFIGURATION = 'Save MVS configuration parameters'
  START_SENSOR_CALIBRATION = 'Start sensors calibration'
  REJECT_SENSOR_CALIBRATION = 'Reject the sensors calibration'
  TOLERANCE_BOUNDING_CYLINDER = 1.2
  CAMERA_EUCLIDEAN_FILTER_TOLERANCE_DEFAULT = 0.2
  CAMERA_EUCLIDEAN_FILTER_TOLERANCE_MIN = 0.001
  CAMERA_EUCLIDEAN_FILTER_TOLERANCE_MAX = 1.0
  CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES_DEFAULT = 350.0
  CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES_MIN = 1.0
  CAMERA_EUCLIDEAN_FILTER_MIN_SAMPLES_MAX = 300000.0
  CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES_DEFAULT = 150000.0
  CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES_MIN = 1.0
  CAMERA_EUCLIDEAN_FILTER_MAX_SAMPLES_MAX = 300000.0
  CAMERA_OUTLIERS_REMOVAL_MEAN_DEFAULT = 50.0
  CAMERA_OUTLIERS_REMOVAL_MEAN_MIN = 0.0
  CAMERA_OUTLIERS_REMOVAL_MEAN_MAX = 100.0
  CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION_DEFAULT = 1.0
  CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION_MIN = 1.0
  CAMERA_OUTLIERS_REMOVAL_STD_DEVIATION_MAX = 10.0
  CAMERA_SPATIAL_FILTER_ALPHA_DEFAULT = 0.6
  CAMERA_SPATIAL_FILTER_ALPHA_MIN = 0.25
  CAMERA_SPATIAL_FILTER_ALPHA_MAX = 1.0
  CAMERA_SPATIAL_FILTER_DELTA_DEFAULT = 25.0
  CAMERA_SPATIAL_FILTER_DELTA_MIN = 1.0
  CAMERA_SPATIAL_FILTER_DELTA_MAX = 50.0
  CAMERA_SPATIAL_FILTER_MAGNITUDE_DEFAULT = 4.0
  CAMERA_SPATIAL_FILTER_MAGNITUDE_MIN = 1.0
  CAMERA_SPATIAL_FILTER_MAGNITUDE_MAX = 5.0
  CAMERA_SPATIAL_FILTER_HOLE_FILLING_DEFAULT = 3.0
  CAMERA_SPATIAL_FILTER_HOLE_FILLING_MIN = 0.0
  CAMERA_SPATIAL_FILTER_HOLE_FILLING_MAX = 5.0
  CAMERA_DECIMATION_FILTER_MAGNITUDE_DEFAULT = 3.0
  CAMERA_DECIMATION_FILTER_MAGNITUDE_MIN = 2.0
  CAMERA_DECIMATION_FILTER_MAGNITUDE_MAX = 8.0
  CAMERA_NEW_GROUND_TOLERANCE_VALUE_DEFAULT = 0.2
  CAMERA_NEW_GROUND_TOLERANCE_VALUE_MIN = 0.001
  CAMERA_NEW_GROUND_TOLERANCE_VALUE_MAX = 1.0
  CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_DEFAULT = 20.0
  CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MIN = 10.0
  CAMERA_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MAX = 100.0
  LIDAR_EUCLIDEAN_FILTER_TOLERANCE_DEFAULT = 0.4
  LIDAR_EUCLIDEAN_FILTER_TOLERANCE_MIN = 0.001
  LIDAR_EUCLIDEAN_FILTER_TOLERANCE_MAX = 1.0
  LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES_DEFAULT = 5.0
  LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES_MIN = 1.0
  LIDAR_EUCLIDEAN_FILTER_MIN_SAMPLES_MAX = 300000.0
  LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES_DEFAULT = 100000.0
  LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES_MIN = 1.0
  LIDAR_EUCLIDEAN_FILTER_MAX_SAMPLES_MAX = 300000.0
  LIDAR_OUTLIERS_REMOVAL_MEAN_DEFAULT = 50.0
  LIDAR_OUTLIERS_REMOVAL_MEAN_MIN = 0.0
  LIDAR_OUTLIERS_REMOVAL_MEAN_MAX = 100.0
  LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION_DEFAULT = 1.0
  LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION_MIN = 1.0
  LIDAR_OUTLIERS_REMOVAL_STD_DEVIATION_MAX = 10.0
  LIDAR_NEW_GROUND_TOLERANCE_VALUE_DEFAULT = 0.2
  LIDAR_NEW_GROUND_TOLERANCE_VALUE_MIN = 0.001
  LIDAR_NEW_GROUND_TOLERANCE_VALUE_MAX = 1.0
  LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_DEFAULT = 20.0
  LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MIN = 10.0
  LIDAR_NEW_NUMBER_CALIBRATION_CLOUDS_VALUE_MAX = 100.0
  MVS_NEW_NN_RECOGNITION_TH_DEFAULT = 0.75
  MVS_NEW_NN_RECOGNITION_TH_MIN = 0.5
  MVS_NEW_NN_RECOGNITION_TH_MAX = 1.1

  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Constants, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
