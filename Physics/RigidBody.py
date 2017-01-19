from Math import Vector 
from Constants import COLOR
import pygame

BALL_SIZE = 10
class RigidBody(object):
  """
  Class to keep track of a ball's location and vector.
  """
  def __init__(self, position = None, force = None, velocity = None, mass = None, size = None, static = None):
    self.position = Vector() if position is None else position
    self.force = Vector() if force is None else force
    self.velocity = Vector() if velocity is None else velocity
    self.mass = 1 if mass is None else mass
    self.size = BALL_SIZE if size is None else size
    self.static = False if static is None else static
      
  def getPixelCoordinates(self, Vector):
    return (int(Vector.x), int(Vector.y))

  def applyForce(self, force):
    self.force = self.force + force

  def draw(self, screen):
    pygame.draw.circle(screen, COLOR.WHITE, self.getPixelCoordinates(self.position), self.size)

  def drawDebug(self, screen):
    position = self.getPixelCoordinates(self.position)
    forceEnd = map(sum, zip(position, self.getPixelCoordinates(self.force)))
    velocityEnd = map(sum, zip(position, self.getPixelCoordinates(self.velocity)))
    pygame.draw.line(screen, COLOR.RED, position, forceEnd)
    pygame.draw.line(screen, COLOR.GREEN, position, velocityEnd)

  def update(self, deltaTime):
    if self.static:
      return
    accel = self.force /self.mass
    self.velocity += accel * deltaTime
    self.position += self.velocity * deltaTime
    self.force = Vector()