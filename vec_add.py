#!/usr/bin/env python

from manimlib.imports import *
import random

class VectorAddition(VectorScene):
    def construct(self):
        self.add_plane()
        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        x_label, y_label = plane.get_axis_labels().split()
        self.add(x_axis, x_label)
        self.add(y_axis, y_label)

        words = TextMobject(
            "Education is the passport to the future!"
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

        vects = self.define_addition()
        # vects = map(Vector, [[1, 2], [3, -1], [4, 1]])
        #self.ask_why(*vects)
        #self.answer_why(*vects)

    def define_addition(self):
        v = TexMobject("(2,4)=\\vec{\\textbf{v}}")
        v.set_color(YELLOW)
        vector = Vector([2, 4])
        vector1 = Vector([2, 4])
        vector.move_to(DOWN)
        x_line = Line(ORIGIN+LEFT+3*DOWN, ORIGIN+LEFT+3*DOWN+2*RIGHT)
        y_line = Line(ORIGIN+LEFT+3*DOWN+2*RIGHT, ORIGIN+LEFT+3*DOWN+2*RIGHT+4*UP)
        x_line.set_color(X_COLOR)
        y_line.set_color(Y_COLOR)

        array = vector_coordinate_label(vector1)
        x_label, y_label = array.get_mob_matrix().flatten()
        x_label_copy = x_label.copy()
        x_label_copy.set_color(X_COLOR)
        y_label_copy = y_label.copy()
        y_label_copy.set_color(Y_COLOR)

        point = Dot(ORIGIN+LEFT+3*DOWN)
        point_word = TextMobject("(-1, -3)")
        point_word.scale(0.7)
        point_word.next_to(point, DOWN)
        #point.add(point_word)

        point1 = Dot(ORIGIN+RIGHT+UP)
        point_word1 = TextMobject("(1, 1)")
        point_word1.scale(0.7)
        point_word1.next_to(point1, UP)
        #point.add(point_word1)

        point2 = Dot(ORIGIN+RIGHT+UP)
        point_word2 = TextMobject("(2, 4)")
        point_word2.scale(0.7)
        point_word2.next_to(point2, LEFT)

        point3 = Dot(ORIGIN+RIGHT+UP)
        point_word3 = TextMobject("(1-(-1),1-(-3))=(2,4)")
        point_word3.scale(0.7)
        point_word3.next_to(point2, LEFT)
        self.wait(2)

        self.play(ShowCreation(vector))
        self.play(FadeIn(point_word))
        self.wait(2) 
        self.play(FadeOut(point_word))
        self.wait()

        self.play(FadeIn(point_word1))
        self.wait(2)
        self.play(FadeOut(point_word1))

        self.play(FadeIn(point_word3))
        self.wait(2)
        self.play(FadeOut(point_word3))
        self.wait(4)

        self.play(ApplyMethod(x_label_copy.next_to, x_line, DOWN))
        self.play(ShowCreation(x_line))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy.next_to, y_line, LEFT))
        self.play(ShowCreation(y_line))
        self.wait(2)

        #self.play(FadeIn(point_word2))
        
        #self.play(Write(array))
        self.play(ApplyMethod(v.next_to, point2))
        self.wait(3)
        self.remove(v)
        self.play(
            FadeOut(x_line)
        )

        self.play(
            FadeOut(y_line)
        )
        self.play(
            FadeOut(x_label_copy)
        )

        self.play(
            FadeOut(y_label_copy)
        )

        v = TexMobject("\\vec{\\textbf{v}}")
        v.set_color(YELLOW)
        self.wait(3)

        nums = list(map(TexMobject, ["-1", "\\dfrac{1}{2}", "2"]))
        for mob in [v] + nums:
            mob.scale(1.5)
        self.play(Write(v, run_time = 1))

        last = None
        for num in nums:
            num.next_to(v, LEFT)
            self.wait(3)
            if last:
                self.play(Transform(last, num))
            else:
                self.play(FadeIn(num))
                last = num
            self.wait(3)

        self.play(FadeOut(v))
        self.play(FadeOut(last))
        self.play(FadeOut(vector))
        self.wait(2)

        vector2 = Vector([1, 2])
        x_line = Line(ORIGIN, RIGHT)
        y_line = Line(RIGHT, RIGHT+2*UP)
        x_line.set_color(X_COLOR)
        y_line.set_color(Y_COLOR)

        array = vector_coordinate_label(vector2)
        x_label, y_label = array.get_mob_matrix().flatten()
        x_label_copy = x_label.copy()
        x_label_copy.set_color(X_COLOR)
        y_label_copy = y_label.copy()
        y_label_copy.set_color(Y_COLOR)

        point = Dot(RIGHT+2*UP)
        point_word = TextMobject("(1, 2)")
        point_word.scale(0.7)
        point_word.next_to(point, DOWN)
        #point.add(point_word)

        self.play(ShowCreation(vector2))
        #self.play(FadeIn(point))
        self.wait(2)
        self.play(ApplyMethod(x_label_copy.next_to, x_line, DOWN))
        self.play(ShowCreation(x_line))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy.next_to, y_line, LEFT))
        self.play(ShowCreation(y_line))
        self.wait(2)
        #self.play(FadeOut(point))
        self.play(Write(array))
        self.wait()
        self.play(FadeOut(array))
        self.wait()
        self.play(FadeOut(x_label_copy))
        self.wait()
        self.play(FadeOut(y_label_copy))
        self.wait()
        self.play(FadeOut(x_line))
        self.wait()
        self.play(FadeOut(y_line))
 
        v = TexMobject("-1\\vec{\\textbf{v}}")
        v.set_color(YELLOW)
        v.next_to(vector2,UP)
        self.play(FadeIn(v))
        self.wait(3)
        self.play(FadeOut(v))
        self.remove(vector2)
        self.wait(3)

    ################################################################################
        vector3 = Vector([-1, -2])
        x_line3 = Line(ORIGIN, -1*RIGHT)
        y_line3 = Line(-1*RIGHT, -1*RIGHT+2*DOWN)
        x_line3.set_color(X_COLOR)
        y_line3.set_color(Y_COLOR)
        point_word4 = TextMobject("The direction of the previous vector changed.")
        point_word4.set_color(YELLOW)

        array3 = vector_coordinate_label(vector3)
        x_label3, y_label3 = array3.get_mob_matrix().flatten()
        x_label_copy3 = x_label3.copy()
        x_label_copy3.set_color(X_COLOR)
        y_label_copy3 = y_label3.copy()
        y_label_copy3.set_color(Y_COLOR)

        point3 = Dot(-1*RIGHT+2*DOWN)
        point_word3 = TextMobject("(-1, -2)")
        point_word3.scale(0.7)
        point_word3.next_to(point3, DOWN)
        #point.add(point_word)

        self.play(ShowCreation(vector3))
        #self.play(FadeIn(point))
        self.wait(2)
        self.play(ApplyMethod(x_label_copy3.next_to, x_line3, DOWN))
        self.play(ShowCreation(x_line3))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy3.next_to, y_line3, LEFT))
        self.play(ShowCreation(y_line3))
        self.wait(2)
        #self.play(FadeOut(point))
        self.play(Write(point_word4))
        self.wait(2)
        self.play(FadeOut(point_word4))
        self.wait(2)

        self.play(Write(array3))
        self.wait()
        self.play(FadeOut(array3))
        
        self.wait()
        self.play(FadeOut(x_label_copy3))
        self.wait()
        self.play(FadeOut(y_label_copy3))
        self.wait()
        self.play(FadeOut(x_line3))
        self.wait()
        self.play(FadeOut(y_line3))
        self.remove(vector3)
        self.wait(3)

############################################################################################
        v = TexMobject("2\\vec{\\textbf{v}}")
        v.set_color(YELLOW)
        v.next_to(vector2,UP)

        self.play(ShowCreation(vector2))

        self.play(ApplyMethod(x_label_copy.next_to, x_line, DOWN))
        self.play(ShowCreation(x_line))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy.next_to, y_line, LEFT))
        self.play(ShowCreation(y_line))
        self.wait(2)
        #self.play(FadeOut(point))
        self.play(Write(array))
        self.wait()

        self.play(FadeIn(v))
        self.wait(3)

        self.play(FadeOut(array))
        self.wait()
        self.play(FadeOut(x_label_copy))
        self.wait()
        self.play(FadeOut(y_label_copy))
        self.wait()
        self.play(FadeOut(x_line))
        self.wait()
        self.play(FadeOut(y_line))

        self.play(FadeOut(v))
        self.remove(vector2)
        self.wait(3)

 
#############################################################################################

        vector4 = Vector([2, 4])
        x_line4 = Line(ORIGIN, 2*RIGHT)
        y_line4 = Line(2*RIGHT, 2*RIGHT+4*UP)
        x_line4.set_color(X_COLOR)
        y_line4.set_color(Y_COLOR)
        point_word5 = TextMobject("Two times longer becomes.")
        point_word5.set_color(YELLOW)

        array4 = vector_coordinate_label(vector4)
        x_label4, y_label4 = array4.get_mob_matrix().flatten()
        x_label_copy4 = x_label4.copy()
        x_label_copy4.set_color(X_COLOR)
        y_label_copy4 = y_label4.copy()
        y_label_copy4.set_color(Y_COLOR)

        point4 = Dot(2*RIGHT+4*UP)
        point_word4 = TextMobject("(2, 4)")
        point_word4.scale(0.7)
        point_word4.next_to(point4, DOWN+RIGHT)
        #point.add(point_word)

        self.play(ShowCreation(vector4))
        #self.play(FadeIn(point))
        self.wait(2)
        self.play(ApplyMethod(x_label_copy4.next_to, x_line4, DOWN))
        self.play(ShowCreation(x_line4))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy4.next_to, y_line4, LEFT))
        self.play(ShowCreation(y_line4))
        self.wait(2)
        #self.play(FadeOut(point))
        self.play(Write(point_word5))
        self.wait(2)
        self.play(FadeOut(point_word5))
        self.wait(2)

        self.play(Write(point_word4))
        self.wait(2)
        self.play(FadeOut(point_word4))
        self.wait(2)

        #self.play(Write(array4))
        #self.wait()
        #self.play(FadeOut(array4))
        
        self.wait()
        self.play(FadeOut(x_label_copy4))
        self.wait()
        self.play(FadeOut(y_label_copy4))
        self.wait()
        self.play(FadeOut(x_line4))
        self.wait()
        self.play(FadeOut(y_line4)) 
        self.remove(vector4)

        self.wait(3)


        v1 = self.add_vector([1, 2])
        v2 = self.add_vector([3, -1], color = MAROON_B)
        l1 = self.label_vector(v1, "v")
        l2 = self.label_vector(v2, "w")
        self.wait(3)
        self.play(ApplyMethod(v2.shift, v1.get_end()))
        self.wait(3)
        

        v_sum = self.add_vector(v2.get_end(), color = PINK)
        sum_tex = "\\vec{\\textbf{v}} + \\vec{\\textbf{w}}"
        self.label_vector(v_sum, sum_tex, rotate = True)
        self.wait(5)
        return v1, v2, v_sum



        




