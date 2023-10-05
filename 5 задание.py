import turtle as t

def koch_curve(size, n):
    if n == 0:
        t.fd(size)
    else:
        koch_curve(size / 3, n - 1)
        t.lt(60)
        koch_curve(size / 3, n - 1)
        t.rt(120)
        koch_curve(size / 3, n - 1)
        t.lt(60)
        koch_curve(size / 3, n - 1)

def draw_koch_showflake(size, n):
        for i in range (3):
            koch_curve (size, n)
            t.rt(120)

n = 3
size = 100
draw_koch_showflake(size, n)
