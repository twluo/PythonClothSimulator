import pygame
import math
import Math
import Physics
from Constants import COLOR
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

def main():
  """
  This is our main program.
  """
  pygame.init()
 
  # Set the height and width of the screen
  size = [SCREEN_WIDTH, SCREEN_HEIGHT]
  screen = pygame.display.set_mode(size)
 
  pygame.display.set_caption("Bouncing Balls")
 
  # Loop until the user clicks the close button.
  done = False
 
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()
  debug = False
  ball_list = []
 
  ball = Physics.RigidBody(position = Math.Vector(x = 350, y = 0), velocity = Math.Vector(10,0,0))
  ball_list.append(ball)
  # -------- Main Program Loop -----------
  while not done:

    screen.fill(COLOR.BLACK)
    # Limit to 60 frames per second and get dt
    dt = clock.tick(60)
    # --- Event Processing
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif event.type == pygame.KEYDOWN:
        # Space bar! Spawn a new ball.
        if event.key == pygame.K_SPACE:
          debug = not debug
    # --- Logic
    for ball in ball_list:
      # Move the ball's center
      distance = Math.Vector(350, 250, 0) - ball.position
      distanceMagnitude = distance.magnitude()
      distanceUnit = distance / distanceMagnitude
      force = distanceUnit * (ball.mass * 2000 / distanceMagnitude)
      pygame.draw.line(screen, COLOR.RED, (ball.position.x, ball.position.y), (ball.position.x + force.x, ball.position.y + force.y))

      ball.applyForce(force)
      ball.update(1 / float(dt))

    # --- Drawing
    # Set the screen background
 
    # Draw the balls
    pygame.draw.circle(screen, COLOR.WHITE, (350,250), 10)
    for ball in ball_list:
      ball.draw(screen)
      if debug:
        ball.drawDebug(screen)
        print "position =", ball.position
        print "velocity =", ball.velocity
        print "force =", ball.force
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
  # Close everything down
  pygame.quit()
 
if __name__ == "__main__":
  main()