from OpenGL.GL import *
from OpenGL.GLU import *

class Camera(object):
  def __init__(self, FOV = None, aspect = None, nearClip = None, farClip = None, distance = None, azimuth = None, incline = None):
    self.FOV = 60 if FOV is None else FOV
    self.aspect = 1.33 if aspect is None else aspect
    self.nearClip = 0.1 if nearClip is None else nearClip
    self.farClip = 100.0 if farClip is None else farClip
    self.distance = 5.0 if distance is None else distance
    self.azimuth = 0.0 if azimuth is None else azimuth
    self.incline = 0.0 if incline is None else incline

  def reset(self):
    self.FOV = 60
    self.aspect = 1.33
    self.nearClip = 0.1
    self.farClip = 100.0
    self.distance = 5.0
    self.azimuth = 0.0
    self.incline = 0.0

  def draw(self):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(self.FOV, self.aspect, self.nearClip, self.farClip)

    glTranslatef(0,0, -self.distance)
    glRotatef(self.incline, 1.0, 0.0, 0.0)
    glRotatef(self.azimuth, 0.0, 1.0, 0.0)

    glMatrixMode(GL_MODELVIEW)