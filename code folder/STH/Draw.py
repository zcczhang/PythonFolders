"""
Fractal Tree
"""

import turtle


def draw_branch(branch_length):
    if branch_length > 5:
        # right branches
        turtle.fd(branch_length)
        turtle.rt(20)
        draw_branch(branch_length-15)

        # left branches
        turtle.lt(40)
        draw_branch(branch_length-15)

        # back to the origin
        turtle.rt(20)
        turtle.bk(branch_length)


def main():
    turtle.speed(0)
    turtle.lt(90)
    turtle.pu()
    turtle.bk(150)
    turtle.pd()
    turtle.color('brown')           # the direction is up

    draw_branch(100)

    turtle.exitonclick()


if __name__ == '__main__':
    main()




