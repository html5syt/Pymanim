from manim import *
from manim.utils.unit import Percent,Pixels
class test(Scene):
    def construct(self):
        gr=NumberPlane(x_range=(-10,10),y_range=(-10,10))
        self.play(FadeIn(gr))
        for perc in range(5,51,5):
            c=Circle(radius=perc*Percent(X_AXIS))
            self.play(Create(c),run_time=0.3)
            s=Square(side_length=2*perc*Percent(Y_AXIS),color=BLUE,fill_opacity=0.3)
            self.play(Create(s),run_time=0.3)