# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from digitaleye_msgs/UavIntReportList.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import digitaleye_msgs.msg
import std_msgs.msg

class UavIntReportList(genpy.Message):
  _md5sum = "dadae2bf68366e87c40ec6f0e1750ad7"
  _type = "digitaleye_msgs/UavIntReportList"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# List of internal generic UAV report(s)

# information on the time at which report was sent
# (epoch time)
std_msgs/Header header

# list of UAVs' description
digitaleye_msgs/UavIntReport[] uavs

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: digitaleye_msgs/UavIntReport
# Generic internal UAV report

# information on the time at which the object
# was reported (epoch time) and its reference frame
std_msgs/Header header

# list of internal metric(s), using UAV_INT_ constants
digitaleye_msgs/Metric[] uav_metric

# Constants for Metric of uav_metric

# internal id, uint
string UAV_INT_ID = Internal ID

# internal status, use STATUS_ constants below
string UAV_INT_STATUS = Internal status

string STATUS_BOOKED            = Booked
string STATUS_BOOKED_ACTIVE     = Active Booking
string STATUS_HANDOVER_AIR_IN   = Taking Over (Air)
string STATUS_HANDOVER_GROUND_IN= Taking Over (Ground)
string STATUS_TAKE_OFF_PREP     = Preparing for Take-Off
string STATUS_TAKING_OFF        = Taking Off
string STATUS_LANDING           = Landing
string STATUS_FLYING_IN         = Flying In
string STATUS_FLYING_OUT        = Flying Out
string STATUS_HELD_FLY_IN       = Held while flying in
string STATUS_HELD_FLY_OUT      = Held while flying out
string STATUS_HELD_TAKE_OFF     = Held while taking off
string STATUS_HELD_LANDING      = Held while landing
string STATUS_LANDED            = Landed
string STATUS_HANDOVER_AIR_OUT  = Handing Over (Air)
string STATUS_EXITING           = Exiting
string STATUS_UNKNOWN           = Unknown

# conformance status, use CONF_ constants
string UAV_INT_CONF_STATUS = Conformance status

string CONF_UNKNOWN         = Unknown
string CONF_KO_UNKNOWN_UAV  = Unsafe Unknown UAV
string CONF_OK_GROUND       = Safe Grounded Unknown UAV
string CONF_OK_AIR          = Safe Unknown UAV
string CONF_WAITING_ENTRY   = Waiting Entry
string CONF_KO_AIR_ENTRY    = Invalid Air Entry
string CONF_OK_AIR_ENTRY    = Valid Air Entry
string CONF_OK_AIR_EXIT    = Valid Air Exit
string CONF_KO_GROUND_ENTRY = Invalid Ground Entry
string CONF_OK_GROUND_ENTRY = Valid Ground Entry
string CONF_KO_ALL_ENTRIES  = Invalid Entries
string CONF_KO_FLIGHT_PATH  = Out of Flight Corridor
string CONF_OK_FLIGHT_PATH  = In Flight Corridor
string CONF_READY_LAND      = Ready to Land
string CONF_READY_FLY_OUT   = Ready to Fly Out

# local position lat:long:alt (in meters)
string UAV_INT_LOC_POS = Local position

# agent registration (string)
string UAV_INT_CALLSIGN = Agent registration

# absolute position lat:long:alt
# (lat, long in degrees and alt in meters - WGS84 ellipsoid)
string UAV_INT_ABS_POS = Absolute position

# ground speed x:y:z (m/s)
string UAV_INT_GND_SPEED = Ground speed

# GNSS fix-type code use FIX_ constants below
string UAV_INT_FIX_TYPE = Fix-type

string FIX_NO_GNSS      = No GNSS
string FIX_NO_FIX       = No Position
string FIX_2D           = 2D Position
string FIX_3D           = 3D Position
string FIX_DGPS         = DGPS
string FIX_RTK_FLOAT    = RTK Float
string FIX_RTK_FIXED    = RTK Fixed
string FIX_STATIC       = Static Fixed
string FIX_PPP          = PPP
string FIX_UNKNOWN      = Unknown

# HDOP horizontal dilution of position (float unitless)
string UAV_INT_HDOP = HDOP

# VDOP horizontal dilution of position (float unitless)
string UAV_INT_VDOP = VDOP

# number of visible satellites by the UAV
string UAV_INT_NB_SATS_VIS = Nb sat vis

# percentage of battery remaining (uint)
string UAV_INT_BATT_REMAIN = Battery remaining

# reported state, use STATE_ constants below
string UAV_INT_C2_STATE = C2 state

string C2_STATE_NOT_READY     = Not Ready
string C2_STATE_READY_TO      = Ready for T-O
string C2_STATE_TAKING_OFF    = Taking Off
string C2_STATE_FLYING        = Flying
string C2_STATE_HELD          = Held
string C2_STATE_LANDING       = Landing
string C2_STATE_UNKNOWN       = Unknown

================================================================================
MSG: digitaleye_msgs/Metric
# Performance indicator for a subsystem,
# component or sensor

# name of the performance indicator
string name

# value of the performance indicator
string value
"""
  __slots__ = ['header','uavs']
  _slot_types = ['std_msgs/Header','digitaleye_msgs/UavIntReport[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,uavs

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(UavIntReportList, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.uavs is None:
        self.uavs = []
    else:
      self.header = std_msgs.msg.Header()
      self.uavs = []

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.uavs)
      buff.write(_struct_I.pack(length))
      for val1 in self.uavs:
        _v1 = val1.header
        _x = _v1.seq
        buff.write(_get_struct_I().pack(_x))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.uav_metric)
        buff.write(_struct_I.pack(length))
        for val2 in val1.uav_metric:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.uavs is None:
        self.uavs = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.uavs = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.UavIntReport()
        _v3 = val1.header
        start = end
        end += 4
        (_v3.seq,) = _get_struct_I().unpack(str[start:end])
        _v4 = _v3.stamp
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v3.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.uav_metric = []
        for i in range(0, length):
          val2 = digitaleye_msgs.msg.Metric()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.value = str[start:end]
          val1.uav_metric.append(val2)
        self.uavs.append(val1)
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.uavs)
      buff.write(_struct_I.pack(length))
      for val1 in self.uavs:
        _v5 = val1.header
        _x = _v5.seq
        buff.write(_get_struct_I().pack(_x))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.uav_metric)
        buff.write(_struct_I.pack(length))
        for val2 in val1.uav_metric:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.uavs is None:
        self.uavs = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.uavs = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.UavIntReport()
        _v7 = val1.header
        start = end
        end += 4
        (_v7.seq,) = _get_struct_I().unpack(str[start:end])
        _v8 = _v7.stamp
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v7.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.uav_metric = []
        for i in range(0, length):
          val2 = digitaleye_msgs.msg.Metric()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.value = str[start:end]
          val1.uav_metric.append(val2)
        self.uavs.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
