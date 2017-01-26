import math
from Particle import Particle
from OpenGL.GL import *
from OpenGL.GLU import *

class Triangle(object):
  def __init__(self, a = None, b = None, c = None, density = None, drag = None):
    self.a = Particle() if a is None else a
    self.b = Particle() if b is None else b
    self.c = Particle() if c is None else c
    self.density = 0 if density is None else density
    self.drag = 0 if drag is None else drag
  
  def applyDragForce(self):
    velocity = self.a.velocity + self.b.velocity + self.c.velocity
    velocity /= 3
    normal = self.setNormals()
    dragForce = normal * (math.sqrt(velocity.magnitudeSquared() / normal.magnitudeSquared()) * velocity.dot(normal)) / 2
    dragForce = dragForce * self.density * self.drag * -0.5
    self.a.applyForce(dragForce)
    self.b.applyForce(dragForce)
    self.c.applyForce(dragForce)

  def draw(self):
    glBegin(GL_TRIANGLES)
    self.a.draw()
    self.b.draw()
    self.c.draw()
    glEnd()

  def update(self, deltaTime):
    self.a.update(deltaTime)
    self.b.update(deltaTime)
    self.c.update(deltaTime)

  def setNormals(self):
    normal = (self.c.position - self.a.position).cross(self.b.position - self.a.position)
    self.a.normals.append(normal)
    self.b.normals.append(normal)
    self.c.normals.append(normal)
    return normal
