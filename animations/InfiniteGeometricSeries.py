from manimlib.imports import *

CONFIG = {"camera_config": {"background_color": WHITE}}


class Opening(Scene):
    def construct(self):
        title1 = TextMobject("A Visualization of an Infinite Geometric Series")
        title1.set_color(BLACK)
        self.play(FadeIn(title1))
        self.play(FadeOut(title1))


class Formulas(Scene):
    def construct(self):
        formula = TexMobject(
            "S",
            "=",
            "a ",
            "+",
            " a",
            "r ",
            "+",
            "a",
            "r",
            "^2 ",
            "+",
            "a",
            "r",
            "^3 ",
            "+",
            " a",
            "r",
            "^4 ",
            "+",
            " a",
            "r",
            "^5 ",
            "+",
            " a",
            "r",
            "^6 ",
            "+",
            " a",
            "r",
            "^7 ",
            "+",
            " a",
            "r",
            "^8 ",
            "+",
            " ...",
        )
        formulacopy = TexMobject(
            "S",
            "=",
            "a ",
            "+",
            " a",
            "r ",
            "+",
            "a",
            "r",
            "^2 ",
            "+",
            "a",
            "r",
            "^3 ",
            "+",
            " a",
            "r",
            "^4 ",
            "+",
            " a",
            "r",
            "^5 ",
            "+",
            " a",
            "r",
            "^6 ",
            "+",
            " a",
            "r",
            "^7 ",
            "+",
            " a",
            "r",
            "^8 ",
            "+",
            " ...",
        )
        formula2 = TexMobject(
            "r",
            "S",
            "=",
            " a",
            "r ",
            "+",
            "a",
            "r",
            "^2 ",
            "+",
            "a",
            "r",
            "^3 ",
            "+",
            " a",
            "r",
            "^4 ",
            "+",
            " a",
            "r",
            "^5 ",
            "+",
            " a",
            "r",
            "^6 ",
            "+",
            " a",
            "r",
            "^7 ",
            "+",
            " a",
            "r",
            "^8 ",
            "+",
            "a",
            "r",
            "^9",
            "+",
            " ...",
        )
        formula3 = TexMobject("S-rS", " = ", "a")
        section1 = TexMobject("S(1-r)", " = ", "a")
        finalform = TexMobject("S = \\frac{a}{1-r}")
        minus = TexMobject("-")
        minus.rotate(90 * DEGREES)
        minus.shift(UP)
        formula.set_color(BLACK)
        formulacopy.set_color(BLACK)
        formula2.set_color(BLACK)
        formula3.set_color(BLACK)
        section1.set_color(BLACK)
        finalform.set_color(BLACK)
        minus.set_color(BLACK)
        formula[2].set_color("#0087FF")
        formula[4].set_color("#0087FF")
        formula[5].set_color("#FF0F00")
        formulacopy[2].set_color("#0087FF")
        formulacopy[4].set_color("#0087FF")
        formulacopy[5].set_color("#FF0F00")
        formula2[0].set_color("#FF0F00")
        formula2[4].set_color("#FF0F00")
        formula2[3].set_color("#0087FF")
        for n in range(6, 35, 4):
            formula2[n].set_color("#0087FF")
        for n in range(7, 37, 4):
            formula2[n].set_color("#FF0F00")
        for n in range(7, 32, 4):
            formula[n].set_color("#0087FF")
            formulacopy[n].set_color("#0087FF")
        for n in range(8, 33, 4):
            formula[n].set_color("#FF0F00")
            formulacopy[n].set_color("#FF0F00")

        self.play(Write(formula[0]), run_time=1.2)
        self.wait(2)
        self.play(Write(formula[1], run_time=0.7))
        self.play(Write(formula[2]), run_time=0.6)
        self.wait(0.7)
        self.play(Write(formula[3]), run_time=0.3)
        self.play(Write(formula[4]), run_time=0.2)
        self.play(Write(formula[5]), run_time=0.1)
        self.wait()
        for n in range(6, 11, 4):
            self.add(formula[n])
            self.wait(0.5)
            self.play(Write(formula[n + 1]), run_time=0.1)
            self.play(Write(formula[n + 2]), run_time=0.2)
            self.play(Write(formula[n + 3]), run_time=0.4)
            self.wait(0.5)
        for n in range(14, 36):
            self.play(Write(formula[n]), run_time=0.1)
        self.wait()

        self.play(formula.shift, UP * 2)
        self.wait()
        self.play(ReplacementTransform(formula.copy(), formulacopy))
        self.wait()
        self.play(ReplacementTransform(formulacopy, formula2))
        self.wait(2)
        self.play(FadeIn(minus))
        self.play(
            FadeOut(minus),
            ReplacementTransform(formula2, formula3),
            ReplacementTransform(formula, formula3),
        )
        self.wait()
        self.play(Transform(formula3[0], section1[0]))
        self.wait()
        self.play(ReplacementTransform(formula3, finalform))
        self.play(FadeOut(finalform))
        self.wait()
        self.wait()


class Substitution_of_onehalf(Scene):
    def construct(self):
        whenonehalf = TexMobject(
            "\\text{When } r = \\frac{1}{2} \\text{ and } a = \\frac{1}{2}"
        )
        formula1 = TexMobject("S = ", "\\frac{a}{1-r}")
        formula2 = TexMobject(
            "S",
            "=",
            "a ",
            "+ ar ",
            "+ ar^2 ",
            "+ ar^3 ",
            "+ ar^4 ",
            "+ ar^5 ",
            "+ ar^6 ",
            "+ ar^7 ",
            "+ ar^8 ",
            "+ ...",
        )
        substitution = TexMobject("S ", "= \\frac{\\frac{1}{2}}{1-\\frac{1}{2}}")
        simplified = TexMobject("S = 1")
        onehalf = TexMobject(
            "S = \\frac{1}{2} ",
            "+ \\frac{1}{2^2} ",
            "+ \\frac{1}{2^3} ",
            "+ \\frac{1}{2^4} ",
            "+ \\frac{1}{2^5} ",
            "+ \\frac{1}{2^6}",
            "+ \\frac{1}{2^7}",
            "+ \\frac{1}{2^8}",
            "+ ...",
        )
        moredetail = TexMobject(
            "S = \\frac{1}{2} ",
            "+ \\frac{1}{4} ",
            "+ \\frac{1}{8} ",
            "+ \\frac{1}{16} ",
            "+ \\frac{1}{32} ",
            "+ \\frac{1}{64}",
            "+",
            "\\frac{1}{128}",
            "+ ",
            "\\frac{1}{256}",
            "+ ...",
        )
        final = TexMobject(
            "S = \\frac{1}{2} ",
            "+ \\frac{1}{4} ",
            "+ \\frac{1}{8} ",
            "+ \\frac{1}{16} ",
            "+ \\frac{1}{32} ",
            "+ \\frac{1}{64}",
            "+",
            "\\frac{1}{128}",
            "+ ",
            "\\frac{1}{256}",
            "+ ... = 1",
        )
        whenonehalf.set_color(BLACK)
        formula1.set_color(BLACK)
        formula2.set_color(BLACK)
        substitution.set_color(BLACK)
        simplified.set_color(BLACK)
        onehalf.set_color(BLACK)
        moredetail.set_color(BLACK)
        final.set_color(BLACK)
        final.shift(UP * 3.5)
        final.scale(0.5)
        self.play(FadeInFromDown(whenonehalf))
        self.wait()
        self.play(whenonehalf.shift, UP * 3.5 + LEFT * 4.5, whenonehalf.scale, 0.5)
        self.wait()
        self.play(FadeIn(formula2))
        self.wait()
        self.play(ReplacementTransform(formula2, onehalf))
        self.wait()
        self.play(ReplacementTransform(onehalf, moredetail))
        self.wait()
        self.play(moredetail.move_to, UP * 3.5, moredetail.scale, 0.5)
        self.wait()
        self.play(FadeIn(formula1))
        self.wait()
        self.play(ReplacementTransform(formula1, substitution))
        self.wait()
        self.play(ReplacementTransform(substitution, simplified))
        self.wait()
        self.play(FadeOut(simplified), ReplacementTransform(moredetail, final))
        self.wait()


class Square_of_one_half(Scene):
    def construct(self):
        def thelength2(n):
            return 3 / 2 ** (n - 1)

        def thelength(n):
            if n == 0:
                return 0
            else:
                return 3 / 2 ** n + thelength(n - 1)

        def partialsum(n):
            if n == 0:
                return 0
            else:
                return partialsum(n - 1) + 3 / 2 ** (n)

        def rectleft(n):
            if n == 0:
                return 0
            else:
                return partialsum(n - 1) + 0.5 * 3 / 2 ** n

        def rectdown(n):
            if n == 0:
                return 0
            else:
                return rectdown(n - 1) + 3 / 2 ** n

        def squaresleft(n):
            if n == 0:
                return 3 / 2
            else:
                return squaresleft(n - 1) + 3 / 2 ** (n + 1)

        def squaresdown(n):
            if n == 0:
                return 0
            else:
                return partialsum(n - 1) + 3 / 2 ** (n + 1)

        color = color_gradient([RED, YELLOW], 20)
        whenonehalf = TexMobject(
            "\\text{When } r = \\frac{1}{2} \\text{ and } a = \\frac{1}{2}"
        )
        whenonehalf.shift(UP * 3.5 + LEFT * 4.5)
        whenonehalf.scale(0.5)
        whenonehalf.set_color(BLACK)
        rectangles = VGroup()
        squares = VGroup()
        for n in range(1, 10):
            rectangles.add(
                Rectangle(
                    height=thelength2(n - 1), width=thelength2(n), stroke_color=BLACK
                )
            )
            squares.add(Square(side_length=thelength2(n), stroke_color=BLACK))
        ogsquare = Square(side_length=6, stroke_color=BLACK)
        rectangles[0].shift(RIGHT * 1.5)
        for n in range(1, 9):
            rectangles[n].shift(LEFT * rectleft(n), DOWN * rectdown(n))
        squares[0].shift(UP * 1.5, LEFT * 1.5)
        for n in range(1, 9):
            squares[n].shift(LEFT * squaresleft(n), DOWN * squaresdown(n))
        for n in range(0, 18, 2):
            squares[int(n / 2)].set_fill(color[n + 1], opacity=1)
            rectangles[int(n / 2)].set_fill(color[n], opacity=1)
        horizontal_lines = VGroup()
        substitution = TexMobject(
            "S = ",
            "\\frac{1}{2} ",
            "+ ",
            "\\frac{1}{4} ",
            "+ ",
            "\\frac{1}{8} ",
            "+ ",
            "\\frac{1}{16} ",
            "+",
            " \\frac{1}{32} ",
            "+ ",
            "\\frac{1}{64}",
            "+ ",
            "\\frac{1}{128}",
            "+ ",
            "\\frac{1}{256}",
            "+ ...",
            "= 1",
        )
        substitutioncopy = TexMobject(
            "S = ",
            "\\frac{1}{2} ",
            "+ ",
            "\\frac{1}{4} ",
            "+ ",
            "\\frac{1}{8} ",
            "+ ",
            "\\frac{1}{16} ",
            "+",
            " \\frac{1}{32} ",
            "+ ",
            "\\frac{1}{64}",
            "+ ",
            "\\frac{1}{128}",
            "+ ",
            "\\frac{1}{256}",
            "+ ...",
            "=1",
        )
        substitutioncopy.set_color(BLACK)
        substitutioncopy.shift(UP * 3.5)
        substitutioncopy.scale(0.5)
        substitution.shift(UP * 3.5)
        substitution.scale(0.5)
        substitution.set_color(BLACK)
        ###simplifiable?
        vertical_lines = VGroup(
            Line(np.array([0, -3, 0]), np.array([0, 3, 0]), stroke_color=BLACK)
        )
        for n in range(0, 9):
            horizontal_lines.add(
                Line(
                    np.array([-3, -thelength(n), 0]),
                    np.array([-thelength(n), -thelength(n), 0]),
                    stroke_color=BLACK,
                )
            )
        for n in range(1, 9):
            vertical_lines.add(
                Line(
                    np.array([-thelength(n), -3, 0]),
                    np.array([-thelength(n), -thelength(n - 1), 0]),
                    stroke_color=BLACK,
                )
            )
        self.add(substitution)
        self.add(whenonehalf)
        self.play(FadeIn(ogsquare))
        for n in range(1, 14, 4):
            self.play(FadeIn(vertical_lines[int((n - 1) / 4)]))
            self.play(FadeIn(rectangles[int((n - 1) / 4)]))
            self.play(
                substitutioncopy[n].move_to,
                rectangles[int((n - 1) / 4)].get_center(),
                substitutioncopy[n].scale,
                8 / 2 ** ((n - 1) / 4),
            )
            self.play(FadeIn(horizontal_lines[int((n - 1) / 4)]))
            self.play(FadeIn(squares[int((n - 1) / 4)]))
            self.play(
                substitutioncopy[n + 2].move_to,
                squares[int((n - 1) / 4)].get_center(),
                substitutioncopy[n + 2].scale,
                8 / 2 ** ((n + 3) / 4),
            )
        for n in range(4, 9):
            self.play(FadeIn(vertical_lines[n]), run_time=0.8 / n)
            self.play(FadeIn(rectangles[n]), run_time=0.8 / n)
            self.play(FadeIn(horizontal_lines[n]), run_time=0.8 / n)
            self.play(FadeIn(squares[n]), run_time=0.8 / n)
        self.wait()


class Substituion_of_one_third(Scene):
    def construct(self):
        whenonehalf = TexMobject(
            "\\text{When } r = \\frac{1}{3} \\text{ and } a = \\frac{1}{3}"
        )
        formula1 = TexMobject("S = ", "\\frac{a}{1-r}")
        formula2 = TexMobject(
            "S",
            "=",
            "a ",
            "+ ar ",
            "+ ar^2 ",
            "+ ar^3 ",
            "+ ar^4 ",
            "+ ar^5 ",
            "+ ar^6 ",
            "+ ar^7 ",
            "+ ar^8 ",
            "+ ...",
        )
        substitution = TexMobject("S ", "= \\frac{\\frac{1}{3}}{1-\\frac{1}{3}}")
        simplified = TexMobject("S = \\frac{1}{2}")
        onehalf = TexMobject(
            "S = \\frac{1}{3} ",
            "+ \\frac{1}{3^2} ",
            "+ \\frac{1}{3^3} ",
            "+ \\frac{1}{3^4} ",
            "+ \\frac{1}{3^5} ",
            "+ \\frac{1}{3^6}",
            "+ ...",
        )
        moredetail = TexMobject(
            "S = \\frac{1}{3} ",
            "+ \\frac{1}{9} ",
            "+ \\frac{1}{27} ",
            "+ \\frac{1}{81} ",
            "+ \\frac{1}{243} ",
            "+ \\frac{1}{729}",
            "+ ...",
        )
        final = TexMobject(
            "S = \\frac{1}{3} ",
            "+ \\frac{1}{9} ",
            "+ \\frac{1}{27} ",
            "+ \\frac{1}{81} ",
            "+ \\frac{1}{243} ",
            "+ \\frac{1}{729}",
            "+ ... = \\frac{1}{2}",
        )
        whenonehalf.set_color(BLACK)
        formula1.set_color(BLACK)
        formula2.set_color(BLACK)
        substitution.set_color(BLACK)
        simplified.set_color(BLACK)
        onehalf.set_color(BLACK)
        moredetail.set_color(BLACK)
        final.set_color(BLACK)
        final.shift(UP * 3.5)
        final.scale(0.5)
        self.play(FadeInFromDown(whenonehalf))
        self.wait()
        self.play(whenonehalf.shift, UP * 3.5 + LEFT * 4.5, whenonehalf.scale, 0.5)
        self.wait()
        self.play(FadeIn(formula2))
        self.wait()
        self.play(ReplacementTransform(formula2, onehalf))
        self.wait()
        self.play(ReplacementTransform(onehalf, moredetail))
        self.wait()
        self.play(moredetail.move_to, UP * 3.5, moredetail.scale, 0.5)
        self.wait()
        self.play(FadeIn(formula1))
        self.wait()
        self.play(ReplacementTransform(formula1, substitution))
        self.wait()
        self.play(ReplacementTransform(substitution, simplified))
        self.wait()
        self.play(FadeOut(simplified), ReplacementTransform(moredetail, final))
        self.wait()


class Square_of_one_third(MovingCameraScene):
    def construct(self):
        def length(n):
            return 3 / 3 ** n

        whenonehalf = TexMobject(
            "\\text{When } r = \\frac{1}{3} \\text{ and } a = \\frac{1}{3}"
        )
        whenonehalf.shift(UP * 3.5, LEFT * 4.5)
        whenonehalf.set_color(BLACK)
        whenonehalf.scale(0.5)
        tex = TexMobject(
            "S = ",
            "\\frac{1}{3} ",
            "+ ",
            "\\frac{1}{9} ",
            "+ ",
            "\\frac{1}{27} ",
            "+ ",
            "\\frac{1}{81}",
            "+",
            "\\frac{1}{243}",
            "+ ",
            "\\frac{1}{729}",
            "+ ...",
            "= \\frac{1}{2}",
        )
        tex.shift(UP * 3.5)
        tex.scale(0.5)
        texcopy = TexMobject(
            "S = ",
            "\\frac{1}{3} ",
            "+ ",
            "\\frac{1}{9} ",
            "+ ",
            "\\frac{1}{27} ",
            "+ ",
            "\\frac{1}{81}",
            "+",
            "\\frac{1}{243}",
            "+ ",
            "\\frac{1}{729}",
            "+ ...",
            "= \\frac{1}{2}",
        )
        texcopy.shift(UP * 3.5)
        texcopy.scale(0.5)
        tex.set_color(BLACK)
        texcopy.set_color(BLACK)
        ogsquare = Square(side_length=6, stroke_color=BLACK)
        vertical_lines1 = VGroup()
        horizontal_lines1 = VGroup()
        vertical_lines2 = VGroup()
        horizontal_lines2 = VGroup()
        rectangles = VGroup()
        squares = VGroup()
        specialrect = VGroup(
            Rectangle(width=2, height=6, stroke_color=BLACK),
            Rectangle(width=2, height=6, stroke_color=BLACK),
        )
        specialsq = VGroup(
            Square(side_length=2, stroke_color=BLACK),
            Square(side_length=2, stroke_color=BLACK),
        )
        for n in range(0, 9):
            rectangles.add(VGroup())
            squares.add(VGroup())
            for i in range(0, 2):
                rectangles[-1].add(
                    Rectangle(width=2 / 3 ** n, height=6 / 3 ** n, stroke_color=BLACK)
                )
                squares[-1].add(Square(side_length=2 / 3 ** n, stroke_color=BLACK))
        specialrect[0].shift(LEFT * 2)
        specialrect[1].shift(RIGHT * 2)
        specialsq[0].shift(UP * 2)
        specialsq[1].shift(DOWN * 2)
        for n in range(1, 9):
            rectangles[n][0].shift(LEFT * (-3 / 3 ** (n + 1) - 3 / 3 ** (n)) / 2)
            squares[n][0].shift(UP * (-3 / 3 ** (n + 1) - 3 / 3 ** (n)) / 2)
            rectangles[n][1].shift(RIGHT * (-3 / 3 ** (n + 1) - 3 / 3 ** (n)) / 2)
            squares[n][1].shift(DOWN * (-3 / 3 ** (n + 1) - 3 / 3 ** (n)) / 2)
        specialrect[1].set_fill(BLUE, opacity=1)
        specialrect[0].set_fill(RED, opacity=1)
        specialsq[1].set_fill(BLUE, opacity=1)
        specialsq[0].set_fill(RED, opacity=1)
        for n in range(2, 9, 2):
            rectangles[n][0].set_fill(BLUE, opacity=1)
            rectangles[n][1].set_fill(RED, opacity=1)
            squares[n][0].set_fill(BLUE, opacity=1)
            squares[n][1].set_fill(RED, opacity=1)
        for n in range(1, 9, 2):
            rectangles[n][1].set_fill(BLUE, opacity=1)
            rectangles[n][0].set_fill(RED, opacity=1)
            squares[n][1].set_fill(BLUE, opacity=1)
            squares[n][0].set_fill(RED, opacity=1)
        for n in range(0, 9):
            vertical_lines1.add(
                Line(
                    np.array([-3 / 3 ** (n + 1), length(n), 0]),
                    np.array([-3 / 3 ** (n + 1), -length(n), 0]),
                    stroke_color=BLACK,
                )
            )
            vertical_lines2.add(
                Line(
                    np.array([3 / 3 ** (n + 1), length(n), 0]),
                    np.array([3 / 3 ** (n + 1), -length(n), 0]),
                    stroke_color=BLACK,
                )
            )
            horizontal_lines1.add(
                Line(
                    np.array([length(n + 1), 3 / 3 ** (n + 1), 0]),
                    np.array([-length(n + 1), 3 / 3 ** (n + 1), 0]),
                    stroke_color=BLACK,
                )
            )
            horizontal_lines2.add(
                Line(
                    np.array([length(n + 1), -3 / 3 ** (n + 1), 0]),
                    np.array([-length(n + 1), -3 / 3 ** (n + 1), 0]),
                    stroke_color=BLACK,
                )
            )
        self.add(tex)
        self.add(whenonehalf)
        self.play(ShowCreation(ogsquare))
        for n in range(0, 1):
            self.play(FadeIn(vertical_lines1[0]), FadeIn(vertical_lines2[0]))
            self.play(FadeIn(specialrect[0]))
            self.play(
                texcopy[(n + 1)].move_to,
                LEFT * 2 / 3 ** (n / 4),
                texcopy[(n + 1)].scale,
                4 / 3 ** ((n / 4)),
            )
            self.play(FadeIn(horizontal_lines1[0]), FadeIn(horizontal_lines2[0]))
            self.play(FadeIn(specialsq[0]))
            self.play(
                texcopy[(n + 3)].move_to,
                UP * 2 / 3 ** (n / 4),
                texcopy[(n + 3)].scale,
                4 / 3 ** ((n / 4) + 0.5),
            )
        for n in range(4, 9, 4):
            self.play(
                FadeIn(vertical_lines1[int(n / 4)]), FadeIn(vertical_lines2[int(n / 4)])
            )
            if n == 4:
                self.play(FadeIn(rectangles[int(n / 4)][0]))
                self.play(
                    texcopy[(n + 1)].move_to,
                    RIGHT * 2 / 3 ** (n / 4),
                    texcopy[(n + 1)].scale,
                    4 / 3 ** ((n / 4)),
                )
            else:
                self.play(FadeIn(rectangles[int(n / 4)][1]))
                self.play(
                    texcopy[(n + 1)].move_to,
                    LEFT * 2 / 3 ** (n / 4),
                    texcopy[(n + 1)].scale,
                    4 / 3 ** ((n / 4)),
                )
            self.play(
                FadeIn(horizontal_lines1[int(n / 4)]),
                FadeIn(horizontal_lines2[int(n / 4)]),
            )
            if n == 4:
                self.play(FadeIn(squares[int(n / 4)][0]))
                self.play(
                    texcopy[(n + 3)].move_to,
                    DOWN * 2 / 3 ** (n / 4),
                    texcopy[(n + 3)].scale,
                    4 / 3 ** ((n / 4) + 0.5),
                )
            else:
                self.play(FadeIn(squares[int(n / 4)][1]))
                self.play(
                    texcopy[(n + 3)].move_to,
                    UP * 2 / 3 ** (n / 4),
                    texcopy[(n + 3)].scale,
                    4 / 3 ** ((n / 4) + 0.5),
                )

        for n in range(3, 9):
            if n % 2 == 0:
                self.play(FadeIn(rectangles[n][1]), run_time=1 / n)
                self.play(FadeIn(squares[n][1]), run_time=1 / n)
            else:
                self.play(FadeIn(rectangles[n][0]), run_time=1 / n)
                self.play(FadeIn(squares[n][0]), run_time=1 / n)

        for n in range(0, 1):
            self.play(FadeIn(specialrect[n + 1]))
            self.play(FadeIn(specialsq[n + 1]))
        for n in range(1, 9):
            if n % 2 != 0:
                self.play(FadeIn(rectangles[n][1]), run_time=0.5 / (n))
                self.play(FadeIn(squares[n][1]), run_time=0.5 / n)
            else:
                self.play(FadeIn(rectangles[n][0]), run_time=0.5 / n)
                self.play(FadeIn(squares[n][0]), run_time=0.5 / n)
        self.wait()
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.move_to,
            np.array([0, 0, 0]),
            self.camera_frame.set_width,
            0.20,
            run_time=5,
        )
        self.wait(0.5)
        self.play(Restore(self.camera_frame), run_time=3.5)


class Substitution_of_one_fourth(Scene):
    def construct(self):
        whenonefourth = TexMobject(
            "\\text{When } r = \\frac{1}{4} \\text{ and } a = \\frac{1}{4}"
        )
        formula1 = TexMobject("S =", " \\frac{a}{1-r}")
        formula2 = TexMobject(
            "S",
            "=",
            "a ",
            "+ ar ",
            "+ ar^2 ",
            "+ ar^3 ",
            "+ ar^4 ",
            "+ ar^5 ",
            "+ ar^6 ",
            "+ ar^7 ",
            "+ ar^8 ",
            "+ ...",
        )
        substitution = TexMobject("S =", " \\frac{\\frac{1}{4}}{1-\\frac{1}{4}}")
        simplified = TexMobject("S =", " \\frac{1}{3}")
        onefourth = TexMobject(
            "S = \\frac{1}{4} ",
            "+ \\frac{1}{4^2} ",
            "+ \\frac{1}{4^3} ",
            "+ \\frac{1}{4^4} ",
            "+ \\frac{1}{4^5} ",
            "+ ...",
        )
        moredetail = TexMobject(
            "S = \\frac{1}{4} ",
            "+ \\frac{1}{16} ",
            "+ \\frac{1}{64} ",
            "+ \\frac{1}{256} ",
            "+ \\frac{1}{1024} ",
            "+ ...",
        )
        final = TexMobject(
            "S = \\frac{1}{4} ",
            "+ \\frac{1}{16} ",
            "+ \\frac{1}{64} ",
            "+ \\frac{1}{256} ",
            "+ \\frac{1}{1024} ",
            "+ ... = \\frac{1}{3}",
        )
        whenonefourth.set_color(BLACK)
        formula1.set_color(BLACK)
        formula2.set_color(BLACK)
        substitution.set_color(BLACK)
        simplified.set_color(BLACK)
        onefourth.set_color(BLACK)
        moredetail.set_color(BLACK)
        final.set_color(BLACK)
        final.shift(UP * 3.5)
        final.scale(0.5)
        self.play(FadeInFromDown(whenonefourth))
        self.wait()
        self.play(whenonefourth.shift, UP * 3.5 + LEFT * 4.5, whenonefourth.scale, 0.5)
        self.wait()
        self.play(FadeIn(formula2))
        self.wait()
        self.play(ReplacementTransform(formula2, onefourth))
        self.wait()
        self.play(ReplacementTransform(onefourth, moredetail))
        self.wait()
        self.play(moredetail.move_to, UP * 3.5, moredetail.scale, 0.5)
        self.wait()
        self.play(FadeIn(formula1))
        self.wait()
        self.play(ReplacementTransform(formula1, substitution))
        self.wait()
        self.play(ReplacementTransform(substitution, simplified))
        self.wait()
        self.play(FadeOut(simplified), ReplacementTransform(moredetail, final))
        self.wait()


class FractalCreation(Scene):
    CONFIG = {
        "fractal_class": KochSnowFlake,
        "max_order": 5,
        "transform_kwargs": {
            "path_arc": 0,
            "lag_ratio": 0.5,
            "run_time": 2,
        },
        "fractal_kwargs": {},
    }

    def construct(self):
        fractal = self.fractal_class(order=0, **self.fractal_kwargs)
        text = TextMobject("Koch Snowflake")
        text.set_color_by_gradient(BLUE, BLUE_A)
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text))
        self.play(FadeIn(fractal))
        for order in range(1, self.max_order + 1):
            new_fractal = self.fractal_class(order=order, **self.fractal_kwargs)
            fractal.align_data(new_fractal)
            self.play(Transform(fractal, new_fractal, **self.transform_kwargs))
            self.wait()
        self.wait()
        self.fractal = fractal


class Square_of_one_fourth(MovingCameraScene):
    def construct(self):
        whenonehalf = TexMobject(
            "\\text{When } r = \\frac{1}{4} \\text{ and } a = \\frac{1}{4}"
        )
        whenonehalf.shift(UP * 3.5, LEFT * 4.5)
        whenonehalf.set_color(BLACK)
        whenonehalf.scale(0.5)
        tex = TexMobject(
            "S = ",
            "\\frac{1}{4} ",
            "+ ",
            "\\frac{1}{16} ",
            "+ ",
            "\\frac{1}{64} ",
            "+ ",
            "\\frac{1}{256}",
            "+",
            "\\frac{1}{1024}",
            "+ ...",
            "= \\frac{1}{3}",
        )
        tex.shift(UP * 3.5)
        tex.scale(0.5)
        texcopy = TexMobject(
            "S = ",
            "\\frac{1}{4} ",
            "+ ",
            "\\frac{1}{16} ",
            "+ ",
            "\\frac{1}{64} ",
            "+ ",
            "\\frac{1}{256}",
            "+",
            "\\frac{1}{1024}",
            "+ ...",
            "= \\frac{1}{3}",
        )
        texcopy.shift(UP * 3.5)
        texcopy.scale(0.5)
        tex.set_color(BLACK)
        texcopy.set_color(BLACK)
        ogsquare = Rectangle(height=6, width=6, stroke_width=2, color=BLACK)
        linehorizontal1 = []
        linevertical1 = []
        linehorizontal2 = []
        linevertical2 = []

        def size(n):
            return 4 * 2 ** (n)

        def sqvalue(n):
            if n == 0:
                return 0
            else:
                return 3 / (2 ** n) + sqvalue(n - 1)

        for k in range(3, 50, 2):
            linehorizontal1.append([sqvalue((k - 3) / 2), sqvalue((k - 1) / 2), 0])
            linehorizontal2.append([3, sqvalue((k - 1) / 2), 0])
            linevertical1.append([sqvalue((k - 1) / 2), sqvalue((k - 3) / 2), 0])
            linevertical2.append([sqvalue((k - 1) / 2), 3, 0])

        line = VGroup(
            Line(
                np.array([3, 0, 0]), np.array([-3, 0, 0]), stroke_width=2, color=BLACK
            ),
            Line(
                np.array([0, -3, 0]), np.array([0, 3, 0]), stroke_width=2, color=BLACK
            ),
            Line(
                np.array([0, 1.5, 0]),
                np.array([3, 1.5, 0]),
                stroke_width=2,
                color=BLACK,
            ),
            Line(
                np.array([1.5, 0, 0]),
                np.array([1.5, 3, 0]),
                stroke_width=2,
                color=BLACK,
            ),
        )

        for n in range(1, 8):
            line.add(
                Line(
                    np.array(linehorizontal1[n]),
                    np.array(linehorizontal2[n]),
                    stroke_width=2,
                    color=BLACK,
                )
            )
            line.add(
                Line(
                    np.array(linevertical1[n]),
                    np.array(linevertical2[n]),
                    stroke_width=2,
                    color=BLACK,
                )
            )
        # Functions
        def partialsum(n):
            if n == 1:
                return 3 / 2
            else:
                return partialsum(n - 1) + 3 / (2 ** n)

        def centersq_position(n):
            if n == 1:
                return partialsum(1)
            else:
                return partialsum(n - 1) + 3 / (2 * 2 ** (n))

        def sidelength(n):
            return 3 / 2 ** (n - 1)

        def size(n):
            return 4 ** (n + 1)

        # Creating Mobjects sets
        squares = VGroup()
        newsquares = VGroup()
        text = VGroup()
        for n in range(1, 17):
            squares.add(VGroup())
            for i in range(1, 4):
                squares[-1].add(Square(side_length=sidelength(n)))

        squares.set_stroke(BLACK, width=2)

        for n in range(1, 17):
            newsquares.add(VGroup())
            for i in range(1, 4):
                newsquares[-1].add(Square(side_length=sidelength(n)))

        newsquares.set_stroke(BLACK, width=2)

        for n in range(0, 9):
            text.add(TexMobject("1 \\over" + str(size(n))))

        text.set_color(BLACK)

        # Creating base objects & positioning objects

        squares[0][1].next_to(squares[0][0], UP, buff=0)
        squares[0][2].shift(RIGHT * 1.5, DOWN * 1.5)
        for n in range(1, 16):
            squares[n][0].next_to(squares[n - 1][0].get_corner(UR), UR, buff=0)
            squares[n][1].next_to(squares[n][0], UP, buff=0)
            squares[n][2].next_to(squares[n][0], RIGHT, buff=0)

        newsquares[0][0].shift(LEFT * 1.5, DOWN * 1.5)
        newsquares[0][1].next_to(newsquares[0][0], UP, buff=0)
        newsquares[0][2].shift(RIGHT * 1.5, DOWN * 1.5)
        for n in range(1, 16):
            newsquares[n][0].next_to(newsquares[n - 1][0].get_corner(UR), UR, buff=0)
            newsquares[n][1].next_to(newsquares[n][0], UP, buff=0)
            newsquares[n][2].next_to(newsquares[n][0], RIGHT, buff=0)

        text[0].shift(DOWN * 1.5, LEFT * 1.5)
        text[0].scale(2)
        for n in range(1, 8):
            text[n].move_to(newsquares[n][0].get_center())
        text[1].scale(1)
        text[2].scale(1 / 2)
        text[3].scale(1 / 4)
        text[4].scale(1 / 8)
        text[5].scale(1 / 16)
        text[6].scale(1 / 32)
        text[7].scale(1 / 64)
        text[8].scale(1 / 128)

        # color filling newsquares
        for n in range(0, 16):
            newsquares[n][0].set_fill("#FF0000", opacity=1)
            newsquares[n][1].set_fill("#FFE500", opacity=1)
            newsquares[n][2].set_fill("#008AFC", opacity=1)
        self.add(tex)
        self.add(whenonehalf)
        self.play(FadeIn(ogsquare))

        for n in range(0, 10, 2):
            self.play(
                GrowFromCenter(line[n]),
                GrowFromCenter(line[n + 1]),
                run_time=4 / (n + 4),
            )
            self.play(FadeIn(newsquares[int(n / 2)][0]), run_time=1 / (n + 1))
            self.play(
                texcopy[n + 1].move_to,
                newsquares[int(n / 2)][0].get_center(),
                texcopy[n + 1].scale,
                2 / 2 ** (n / 2 - 1),
            )
        for n in range(10, 18, 2):
            self.play(
                GrowFromCenter(line[n]),
                GrowFromCenter(line[n + 1]),
                run_time=4 / (n + 4),
            )
            self.play(FadeIn(newsquares[int(n / 2)][0]), run_time=1 / (n + 1))
        self.play(*[FadeIn(newsquares[n][0], run_time=1) for n in range(9, 14)])
        for n in range(0, 8):
            self.play(
                FadeIn(newsquares[n][1]), FadeIn(newsquares[n][2]), run_time=1 / (n + 1)
            )
        self.play(*[FadeIn(newsquares[n][1], run_time=1) for n in range(8, 14)])
        self.play(*[FadeIn(newsquares[n][2], run_time=0.1) for n in range(8, 14)])

        self.remove(*[line[n] for n in range(0, 18)])

        self.play(*[FadeOut(texcopy[n]) for n in range(0, 12)])

        self.remove(ogsquare)
        # cameracontrol

        self.camera_frame.save_state()
        self.play(
            self.camera_frame.move_to,
            newsquares[6][0],
            self.camera_frame.set_width,
            0.51,
            run_time=5,
        )
        self.wait(0.5)
        self.play(Restore(self.camera_frame), run_time=2)
        # Seperation scene

        self.play(
            newsquares[0][0].move_to,
            DOWN * 1.5,
            newsquares[0][1].move_to,
            DOWN * 1.5 + LEFT * 4.5,
            newsquares[0][2].move_to,
            DOWN * 1.5 + RIGHT * 4.5,
            newsquares[1][0].move_to,
            UP * 0.75,
            newsquares[1][1].move_to,
            UP * 0.75 + LEFT * 4.5,
            newsquares[1][2].move_to,
            UP * 0.75 + RIGHT * 4.5,
            newsquares[2][0].move_to,
            UP * centersq_position(2),
            newsquares[2][1].move_to,
            UP * centersq_position(2) + LEFT * 4.5,
            newsquares[2][2].move_to,
            UP * centersq_position(2) + RIGHT * 4.5,
            newsquares[3][0].move_to,
            UP * centersq_position(3),
            newsquares[3][1].move_to,
            UP * centersq_position(3) + LEFT * 4.5,
            newsquares[3][2].move_to,
            UP * centersq_position(3) + RIGHT * 4.5,
            newsquares[4][0].move_to,
            UP * centersq_position(4),
            newsquares[4][1].move_to,
            UP * centersq_position(4) + LEFT * 4.5,
            newsquares[4][2].move_to,
            UP * centersq_position(4) + RIGHT * 4.5,
            newsquares[5][0].move_to,
            UP * centersq_position(5),
            newsquares[5][1].move_to,
            UP * centersq_position(5) + LEFT * 4.5,
            newsquares[5][2].move_to,
            UP * centersq_position(5) + RIGHT * 4.5,
            newsquares[6][0].move_to,
            UP * centersq_position(6),
            newsquares[6][1].move_to,
            UP * centersq_position(6) + LEFT * 4.5,
            newsquares[6][2].move_to,
            UP * centersq_position(6) + RIGHT * 4.5,
            newsquares[7][0].move_to,
            UP * centersq_position(7),
            newsquares[7][1].move_to,
            UP * centersq_position(7) + LEFT * 4.5,
            newsquares[7][2].move_to,
            UP * centersq_position(7) + RIGHT * 4.5,
            newsquares[8][0].move_to,
            UP * centersq_position(8),
            newsquares[8][1].move_to,
            UP * centersq_position(8) + LEFT * 4.5,
            newsquares[8][2].move_to,
            UP * centersq_position(8) + RIGHT * 4.5,
            newsquares[9][0].move_to,
            UP * centersq_position(9),
            newsquares[9][1].move_to,
            UP * centersq_position(9) + LEFT * 4.5,
            newsquares[9][2].move_to,
            UP * centersq_position(9) + RIGHT * 4.5,
            newsquares[10][0].move_to,
            UP * centersq_position(10),
            newsquares[10][1].move_to,
            UP * centersq_position(10) + LEFT * 4.5,
            newsquares[10][2].move_to,
            UP * centersq_position(10) + RIGHT * 4.5,
            newsquares[11][0].move_to,
            UP * centersq_position(11),
            newsquares[11][1].move_to,
            UP * centersq_position(11) + LEFT * 4.5,
            newsquares[11][2].move_to,
            UP * centersq_position(11) + RIGHT * 4.5,
            newsquares[12][0].move_to,
            UP * centersq_position(12),
            newsquares[12][1].move_to,
            UP * centersq_position(12) + LEFT * 4.5,
            newsquares[12][2].move_to,
            UP * centersq_position(12) + RIGHT * 4.5,
            newsquares[13][0].move_to,
            UP * centersq_position(13),
            newsquares[13][1].move_to,
            UP * centersq_position(13) + LEFT * 4.5,
            newsquares[13][2].move_to,
            UP * centersq_position(13) + RIGHT * 4.5,
            newsquares[14][0].move_to,
            UP * centersq_position(14),
            newsquares[14][1].move_to,
            UP * centersq_position(14) + LEFT * 4.5,
            newsquares[14][2].move_to,
            UP * centersq_position(14) + RIGHT * 4.5,
        )

        self.wait(2)

        # combining scene
        self.play(
            newsquares[0][1].move_to,
            newsquares[0][0],
            newsquares[0][2].move_to,
            newsquares[0][0],
            newsquares[1][1].move_to,
            newsquares[1][0],
            newsquares[1][2].move_to,
            newsquares[1][0],
            newsquares[2][1].move_to,
            newsquares[2][0],
            newsquares[2][2].move_to,
            newsquares[2][0],
            newsquares[3][1].move_to,
            newsquares[3][0],
            newsquares[3][2].move_to,
            newsquares[3][0],
            newsquares[4][1].move_to,
            newsquares[4][0],
            newsquares[4][2].move_to,
            newsquares[4][0],
            newsquares[5][1].move_to,
            newsquares[5][0],
            newsquares[5][2].move_to,
            newsquares[5][0],
            newsquares[6][1].move_to,
            newsquares[6][0],
            newsquares[6][2].move_to,
            newsquares[6][0],
            newsquares[7][1].move_to,
            newsquares[7][0],
            newsquares[7][2].move_to,
            newsquares[7][0],
            newsquares[8][1].move_to,
            newsquares[8][0],
            newsquares[8][2].move_to,
            newsquares[8][0],
            newsquares[9][1].move_to,
            newsquares[9][0],
            newsquares[9][2].move_to,
            newsquares[9][0],
            newsquares[10][1].move_to,
            newsquares[10][0],
            newsquares[10][2].move_to,
            newsquares[10][0],
            newsquares[11][1].move_to,
            newsquares[11][0],
            newsquares[11][2].move_to,
            newsquares[11][0],
            newsquares[12][1].move_to,
            newsquares[12][0],
            newsquares[12][2].move_to,
            newsquares[12][0],
            newsquares[13][1].move_to,
            newsquares[13][0],
            newsquares[13][2].move_to,
            newsquares[13][0],
            newsquares[14][1].move_to,
            newsquares[14][0],
            newsquares[14][2].move_to,
            newsquares[14][0],
        )
        self.wait(2)


class FibonacciSpiral(MovingCameraScene):
    def construct(self):
        def fib(n):
            if n <= 1:
                return 1
            else:
                return fib(n - 1) + fib(n - 2)

        text = TextMobject("More of Fractals(self-similar patterns)")
        text.set_color_by_gradient(BLUE, BLUE_A)
        text2 = TextMobject("Golden Spiral")
        text2.set_color_by_gradient(YELLOW, GOLD)
        squares = VGroup()

        for n in range(0, 29, 4):
            squares.add(
                Square(
                    side_length=fib(n),
                    fill_color=WHITE,
                    fill_opacity=1,
                    stroke_width=1,
                    stroke_color=BLACK,
                )
            )
            squares.add(
                Square(
                    side_length=fib(n + 1),
                    fill_color=WHITE,
                    fill_opacity=1,
                    stroke_width=1,
                    stroke_color=BLACK,
                )
            )
            squares.add(
                Square(
                    side_length=fib(n + 2),
                    fill_color=WHITE,
                    fill_opacity=1,
                    stroke_width=1,
                    stroke_color=BLACK,
                )
            )
            squares.add(
                Square(
                    side_length=fib(n + 3),
                    fill_color=WHITE,
                    fill_opacity=1,
                    stroke_width=1,
                    stroke_color=BLACK,
                )
            )

        for n in range(1, 26, 4):
            squares[n].next_to(squares[n - 1], RIGHT, aligned_edge=DOWN, buff=0)
            squares[n + 1].next_to(squares[n], UP, aligned_edge=RIGHT, buff=0)
            squares[n + 2].next_to(squares[n + 1], LEFT, aligned_edge=UP, buff=0)
            squares[n + 3].next_to(squares[n + 2], DOWN, aligned_edge=LEFT, buff=0)

        arcs = VGroup()

        for n in range(0, 26, 4):
            arcs.add(
                Arc(radius=fib(n), angle=TAU / 4, start_angle=TAU / 2, stroke_width=3)
            )
            arcs.add(
                Arc(
                    radius=fib(n + 1),
                    angle=TAU / 4,
                    start_angle=TAU * 3 / 4,
                    stroke_width=3,
                )
            )
            arcs.add(
                Arc(radius=fib(n + 2), angle=TAU / 4, start_angle=0, stroke_width=3)
            )
            arcs.add(
                Arc(
                    radius=fib(n + 3),
                    angle=TAU / 4,
                    start_angle=TAU / 4,
                    stroke_width=3,
                )
            )
        for n in range(0, 26, 4):
            arcs[n].set_color_by_gradient(RED, ORANGE)
            arcs[n + 1].set_color_by_gradient(ORANGE, "#FFC100")
            arcs[n + 2].set_color_by_gradient("#FFC100", "#FF0000")
            arcs[n + 3].set_color_by_gradient("#FF0000", RED)
        for n in range(0, 26, 4):
            arcs[n].next_to(squares[n], UP, aligned_edge=DOWN, buff=-fib(n) / 2)
            arcs[n + 1].next_to(
                squares[n + 1], UP, aligned_edge=DOWN, buff=-fib(n + 1) / 2
            )
            arcs[n + 2].next_to(
                squares[n + 2], UP, aligned_edge=DOWN, buff=-fib(n + 2) / 2
            )
            arcs[n + 3].next_to(
                squares[n + 3], UP, aligned_edge=DOWN, buff=-fib(n + 3) / 2
            )

        for n in range(0, 26):
            self.add(squares[n])
            self.add(arcs[n])
        self.play(FadeInFromDown(text))
        self.play(FadeOut(text))
        self.wait(0.5)
        self.play(FadeIn(text2))
        self.play(FadeOut(text2))
        self.wait()
        self.play(self.camera_frame.set_width, 80000, run_time=20)
        self.wait()


class Closingcredits(Scene):
    def construct(self):
        anim = TextMobject("\\textit{Animated By}")
        anim.scale(2.5)
        anim.set_color(BLACK)
        creator = TextMobject("Ausbxuse")
        creator.scale(2.5)
        creator.set_color_by_gradient("#0087FF", BLUE_A)
        self.play(FadeInFromLarge(anim))
        self.play(ReplacementTransform(anim, creator))
        self.wait(4)
        self.play(FadeOut(creator))
