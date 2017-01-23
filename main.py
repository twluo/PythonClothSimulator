import pygame
import math
import Math
import Cloth
from Camera.Camera import Camera
from Constants import COLOR
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

def init():
  specular = [ 1.0, 1.0, 1.0, 1.0 ]
  shininess = [ 100.0 ]
  altSpecular = [ 0.0, 1.0, 0.0, 1.0 ]
  light_diffuse = [ 1.0, 0.0, 0.0, 1.0 ]
  light_position = [ 1.0, 0.0, 0.0, 0.0 ]
  altlight_position = [ -1.0, 0.0, 0.0, 0.0 ]
  glLoadIdentity()
  glLightfv(GL_LIGHT0, GL_POSITION, light_position)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
  glLightfv(GL_LIGHT1, GL_POSITION, altlight_position)
  glLightfv(GL_LIGHT1, GL_DIFFUSE, altSpecular)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
  glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
  glEnable(GL_COLOR_MATERIAL)
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)
  glEnable(GL_LIGHT1)

def main():
  """
  This is our main program.
  """
  pygame.init()
  done = False
  # Set the height and width of the screen
  size = [SCREEN_WIDTH, SCREEN_HEIGHT]
  screen = pygame.display.set_mode(size, DOUBLEBUF|OPENGL)
  init()
  cam = Camera(aspect = size[0] / size[1])
  cam.distance += 4
  pygame.display.set_caption("Cloth Simulator")
 
  # Loop until the user clicks the close button.
 
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()
  debug = False
  cloth = Cloth.Cloth()
  wind = Math.Vector(0,0,0)
  # -------- Main Program Loop -----------
  while not done:
    # Limit to 60 frames per second and get dt
    dt = clock.tick(60)
    # --- Event Processing
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          wind.x += 1
        if event.key == pygame.K_z:
          wind.x -= 1
        if event.key == pygame.K_s:
          wind.y += 1
        if event.key == pygame.K_x:
          wind.y -= 1
        if event.key == pygame.K_d:
          wind.z += 1
        if event.key == pygame.K_c:
          wind.z -= 1
        if event.key == pygame.K_SPACE:
          debug = not debug
        print "Wind =", wind


    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor(1,0,0)
    cam.draw()
    cloth.applyForce(wind)
    cloth.update(1/float(dt))
    cloth.draw(debug)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.time.wait(60)
  # Close everything down
  pygame.quit()
 
if __name__ == "__main__":
  main()