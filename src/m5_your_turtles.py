"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Robert Fiedler.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

turtle_power = rg.SimpleTurtle('turtle')
turtle_power.pen = rg.Pen('cornsilk', 15)
turtle_power.speed = 100

size = 200

for k in range(8):
    turtle_power.draw_square(size)
    turtle_power.right(45)

turtle_soup = rg.SimpleTurtle('turtle')
turtle_soup.pen = rg.Pen('coral', 10)
turtle_soup.speed = 40

sides = 3

for k in range(8):
    turtle_soup.draw_regular_polygon(sides, 100)
    turtle_soup.right(45)

window.close_on_mouse_click()