# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from digitaleye_msgs/ObjectList.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import digitaleye_msgs.msg
import genpy
import geometry_msgs.msg
import std_msgs.msg

class ObjectList(genpy.Message):
  _md5sum = "5a8565b24262d2dd29181021ab99d186"
  _type = "digitaleye_msgs/ObjectList"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# List of objects reported within the Monitered Space

# information on the time at which objects
# were reported (epoch time) and their reference frame
std_msgs/Header header

# list of reported object(s)
digitaleye_msgs/Object[] objects

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
MSG: digitaleye_msgs/Object
# Description of an object in the Monitored Space

# information on the time at which the object
# was reported (epoch time) and its reference frame
std_msgs/Header header

# id assigned to the reported object
uint64 object_id

# list of ID(s) of reported object(s) which
# constitute it (if fused)
uint64[] fused_ids

# coordinates of the object’s estimated position
# in the local reference frame (meters)
geometry_msgs/Point position

# 3D covariance of the object position, represents the quality
# of the position estimate, higher covariances mean
# a worse estimate. XX, XY, XZ, YX, YY, YZ, ZX, ZY, ZZ
float32[9] pos_covariance

# estimated accuracy radius of object's position (meters)
float32 accuracy

# estimated velocity of the object (m/s)
geometry_msgs/Vector3 velocity

# estimated acceleration of the object (m/s2)
geometry_msgs/Accel acceleration

# estimated size of the object (meters)
geometry_msgs/Point scale

# object’s category
# e.g. Personnel, Package, Passenger, UAV, etc.
string classification

# list of zone(s) in which the object is
ZoneObjectStatus[] zones

# object’s name
# e.g. Minion-01 Minion-02, etc.
string name

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Accel
# This expresses acceleration in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: digitaleye_msgs/ZoneObjectStatus
# Status of the object within the specified zone

# identifier of the zone the object is in
uint32 zone_id

# whether or not the object is allowed in the zone
bool allowed

# time the object was first detected in this zone
# (ros timestamp in epoch time)
time first_detected

# time the object was last detected in this zone
# (ros timestamp in epoch time)
time last_detected
"""
  __slots__ = ['header','objects']
  _slot_types = ['std_msgs/Header','digitaleye_msgs/Object[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,objects

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectList, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.objects is None:
        self.objects = []
    else:
      self.header = std_msgs.msg.Header()
      self.objects = []

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
      length = len(self.objects)
      buff.write(_struct_I.pack(length))
      for val1 in self.objects:
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
        _x = val1.object_id
        buff.write(_get_struct_Q().pack(_x))
        length = len(val1.fused_ids)
        buff.write(_struct_I.pack(length))
        pattern = '<%sQ'%length
        buff.write(struct.Struct(pattern).pack(*val1.fused_ids))
        _v3 = val1.position
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        buff.write(_get_struct_9f().pack(*val1.pos_covariance))
        _x = val1.accuracy
        buff.write(_get_struct_f().pack(_x))
        _v4 = val1.velocity
        _x = _v4
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v5 = val1.acceleration
        _v6 = _v5.linear
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v7 = _v5.angular
        _x = _v7
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.scale
        _x = _v8
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.classification
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.zones)
        buff.write(_struct_I.pack(length))
        for val2 in val1.zones:
          _x = val2
          buff.write(_get_struct_IB().pack(_x.zone_id, _x.allowed))
          _v9 = val2.first_detected
          _x = _v9
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _v10 = val2.last_detected
          _x = _v10
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = val1.name
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
      if self.objects is None:
        self.objects = None
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
      self.objects = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.Object()
        _v11 = val1.header
        start = end
        end += 4
        (_v11.seq,) = _get_struct_I().unpack(str[start:end])
        _v12 = _v11.stamp
        _x = _v12
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v11.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v11.frame_id = str[start:end]
        start = end
        end += 8
        (val1.object_id,) = _get_struct_Q().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sQ'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.fused_ids = s.unpack(str[start:end])
        _v13 = val1.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 36
        val1.pos_covariance = _get_struct_9f().unpack(str[start:end])
        start = end
        end += 4
        (val1.accuracy,) = _get_struct_f().unpack(str[start:end])
        _v14 = val1.velocity
        _x = _v14
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v15 = val1.acceleration
        _v16 = _v15.linear
        _x = _v16
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v17 = _v15.angular
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v18 = val1.scale
        _x = _v18
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.classification = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.classification = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.zones = []
        for i in range(0, length):
          val2 = digitaleye_msgs.msg.ZoneObjectStatus()
          _x = val2
          start = end
          end += 5
          (_x.zone_id, _x.allowed,) = _get_struct_IB().unpack(str[start:end])
          val2.allowed = bool(val2.allowed)
          _v19 = val2.first_detected
          _x = _v19
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          _v20 = val2.last_detected
          _x = _v20
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          val1.zones.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        self.objects.append(val1)
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
      length = len(self.objects)
      buff.write(_struct_I.pack(length))
      for val1 in self.objects:
        _v21 = val1.header
        _x = _v21.seq
        buff.write(_get_struct_I().pack(_x))
        _v22 = _v21.stamp
        _x = _v22
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v21.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.object_id
        buff.write(_get_struct_Q().pack(_x))
        length = len(val1.fused_ids)
        buff.write(_struct_I.pack(length))
        pattern = '<%sQ'%length
        buff.write(val1.fused_ids.tostring())
        _v23 = val1.position
        _x = _v23
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        buff.write(val1.pos_covariance.tostring())
        _x = val1.accuracy
        buff.write(_get_struct_f().pack(_x))
        _v24 = val1.velocity
        _x = _v24
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v25 = val1.acceleration
        _v26 = _v25.linear
        _x = _v26
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v27 = _v25.angular
        _x = _v27
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v28 = val1.scale
        _x = _v28
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.classification
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.zones)
        buff.write(_struct_I.pack(length))
        for val2 in val1.zones:
          _x = val2
          buff.write(_get_struct_IB().pack(_x.zone_id, _x.allowed))
          _v29 = val2.first_detected
          _x = _v29
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _v30 = val2.last_detected
          _x = _v30
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = val1.name
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
      if self.objects is None:
        self.objects = None
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
      self.objects = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.Object()
        _v31 = val1.header
        start = end
        end += 4
        (_v31.seq,) = _get_struct_I().unpack(str[start:end])
        _v32 = _v31.stamp
        _x = _v32
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v31.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v31.frame_id = str[start:end]
        start = end
        end += 8
        (val1.object_id,) = _get_struct_Q().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sQ'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.fused_ids = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=length)
        _v33 = val1.position
        _x = _v33
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 36
        val1.pos_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=9)
        start = end
        end += 4
        (val1.accuracy,) = _get_struct_f().unpack(str[start:end])
        _v34 = val1.velocity
        _x = _v34
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v35 = val1.acceleration
        _v36 = _v35.linear
        _x = _v36
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v37 = _v35.angular
        _x = _v37
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v38 = val1.scale
        _x = _v38
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.classification = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.classification = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.zones = []
        for i in range(0, length):
          val2 = digitaleye_msgs.msg.ZoneObjectStatus()
          _x = val2
          start = end
          end += 5
          (_x.zone_id, _x.allowed,) = _get_struct_IB().unpack(str[start:end])
          val2.allowed = bool(val2.allowed)
          _v39 = val2.first_detected
          _x = _v39
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          _v40 = val2.last_detected
          _x = _v40
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          val1.zones.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        self.objects.append(val1)
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
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_9f = None
def _get_struct_9f():
    global _struct_9f
    if _struct_9f is None:
        _struct_9f = struct.Struct("<9f")
    return _struct_9f
_struct_IB = None
def _get_struct_IB():
    global _struct_IB
    if _struct_IB is None:
        _struct_IB = struct.Struct("<IB")
    return _struct_IB
_struct_Q = None
def _get_struct_Q():
    global _struct_Q
    if _struct_Q is None:
        _struct_Q = struct.Struct("<Q")
    return _struct_Q
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
