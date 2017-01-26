from Math import Vector 
from Constants import COLOR
from OpenGL.GL import *
from OpenGL.GLU import *

BALL_SIZE = 10
class Particle(object):
  """
  Class to keep track of a ball's location and vector.
  """
  def __init__(self, position = None, normal = None, force = None, velocity = None, mass = None, static = None):
    self.position = Vector() if position is None else position
    self.normals = [] if normal is None else normal
    self.force = Vector() if force is None else force
    self.velocity = Vector() if velocity is None else velocity
    self.mass = 1 if mass is None else mass
    self.static = False if static is None else static

  def __repr__(self):
    return str(self.position)
      
  def getPixelCoordinates(self, Vector):
    return (int(Vector.x), int(Vector.y))

  def applyForce(self, force):
    self.force = self.force + force

  def getNormal(self):
    if len(self.normals) is 0:
      return None
    normal = Vector()
    for n in self.normals:
      normal += n
    normal /= len(self.normals)
    normal = normal.normalize()
    return normal

  def draw(self):
    normal = self.getNormal()
    glNormal(normal.x, normal.y, -normal.z)
    glVertex3f(self.position.x, self.position.y, self.position.z)

  def update(self, deltaTime):
    if self.static:
      return
    accel = self.force /self.mass
    self.velocity += accel * deltaTime
    self.position += self.velocity * deltaTime
    self.force = Vector()