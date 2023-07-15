class ArrowAndNumberline(Scene):
    def construct(self):
        line = NumberLine( x_range= [-5 , 5] ) #создаём объекты 
        lin = Vector(DOWN)
        pointer = ValueTracker(0) #счётчик

        lin.add_updater(
            lambda mob: mob.next_to(line.number_to_point( pointer.get_value()), UP)
            )

        lin.update()

        self.add( line, lin)
        self.wait()

        self.play( pointer.animate.set_value(4))
        self.play( pointer.animate.set_value(-2))
