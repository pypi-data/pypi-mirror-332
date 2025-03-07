# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from digitaleye_msgs/Allocation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import digitaleye_msgs.msg

class Allocation(genpy.Message):
  _md5sum = "5acc02933cf4d919065bb9ac18a8c10d"
  _type = "digitaleye_msgs/Allocation"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Allocation in 4D

# allocation id
uint32 id

# action id, of which the allocation is part of
uint32 action_id

# allocation for the following entity id(s)
uint64[] entity_id

# allocation for the following entity class(es) (can be empty), use ENT_CLASS
uint32[] entity_class

# 3D Volume of allocation
digitaleye_msgs/Volume[] volume

# volume block ids
uint32[] block_ids

# start time of allocation (included) (Epoch timestamp in seconds)
uint64 start

# end time of allocation (included) (Epoch timestamp in seconds)
uint64 end

# duration allocation (included) (seconds)
uint64 duration

# category of allocation, use BLOCK_CAT_ in Constants Allocations
uint32 category

# command on allocation entry
digitaleye_msgs/VehicleCommand[] commands

# action dependencies
uint32[] action_dep

================================================================================
MSG: digitaleye_msgs/Volume
# Volume definition

# Volume shape, use SHAPE_
uint32 shape

uint32 SHAPE_PRISM=1
uint32 SHAPE_SPHERE=2
uint32 SHAPE_CYLINDER=3

# Parameters of the volume
uint32[] int_param
float64[] float_param

# Prism: characterised by 2 bases of same nb of point (x,y,z), ordered the same way
# size of float param is nb points*PRISM_FLOAT_PARAM_SIZE*2
# (number of points * number of coordinates/float param per point  * 2 bases)
# Prism int parameters indexes
uint32 PRISM_INT_NB_POINTS=0
uint32 PRISM_INT_PARAM_SIZE=1 # constant (not index) - size of int_param
# Prism float parameters indexes
uint32 PRISM_FLOAT_X=0
uint32 PRISM_FLOAT_Y=1
uint32 PRISM_FLOAT_Z=2
uint32 PRISM_FLOAT_PARAM_SIZE=3  # constant (not index) - size of each point / nb of float params per point

# Sphere: characterised by radius and centre point (x,y,z)
# Sphere no int parameters
uint32 SPHERE_INT_PARAM_SIZE=0 # constant (not index) - size of int_param
# Sphere float parameters indexes
uint32 SPHERE_FLOAT_RADIUS=0
uint32 SPHERE_FLOAT_X=1
uint32 SPHERE_FLOAT_Y=2
uint32 SPHERE_FLOAT_Z=3
uint32 SPHERE_FLOAT_PARAM_SIZE=4 # constant (not index) - size of float_param

# Cylinder: characterised by 2 bases with each:
#   centre point (x,y,z), radius, termination: spherical/flat (use TERM_)
# Cylinder int parameters indexes
uint32 CYLINDER_INT_TERM1=0
uint32 CYLINDER_INT_TERM2=1
uint32 CYLINDER_INT_PARAM_SIZE=2 # constant (not index) - size of int_param

# Cylinder float parameters indexes
uint32 CYLINDER_FLOAT_X1=0
uint32 CYLINDER_FLOAT_Y1=1
uint32 CYLINDER_FLOAT_Z1=2
uint32 CYLINDER_FLOAT_RADIUS1=3
uint32 CYLINDER_FLOAT_X2=4
uint32 CYLINDER_FLOAT_Y2=5
uint32 CYLINDER_FLOAT_Z2=6
uint32 CYLINDER_FLOAT_RADIUS2=7
uint32 CYLINDER_FLOAT_PARAM_SIZE=8 # constant (not index) - size of float_param

# termination of volume, spherical or flat
uint32 TERM_SPHERE=0
uint32 TERM_FLAT=1

================================================================================
MSG: digitaleye_msgs/VehicleCommand
# definition of vehicle commands

# The command, CMD_, see below
uint32 command

# Command
uint32 CMD_GOTO=0
uint32 CMD_TAKEOFF=1
uint32 CMD_LAND=2
uint32 CMD_STOP=3
uint32 CMD_CHANGE_YAW=4
uint32 CMD_CHANGE_SPEED=5
uint32 CMD_JUMP_CMD=6

# Parameters of the command
uint32 delay # delay of the command in second, mostly useful for missions
uint32[] int_param
float64[] float_param

## GOTO: Frame, use FRAME_; yaw angle in degrees, see specified frame;
## x, y, z see specified frame; ground speed m/s
# GOTO int parameters indexes
uint32 GOTO_INT_FRAME=0
uint32 GOTO_INT_YAW=1
uint32 GOTO_INT_PARAM_SIZE=2 # constant (not index) - size of int_param
# GOTO float parameters indexes
uint32 GOTO_FLOAT_X=0
uint32 GOTO_FLOAT_Y=1
uint32 GOTO_FLOAT_Z=2
uint32 GOTO_FLOAT_SPEED=3
uint32 GOTO_FLOAT_PARAM_SIZE=4 # constant (not index) - size of float_param

## TAKEOFF: Frame, use FRAME_; yaw angle in degrees, see specified frame;
## z see specified frame; vertical speed m/s
# TAKEOFF int parameters indexes
uint32 TAKEOFF_INT_FRAME=0
uint32 TAKEOFF_INT_YAW=1
uint32 TAKEOFF_INT_PARAM_SIZE=2 # constant (not index) - size of int_param
# TAKEOFF float parameters indexes
uint32 TAKEOFF_FLOAT_Z=0
uint32 TAKEOFF_FLOAT_SPEED=1
uint32 TAKEOFF_FLOAT_PARAM_SIZE=2 # constant (not index) - size of float_param

## LAND: no parameters
uint32 LAND_INT_PARAM_SIZE=0 # constant (not index) - size of int_param
uint32 LAND_FLOAT_PARAM_SIZE=0 # constant (not index) - size of float_param

## STOP: no parameters
uint32 STOP_INT_PARAM_SIZE=0 # constant (not index) - size of int_param
uint32 STOP_FLOAT_PARAM_SIZE=0 # constant (not index) - size of float_param

## CHANGE_YAW: Frame, use YAW_FRAME_; yaw angle in degrees, see specified frame; speed deg/s
# CHANGE_YAW int parameters indexes
uint32 CHANGE_YAW_INT_FRAME=0
uint32 CHANGE_YAW_INT_YAW=1
uint32 CHANGE_YAW_INT_SPEED=2
uint32 CHANGE_YAW_INT_PARAM_SIZE=3 # constant (not index) - size of int_param
# CHANGE_YAW no float parameters
uint32 CHANGE_YAW_FLOAT_PARAM_SIZE=0 # constant (not index) - size of float_param

## CHANGE_SPEED: ground speed in m/s
uint32 CHANGE_SPEED_INT_PARAM_SIZE=0 # constant (not index) - size of int_param
# CHANGE_SPEED float parameters indexes
uint32 CHANGE_SPEED_FLOAT_Z=0
uint32 CHANGE_SPEED_FLOAT_PARAM_SIZE=1 # constant (not index) - size of float_param

## JUMP_CMD: Command number to jump to; repeat giving the number of repeats
# JUMP_CMD int parameters indexes
uint32 JUMP_CMD_INT_CMD_NB=0
uint32 JUMP_CMD_INT_REPEAT=1
uint32 JUMP_CMD_INT_PARAM_SIZE=2 # constant (not index) - size of int_param
# JUMP_CMD no float parameters
uint32 JUMP_CMD_FLOAT_PARAM_SIZE=0 # constant (not index) - size of float_param

## FRAME:
uint32 FRAME_PORTAL = 0 # Portal coordinate frame, coordinates in m, absolute yaw (-1 to not specify)
uint32 FRAME_GLOBAL = 1 # WGS84 coordinate frame (deg) + MSL altitude (m), absolute yaw (-1 to not specify)
uint32 FRAME_FRD = 2 # FRD local frame, x: Forward, y: Right, z: Down (m), relative yaw

"""
  __slots__ = ['id','action_id','entity_id','entity_class','volume','block_ids','start','end','duration','category','commands','action_dep']
  _slot_types = ['uint32','uint32','uint64[]','uint32[]','digitaleye_msgs/Volume[]','uint32[]','uint64','uint64','uint64','uint32','digitaleye_msgs/VehicleCommand[]','uint32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,action_id,entity_id,entity_class,volume,block_ids,start,end,duration,category,commands,action_dep

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Allocation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.action_id is None:
        self.action_id = 0
      if self.entity_id is None:
        self.entity_id = []
      if self.entity_class is None:
        self.entity_class = []
      if self.volume is None:
        self.volume = []
      if self.block_ids is None:
        self.block_ids = []
      if self.start is None:
        self.start = 0
      if self.end is None:
        self.end = 0
      if self.duration is None:
        self.duration = 0
      if self.category is None:
        self.category = 0
      if self.commands is None:
        self.commands = []
      if self.action_dep is None:
        self.action_dep = []
    else:
      self.id = 0
      self.action_id = 0
      self.entity_id = []
      self.entity_class = []
      self.volume = []
      self.block_ids = []
      self.start = 0
      self.end = 0
      self.duration = 0
      self.category = 0
      self.commands = []
      self.action_dep = []

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
      buff.write(_get_struct_2I().pack(_x.id, _x.action_id))
      length = len(self.entity_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%sQ'%length
      buff.write(struct.Struct(pattern).pack(*self.entity_id))
      length = len(self.entity_class)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.entity_class))
      length = len(self.volume)
      buff.write(_struct_I.pack(length))
      for val1 in self.volume:
        _x = val1.shape
        buff.write(_get_struct_I().pack(_x))
        length = len(val1.int_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(struct.Struct(pattern).pack(*val1.int_param))
        length = len(val1.float_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.float_param))
      length = len(self.block_ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.block_ids))
      _x = self
      buff.write(_get_struct_3QI().pack(_x.start, _x.end, _x.duration, _x.category))
      length = len(self.commands)
      buff.write(_struct_I.pack(length))
      for val1 in self.commands:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.command, _x.delay))
        length = len(val1.int_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(struct.Struct(pattern).pack(*val1.int_param))
        length = len(val1.float_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.float_param))
      length = len(self.action_dep)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.action_dep))
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
      if self.volume is None:
        self.volume = None
      if self.commands is None:
        self.commands = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.id, _x.action_id,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sQ'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.entity_id = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.entity_class = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.volume = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.Volume()
        start = end
        end += 4
        (val1.shape,) = _get_struct_I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.int_param = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.float_param = s.unpack(str[start:end])
        self.volume.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.block_ids = s.unpack(str[start:end])
      _x = self
      start = end
      end += 28
      (_x.start, _x.end, _x.duration, _x.category,) = _get_struct_3QI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.commands = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.VehicleCommand()
        _x = val1
        start = end
        end += 8
        (_x.command, _x.delay,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.int_param = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.float_param = s.unpack(str[start:end])
        self.commands.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.action_dep = s.unpack(str[start:end])
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
      buff.write(_get_struct_2I().pack(_x.id, _x.action_id))
      length = len(self.entity_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%sQ'%length
      buff.write(self.entity_id.tostring())
      length = len(self.entity_class)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.entity_class.tostring())
      length = len(self.volume)
      buff.write(_struct_I.pack(length))
      for val1 in self.volume:
        _x = val1.shape
        buff.write(_get_struct_I().pack(_x))
        length = len(val1.int_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(val1.int_param.tostring())
        length = len(val1.float_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.float_param.tostring())
      length = len(self.block_ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.block_ids.tostring())
      _x = self
      buff.write(_get_struct_3QI().pack(_x.start, _x.end, _x.duration, _x.category))
      length = len(self.commands)
      buff.write(_struct_I.pack(length))
      for val1 in self.commands:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.command, _x.delay))
        length = len(val1.int_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(val1.int_param.tostring())
        length = len(val1.float_param)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.float_param.tostring())
      length = len(self.action_dep)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.action_dep.tostring())
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
      if self.volume is None:
        self.volume = None
      if self.commands is None:
        self.commands = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.id, _x.action_id,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sQ'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.entity_id = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.entity_class = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.volume = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.Volume()
        start = end
        end += 4
        (val1.shape,) = _get_struct_I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.int_param = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.float_param = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.volume.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.block_ids = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      _x = self
      start = end
      end += 28
      (_x.start, _x.end, _x.duration, _x.category,) = _get_struct_3QI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.commands = []
      for i in range(0, length):
        val1 = digitaleye_msgs.msg.VehicleCommand()
        _x = val1
        start = end
        end += 8
        (_x.command, _x.delay,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.int_param = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.float_param = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.commands.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.action_dep = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
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
_struct_3QI = None
def _get_struct_3QI():
    global _struct_3QI
    if _struct_3QI is None:
        _struct_3QI = struct.Struct("<3QI")
    return _struct_3QI
