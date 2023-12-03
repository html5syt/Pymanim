from manim import *
from manim.utils.unit import Percent,Pixels


import subprocess

class test2(Scene):
    def construct(self):
        gr=NumberPlane(x_range=(-10,10),y_range=(-10,10))
        self.play(FadeIn(gr))
        for perc in range(5,51,5):
            c=Circle(radius=perc*Percent(X_AXIS))
            self.play(Create(c),run_time=0.3)
            s=Square(side_length=2*perc*Percent(Y_AXIS),color=BLUE,fill_opacity=0.3)
            self.play(Create(s),run_time=0.3)
    

class test(Scene):
    def construct(self):
        red_dot=Dot(color=RED)
        green_dot=Dot(color=GREEN).next_to(red_dot,RIGHT)
        blue_dot=Dot(color=BLUE).next_to(red_dot,UP)
        dot_group=VGroup(red_dot,green_dot,blue_dot)
        dot_group.to_edge(RIGHT)
        

def sh(command, print_msg=True):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            print(line)
        lines.append(line)
    return lines

if __name__=="__main__":
    sh("python3 -m manim -qm scene.py test")
    