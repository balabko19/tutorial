class OpenGLIntro(Scene):
    def construct(self):
        plane = NumberPlane()
        cursor_dot = Dot().move_to( 3*RIGHT + 2*UP)
        red_circle = Circle(
            radius = np.linalg.norm(cursor_dot.get_center())
        )
        red_circle.add_updater(
            lambda mob: mob.become(
            Circle(
            radius=np.linalg.norm(cursor_dot.get_center()),
            color=RED
            )
            
            )
            )
        self.play(Create(plane), Create(red_circle), FadeIn(cursor_dot))
        self.cursor_dot = cursor_dot

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key as pyglet_key
        if symbol == pyglet_key.G:
            self.play(
                self.cursor_dot.animate.move_to(self.mouse_point.get_center())

            )
            super().on_key_press(symbol, modifiers)
