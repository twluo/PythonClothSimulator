import Math
from Particle import Particle
from Triangle import Triangle
from SpringDamper import SpringDamper

class Cloth(object):
  def __init__(self, position = None, width = None, height = None, numOfParticlesX = None, numOfParticlesY = None, density = None, drag = None, springFactor = None, dampingFactor = None):
    self.position = Math.Vector() if position is None else position
    self.width = 8.0 if width is None else float(width)
    self.height = 8.0 if height is None else float(height)
    self.numOfParticlesX = 5 if numOfParticlesX is None else numOfParticlesX
    self.numOfParticlesY = 5 if numOfParticlesY is None else numOfParticlesY
    self.density = 1.2 if density is None else density
    self.drag = 0.4 if drag is None else drag
    self.springFactor = 1000 if springFactor is None else springFactor
    self.dampingFactor = 1 if dampingFactor is None else dampingFactor
    self.force = Math.Vector()
    self.particles = []
    self.triangles = []
    self.springDampers = []
    self.setParticles()
    self.setTriangles()
    self.setSpringDampers()

  def setParticles(self):
    rowOffset = self.width / (self.numOfParticlesX - 1)
    colOffset = self.height / (self.numOfParticlesY - 1)
    position = self.position - Math.Vector(self.width/2, -self.height/2, 0)
    for y in xrange(self.numOfParticlesY):
      particles = []
      for x in xrange(self.numOfParticlesX):
        if y is 0 and x is 0:
          particles.append(Particle(position = Math.Vector(position.x + rowOffset * x, position.y - colOffset * y, position.z), static = True))
        else:
          particles.append(Particle(position = Math.Vector(position.x + rowOffset * x, position.y - colOffset * y, position.z), static = False))
      self.particles.append(particles)

  def setTriangles(self):
    for i in xrange(self.numOfParticlesY):
      for j in xrange(self.numOfParticlesX - 1):
        if i is 0:
          self.triangles.append(Triangle(self.particles[i][j], self.particles[i][j+1], self.particles[i+1][j], self.density, self.drag))
        elif i is self.numOfParticlesY - 1:
          self.triangles.append(Triangle(self.particles[i][j], self.particles[i-1][j+1], self.particles[i][j+1], self.density, self.drag))
        else:
          self.triangles.append(Triangle(self.particles[i][j], self.particles[i][j+1], self.particles[i+1][j], self.density, self.drag))
          self.triangles.append(Triangle(self.particles[i][j], self.particles[i-1][j+1], self.particles[i][j+1], self.density, self.drag))

  def setSpringDampers(self):
    for i in xrange(self.numOfParticlesY):
      for j in xrange(self.numOfParticlesX):
        if i == 0:
          if j is self.numOfParticlesX - 1:
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i+1][j], self.springFactor, self.dampingFactor))
          else:
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i][j+1], self.springFactor, self.dampingFactor))
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i+1][j+1], self.springFactor, self.dampingFactor))
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i+1][j], self.springFactor, self.dampingFactor))
        elif i is self.numOfParticlesY - 1:
          if j is not self.numOfParticlesX- 1:
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i-1][j+1], self.springFactor, self.dampingFactor))
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i][j+1], self.springFactor, self.dampingFactor))
        else:
          if j is self.numOfParticlesX - 1:
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i+1][j], self.springFactor, self.dampingFactor))
          else:
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i-1][j+1], self.springFactor, self.dampingFactor))
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i][j+1], self.springFactor, self.dampingFactor))
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i+1][j+1], self.springFactor, self.dampingFactor))
            self.springDampers.append(SpringDamper(self.particles[i][j], self.particles[i+1][j], self.springFactor, self.dampingFactor))
    self.springDampers.append(SpringDamper(self.particles[0][0], self.particles[0][self.numOfParticlesX - 1], 100, self.dampingFactor))
    self.springDampers.append(SpringDamper(self.particles[0][0], self.particles[self.numOfParticlesY - 1][0], 100, self.dampingFactor))
    self.springDampers.append(SpringDamper(self.particles[0][0], self.particles[self.numOfParticlesY - 1][self.numOfParticlesX - 1], 100, self.dampingFactor))
    self.springDampers.append(SpringDamper(self.particles[self.numOfParticlesY - 1][0], self.particles[0][self.numOfParticlesX - 1], 100, self.dampingFactor))
    self.springDampers.append(SpringDamper(self.particles[self.numOfParticlesY - 1][0], self.particles[self.numOfParticlesY - 1][self.numOfParticlesX - 1], 100, self.dampingFactor))
    self.springDampers.append(SpringDamper(self.particles[self.numOfParticlesY - 1][self.numOfParticlesX - 1], self.particles[0][self.numOfParticlesX - 1], 100, self.dampingFactor))

  def draw(self, debug):
    if debug:
      for springDamper in self.springDampers:
        springDamper.draw()
    else:
      for triangle in self.triangles:
        triangle.draw()

  def applyForce(self, force):
    self.force += force

  def update(self, dt):
    for particles in self.particles:
      for particle in particles:
        particle.applyForce(Math.Vector(0,-9.8,0) * particle.mass)
        particle.applyForce(self.force)
    for springDamper in self.springDampers:
      springDamper.applySpringDamperForce()
    for triangle in self.triangles:
      triangle.applyDragForce()
    self.force = Math.Vector()
    for particles in self.particles:
      for particle in particles:
        particle.update(dt)
