import time

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
import os
import threading
import solvecube

# 魔方的每个面的颜色
# 上黄下白，左橙右红，前蓝后绿
colors = {
    "u": (1, 1, 0),  # 黄色
    "d": (1, 1, 1),  # 白色
    "l": (1, 0.5, 0),  # 橙色
    "r": (1, 0, 0),  # 红色
    "f": (0, 0, 1),  # 蓝色
    "b": (0, 1, 0),  # 绿色
    "i": (0, 0, 0)  # 内部面黑色
}

vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

# 每个面的顶点，按立方体6个面的顺序
surfaces = [
    [0, 3, 7, 4],  # 上面 (Up)
    [1, 2, 6, 5],  # 下面 (Down)
    [4, 5, 6, 7],  # 前面 (Front)
    [0, 1, 2, 3],  # 后面 (Back)
    [2, 3, 7, 6],  # 左面 (Left)
    [0, 1, 5, 4]  # 右面 (Right)
]

spinning = False
op_index = 0
op = []


def draw_cube_l(index, cube):
    glBegin(GL_QUADS)

    # 绘制每个面并设定对应颜色
    color_sort = []
    if cube.coord_l[index][3]:
        color_sort = cube.coord_l[index][5:3:-1]
    else:
        color_sort = cube.coord_l[index][4:6:1]

    position_sort = []
    if cube.coord_l[index][1] == 1:
        position_sort.append(0)
    elif cube.coord_l[index][1] == -1:
        position_sort.append(1)

    if cube.coord_l[index][2] == 1:
        position_sort.append(2)
    elif cube.coord_l[index][2] == -1:
        position_sort.append(3)

    if cube.coord_l[index][0] == -1:
        position_sort.append(4)
    elif cube.coord_l[index][0] == 1:
        position_sort.append(5)

    for i in range(6):
        if i not in position_sort:
            position_sort.append(i)

    for i in range(2):
        glColor3fv(colors[color_sort[i]])
        for vertex in surfaces[position_sort[i]]:
            glVertex3fv(vertices[vertex])

    glColor3fv(colors['i'])

    for i in range(2, 6):
        for vertex in surfaces[position_sort[i]]:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_cube_j(index, cube):
    glBegin(GL_QUADS)

    # 绘制每个面并设定对应颜色
    color_sort = []
    if cube.coord_j[index][3] == 0:
        color_sort = cube.coord_j[index][4:7:1]
    elif cube.coord_j[index][3] == 1:
        color_sort = cube.coord_j[index][5:7:1]
        color_sort.append(cube.coord_j[index][4])
    else:
        color_sort.append(cube.coord_j[index][6])
        color_sort.append(cube.coord_j[index][4])
        color_sort.append(cube.coord_j[index][5])

    position_sort = []
    if cube.coord_j[index][1] == 1:
        position_sort.append(0)
    elif cube.coord_j[index][1] == -1:
        position_sort.append(1)

    if cube.coord_j[index][2] == 1:
        position_sort.append(2)
    elif cube.coord_j[index][2] == -1:
        position_sort.append(3)

    if cube.coord_j[index][0] == -1:
        position_sort.append(4)
    elif cube.coord_j[index][0] == 1:
        position_sort.append(5)

    for i in range(6):
        if i not in position_sort:
            position_sort.append(i)

    if cube.coord_j[index][0] * cube.coord_j[index][1] * cube.coord_j[index][2] == 1:
        position_sort[1], position_sort[2] = position_sort[2], position_sort[1]

    for i in range(3):
        glColor3fv(colors[color_sort[i]])
        for vertex in surfaces[position_sort[i]]:
            glVertex3fv(vertices[vertex])

    glColor3fv(colors['i'])

    for i in range(3, 6):
        for vertex in surfaces[position_sort[i]]:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_cube_c(index, cube):
    glBegin(GL_QUADS)
    glColor3fv(colors[cube.coord_c[index][3]])
    for vertex in surfaces[cube.state_c.index(index)]:
        glVertex3fv(vertices[vertex])

    glColor3fv(colors['i'])
    for i in range(6):
        if i == cube.state_c.index(index):
            continue
        for vertex in surfaces[i]:
            glVertex3fv(vertices[vertex])

    glEnd()


# 绘制三阶魔方
def draw_rubiks_cube(cube):
    # 棱
    for i in range(0, 12):
        glPushMatrix()
        glTranslatef(cube.coord_l[i][0] * 2.04, cube.coord_l[i][1] * 2.04, cube.coord_l[i][2] * 2.04)  # 减小每个立方体的间隙
        draw_cube_l(i, cube)
        glPopMatrix()
    # 角
    for i in range(8):
        glPushMatrix()
        glTranslatef(cube.coord_j[i][0] * 2.04, cube.coord_j[i][1] * 2.04, cube.coord_j[i][2] * 2.04)  # 减小每个立方体的间隙
        draw_cube_j(i, cube)
        glPopMatrix()

    # 中心
    for i in range(6):
        glPushMatrix()
        glTranslatef(cube.coord_c[i][0] * 2.04, cube.coord_c[i][1] * 2.04, cube.coord_c[i][2] * 2.04)
        draw_cube_c(i, cube)
        glPopMatrix()


# 初始化 OpenGL 和 pygame
def draw(cube):
    global spinning
    degree = 0
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # 启用深度测试，避免看到内部面
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glClearColor(0.9, 0.9, 1, 0.5)
    # 设置投影矩阵
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -16)  # 调整摄像机位置

    rotation_x, rotation_y = 0, 0
    mouse_down = False

    # 主循环
    while cube.keep_draw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # 鼠标事件处理
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键按下
                    mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # 左键松开
                    mouse_down = False
            if event.type == pygame.MOUSEMOTION and mouse_down:
                if (-90 < rotation_x or event.rel[1] >= 0) and (rotation_x < 90 or event.rel[1] <= 0):
                    rotation_x += event.rel[1]
                rotation_y += event.rel[0]

        # 清空屏幕并清空深度缓冲区
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # 应用旋转
        glPushMatrix()
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        # 绘制三阶魔方
        draw_rubiks_cube(cube)
        if spinning:
            degree += 10
            if degree >= 90:
                degree = 0
                spinning = False
                recover(cube)
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(8)


def recover(cube):
    global spinning
    global op_index
    if op_index < len(op):
        if spinning == 0:
            if op[op_index] == '||':
                op_index += 1
                print('')
            elif op[op_index] == '|||':
                op_index += 1

            else:
                print(op[op_index], end=' ')
                cube.spin(op[op_index])
                op_index += 1
            spinning = 1


def main_function(cube):
    global op_index
    global op
    index = 1
    while index:
        os.system('cls')
        print('*******菜单******')
        print('0.退出')
        print('1.解魔方')
        print('2.自由操作')
        print('请选择：', end=' ')
        choose = input()
        if len(choose) == 0:
            continue
        index = int(choose)
        if index == 0:
            cube.keep_draw = False
            break
        elif index == 1:
            os.system('cls')
            print('当前模式：解魔方')
            print('0.退出')
            print('1.使用已有状态')
            print('2.输入新状态')
            print('请选择：', end=' ')
            index = int(input())
            if index == 0:
                continue
            elif index == 1:
                cube.print_state()
                op = solvecube.solvecube(cube)
                op_index = 0
                os.system('pause')
                recover(cube)
                while op_index < len(op) - 1:
                    time.sleep(0.5)
            elif index == 2:
                cube.input_state()
                cube.print_state()
                op = solvecube.solvecube(cube)
                op_index = 0
                os.system('pause')
                recover(cube)
                while op_index < len(op) - 1:
                    time.sleep(0.5)
            else:
                print('无效操作')
                os.system('pause')
                continue
        elif index == 2:
            op_lst = []
            while index:
                os.system('cls')
                print('当前模式：自由操作(EXIT退出)')
                print('当前操作:', end=' ')
                for opt in op_lst:
                    print(opt, end=' ')
                print('\n请输入操作：')
                opt = input()
                if len(opt) == 0:
                    continue
                if opt == 'exit' or opt == 'EXIT':
                    os.system('pause')
                    break
                elif opt[0] in Cube.influence and len(opt) <= 2:
                    op_lst.append(opt)
                    cube.spin(opt)

                else:
                    print('无效操作')
                    time.sleep(1.5)
            cube.update_rd()
        else:
            print('无效操作')
            time.sleep(0.8)

if __name__ == "__main__":
    cube = Cube()

    thread_1 = threading.Thread(target=draw, args=(cube,))
    thread_2 = threading.Thread(target=main_function, args=(cube,))

    thread_2.start()
    thread_1.start()

    thread_1.join()
    thread_2.join()
