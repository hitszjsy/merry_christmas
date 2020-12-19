
def sideflake(pen, length, n):
    if n == 1:
        pen.fd(length)
    if n > 1:
        length = length / 3
        sideflake(pen, length, n - 1)
        pen.left(60)
        sideflake(pen, length, n - 1)
        pen.right(120)
        sideflake(pen, length, n - 1)
        pen.left(60)
        sideflake(pen, length, n - 1)



