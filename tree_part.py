
def draw_tree_part(pen, pen2, x, y, num): # num 画的数次
    pen.goto(x, y)
    for i in range(4):
        k = num-1+i # k represent 一侧方块数
        pen.goto(x, y-i*30)
        pen.stamp() # 画中间
        for j in range(k):
            pen.goto(x-30*(j+1), y-i*30)
            pen.stamp()
            pen.goto(x+30*(j+1), y-i*30)
            pen.stamp() # 将两侧分别画好

    pen2.goto(x - (num + 2) * 30, y - 60)
    pen2.color('yellow')
    pen2.stamp()
    pen2.goto(x + (num + 2) * 30, y - 60)
    pen2.color('yellow')
    pen2.stamp()
    pen2.goto(x - (num + 3) * 30, y - 90)
    pen2.color('red')
    pen2.stamp()
    pen2.goto(x + (num + 3) * 30, y - 90)
    pen2.color('red')
    pen2.stamp()

