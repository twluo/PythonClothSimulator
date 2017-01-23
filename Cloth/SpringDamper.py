import Particle
import Math
from OpenGL.GL import *
from OpenGL.GLU import *

class SpringDamper(object):
  def __init__(self, a = None, b = None, springFactor = None, dampingFactor = None):
    self.a = Particle() if a is None else a
    self.b = Particle() if b is None else b
    self.springFactor = 0 if springFactor is None else springFactor
    self.dampingFactor = 0 if dampingFactor is None else dampingFactor
    self.restLength = (b.position - a.position).magnitude()

  def applySpringDamperForce(self):
    direction = self.b.position - self.a.position
    length = direction.magnitude()
    direction /= length
    deltaSpeed = self.a.velocity.dot(direction) - self.b.velocity.dot(direction)
    deltaLength = self.restLength - length
    springDamperForce = -(self.springFactor * deltaLength + self.dampingFactor * deltaSpeed)
    springDamperForce = direction * springDamperForce
    self.a.applyForce(springDamperForce)
    self.b.applyForce(-springDamperForce)

  def draw(self):
    glBegin(GL_LINES);
    glColor3d(0, 1, 1);
    glVertex3f(self.a.position.x, self.a.position.y, self.a.position.z);
    glVertex3f(self.b.position.x, self.b.position.y, self.b.position.z);
    glEnd();