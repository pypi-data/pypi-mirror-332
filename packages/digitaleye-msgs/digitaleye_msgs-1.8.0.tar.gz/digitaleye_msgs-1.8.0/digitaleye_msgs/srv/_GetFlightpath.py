# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from digitaleye_msgs/GetFlightpathRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetFlightpathRequest(genpy.Message):
  _md5sum = "43310bbaa3bc410f9c4a6b88224c5088"
  _type = "digitaleye_msgs/GetFlightpathRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Returns the latest local computed flighpath for a given UAV
# This query stops the generation of the flight path

# agent registration of the UAV
uint64 agent_reg

# type of fligh path to retrieve:
#  - true: UAV is flying in
#  - false: UAV is flying out
bool is_flying_in

"""
  __slots__ = ['agent_reg','is_flying_in']
  _slot_types = ['uint64','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       agent_reg,is_flying_in

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetFlightpathRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.agent_reg is None:
        self.agent_reg = 0
      if self.is_flying_in is None:
        self.is_flying_in = False
    else:
      self.agent_reg = 0
      self.is_flying_in = False

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
      buff.write(_get_struct_QB().pack(_x.agent_reg, _x.is_flying_in))
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
      _x = self
      start = end
      end += 9
      (_x.agent_reg, _x.is_flying_in,) = _get_struct_QB().unpack(str[start:end])
      self.is_flying_in = bool(self.is_flying_in)
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
      buff.write(_get_struct_QB().pack(_x.agent_reg, _x.is_flying_in))
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
      _x = self
      start = end
      end += 9
      (_x.agent_reg, _x.is_flying_in,) = _get_struct_QB().unpack(str[start:end])
      self.is_flying_in = bool(self.is_flying_in)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_QB = None
def _get_struct_QB():
    global _struct_QB
    if _struct_QB is None:
        _struct_QB = struct.Struct("<QB")
    return _struct_QB
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from digitaleye_msgs/GetFlightpathResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import digitaleye_msgs.msg
import geometry_msgs.msg

class GetFlightpathResponse(genpy.Message):
  _md5sum = "0deee877a58c3e27b14561d2a9cdbdc4"
  _type = "digitaleye_msgs/GetFlightpathResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
# flight path for this UAV
digitaleye_msgs/Flightpath flight_path


================================================================================
MSG: digitaleye_msgs/Flightpath
# Fligh path definition

# TOLZ id (0 = N/A)
uint32 tolz_id

# list of flight point(s)
digitaleye_msgs/Flightpoint[] flight_points

================================================================================
MSG: digitaleye_msgs/Flightpoint
# Flight point definition

# local coordinates of point (meters)
geometry_msgs/Point coord

# desired speed to reach this point (m/s)
float32 speed

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['flight_path']
  _slot_types = ['digitaleye_msgs/Flightpath']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       flight_path

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetFlightpathResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.flight_path is None:
        self.flight_path = digitaleye_msgs.msg.Flightpath()
    else:
      self.flight_path = digitaleye_msgs.msg.Flightpath()

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
      _x = self.flight_path.tolz_id
      buff.write(_get_struct_I().pack(_x))
      length = len(self.flight_path.flight_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.flight_path.flight_points:
        _v1 = val1.coord
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.speed
        buff.write(_get_struct_f().pack(_x))
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
      if self.flight_path is None:
        self.flight_path = digitaleye_msgs.msg.Flightpath()
      end = 0
      start = end
      end += 4
      (self.flight_path.tolz_id,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flight_path.flight_points = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.Flightpoint()
        _v2 = val1.coord
        _x = _v2
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (val1.speed,) = _get_struct_f().unpack(str[start:end])
        self.flight_path.flight_points.append(val1)
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
      _x = self.flight_path.tolz_id
      buff.write(_get_struct_I().pack(_x))
      length = len(self.flight_path.flight_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.flight_path.flight_points:
        _v3 = val1.coord
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.speed
        buff.write(_get_struct_f().pack(_x))
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
      if self.flight_path is None:
        self.flight_path = digitaleye_msgs.msg.Flightpath()
      end = 0
      start = end
      end += 4
      (self.flight_path.tolz_id,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flight_path.flight_points = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.Flightpoint()
        _v4 = val1.coord
        _x = _v4
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (val1.speed,) = _get_struct_f().unpack(str[start:end])
        self.flight_path.flight_points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
class GetFlightpath(object):
  _type          = 'digitaleye_msgs/GetFlightpath'
  _md5sum = 'aacb4cc4adb772ef9d9b6984105bc552'
  _request_class  = GetFlightpathRequest
  _response_class = GetFlightpathResponse
