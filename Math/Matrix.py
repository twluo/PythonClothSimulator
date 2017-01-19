from Vector import Vector

class Matrix(object):
  def __init__(self, a = None, b = None, c = None, d = None):
    self.a = Vector(1,0,0,0) if a is None else a
    self.b = Vector(0,1,0,0) if b is None else b
    self.c = Vector(0,0,1,0) if c is None else c
    self.d = Vector(0,0,0,1) if d is None else d

  def __str__(self):
    a = "\n<" + str(self.a.x) + "," + str(self.b.x) + "," + str(self.c.x) + "," + str(self.d.x) + ">"
    b = "\n<" + str(self.a.y) + "," + str(self.b.y) + "," + str(self.c.y) + "," + str(self.d.y) + ">"
    c = "\n<" + str(self.a.z) + "," + str(self.b.z) + "," + str(self.c.z) + "," + str(self.d.z) + ">"
    d = "\n<" + str(self.a.w) + "," + str(self.b.w) + "," + str(self.c.w) + "," + str(self.d.w) + ">"
    return a + b + c + d