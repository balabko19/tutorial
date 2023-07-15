from manim import *

class UpdaterAndAnimation(Scene):
    def construct(self):
        red_dot =Dot(color = RED).shift(LEFT)
        rotating_square = Square()
        rotating_square.add_updater(
            lambda mob, dt: mob.rotate(PI*dt)
        )

        def shifter(mob, dt):
            mob.shift( 2*dt*RIGHT)

        red_dot.add_updater(shifter)

        self.add( red_dot, rotating_square)
        self.wait(1)
        red_dot.suspend_updating()

        self.play(
            red_dot.animate.shift(UP),
            rotating_square.animate.move_to([-2, -2, 0])    
        )

        self.wait(1)
        
