#!/usr/bin/env python

from manimlib.imports import *
import random


class OpeningQuote(Scene):
    def construct(self):
        words = TextMobject(
            "``The introduction of vectors for engineering students in Mongolia.''",
        )
        words.to_edge(UP)    
        for mob in words.submobjects[27:27+11]:
            mob.set_color(GREEN)
        author = TextMobject("X-scientist")
        author.set_color(YELLOW)
        author.next_to(words, DOWN, buff = 0.5)

        self.play(FadeIn(words))
        self.wait(1)
        self.play(Write(author, run_time = 4))
        self.wait(2)
        self.play(FadeOut(words))
        self.play(FadeOut(author))
        self.wait(2)

        self.introduce_coordinate_plane()
        self.show_vector_coordinates()
        #self.define_addition()

    def introduce_coordinate_plane(self):
        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        x_label, y_label = plane.get_axis_labels().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)
        #tick_marks = VMobject(x_tick_marks, y_tick_marks)
        #tick_marks.set_color(WHITE)
        plane_lines = [m for m in plane.get_family() if isinstance(m, Line)]
        origin_words = TextMobject("Origin")
        origin_words.shift(2*UP+2*LEFT)
        dot = Dot(radius = 0.1).set_color(RED)
        line = Line(origin_words.get_bottom(), dot.get_corner(UP+LEFT))

        unit_brace = Brace(Line(RIGHT, 2*RIGHT))
        one = TexMobject("1").next_to(unit_brace, DOWN)

        self.add(x_axis, x_label)
        self.wait()
        self.play(ShowCreation(y_axis))
        self.play(Write(y_label, run_time = 1))
        self.wait(2)

        self.play(
            Write(origin_words),
            GrowFromCenter(dot),
            ShowCreation(line),
            run_time = 1
        )
        self.wait(2)
        self.play(
            FadeOut(origin_words)
        )

        self.play(
            FadeOut(line)
        )
        self.remove(origin_words, line)
        self.wait()
        self.play(
            ShowCreation(x_tick_marks)
        )
        self.play(
            ShowCreation(y_tick_marks)
        )


        self.play(
            GrowFromCenter(unit_brace),
            Write(one, run_time = 1)            
        )
        self.wait(2)
        self.remove(unit_brace, one)
        self.play(
            *list(map(GrowFromCenter, plane_lines)) + [
            Animation(x_axis), Animation(y_axis)
        ])
        self.wait()

    def show_vector_coordinates(self):
        starting_mobjects = list(self.mobjects)

        vector1 = Vector([3, 4])
        vector2 = Vector([3, 4])
        vector3 = Vector([2, 3])
        vector1.move_to(UP)
        #v_line=Line(ORIGIN+1.5*LEFT+DOWN,ORIGIN+1.5*LEFT+DOWN+3*RIGHT+4*UP)

        x_line1 = Line(ORIGIN+1.5*LEFT+DOWN, ORIGIN+1.5*LEFT+DOWN+3*RIGHT)
        y_line1 = Line(ORIGIN+1.5*LEFT+DOWN+3*RIGHT, ORIGIN+1.5*LEFT+DOWN+3*RIGHT+4*UP)
        x_line1.set_color(X_COLOR)
        y_line1.set_color(Y_COLOR)


        array1 = vector_coordinate_label(vector2)
        array2 = vector_coordinate_label(vector3)
        x_label1, y_label1 = array1.get_mob_matrix().flatten()
        x_label_copy1 = x_label1.copy()
        x_label_copy1.set_color(X_COLOR)
        y_label_copy1 = y_label1.copy()
        y_label_copy1.set_color(Y_COLOR)


        point1 = Dot(ORIGIN+1.5*LEFT+DOWN)
        point_word1 = TextMobject("(-1.5, -1) \\\\ Beginning of our new vector from origin")
        point_word1.scale(0.7)
        point_word1.next_to(point1, DOWN)
        point1.add(point_word1)

        point2 = Dot(ORIGIN+1.5*LEFT+DOWN+3*RIGHT+4*UP)
        point_word2 = TextMobject("(1.5, 3) \\\\ End of our new vector\\\\ from origin")
        point_word2.scale(0.7)
        point_word2.next_to(point2, DOWN)
        point1.add(point_word2)


        point3 = Dot(ORIGIN+1.5*LEFT+DOWN+3*RIGHT+4*UP)
        point_word3 = TextMobject("(3, 4) \\\\ components of vector")
        point_word3.scale(0.7)

 
        self.play(ShowCreation(vector1))
        self.play(FadeIn(point1))
        self.play(FadeIn(point2))
        self.wait(4) 
        self.play(FadeOut(point1))
        self.play(FadeOut(point2))

        self.play(FadeIn(point3))
        point_word3.next_to(point3, DOWN)
        point3.add(point_word3) 

        self.play(ApplyMethod(x_label_copy1.next_to, x_line1, DOWN))
        self.play(ShowCreation(x_line1))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy1.next_to, y_line1, LEFT))
        self.play(ShowCreation(y_line1))
        self.wait(2)

        self.clear()
        self.add(*starting_mobjects)  
        self.wait(4)

   