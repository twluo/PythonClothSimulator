import math

class Vector(object):

  def __init__(self,x = None,y = None,z = None, w = None):
    self.x = 0 if x is None else x
    self.y = 0 if y is None else y
    self.z = 0 if z is None else z
    self.w = 1 if w is None else w

  def __add__(self, other):
    if type(other) == type(self):
      return Vector(x = self.x + other.x, y = self.y + other.y, z = self.z + other.z)

  def __sub__(self, other):
    if type(other) == type(self):
      return self + (-other)

  def __mul__(self, other):
    if type(other) == type(1.0) or type(other) == type(1):
      return Vector(x = self.x * other, y = self.y * other, z = self.z * other)

  def __div__(self, other):
    if type(other) == type(1.0) or type(other) == type(1):
      return self * (1/other)
  def __neg__(self):
    return self * -1

  def __str__(self):
    return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w) + ">"

  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z

  def magnitudeSquared(self):
    return self.dot(self)

  def magnitude(self):
    return math.sqrt(self.magnitudeSquared())

  def reflect(self, other):
    return (other * (2 * self.dot(other))) - self

  def normalize(self):
    return self / self.magnitude()
