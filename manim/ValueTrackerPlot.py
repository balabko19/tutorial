class ValueTrackerPlot(Scene):
    def construct(self):

        a =ValueTracker(1)
        ax = Axes(x_range= [-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        parabola = ax.plot( lambda x: x ** 2 , color = RED)
        parabola.add_updater(
            lambda mob:mob.become(ax.plot( lambda x: a.get_value() * x**2, color = RED))
        )

        a_number = DecimalNumber(
            a.get_value(), 
            color=RED, 
            num_decimal_places=3,
            show_ellipsis=True
        )

        a_number.add_updater(
            lambda mob:
            mob.set_value( a.get_value()).next_to(parabola, RIGHT)

        )

        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-3))        
