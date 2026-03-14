from Cube import Cube


def solvecube(cube):
    cube.update_rd()
    print('已复位棱块:', cube.rd_l, '已复位角块:', cube.rd_j, '需翻转棱块:', cube.rd_f_l, '需翻转角块:', cube.rd_f_j)
    predict_code_length_l = 12 - len(cube.rd_l) - len(cube.rd_f_l) - 1
    predict_code_length_j = 8 - len(cube.rd_j) - len(cube.rd_f_j) - 1
    if 0 in cube.rd_l or 0 in cube.rd_f_l:
        predict_code_length_l += 1
    if 3 in cube.rd_j or 3 in cube.rd_f_j:
        predict_code_length_j += 1
    code_l = []
    coded_l = []
    code_j = []
    coded_j = []

    # 棱块编码
    cur_loop = -1  # 记录当前所在小循环

    if Cube.index_l(cube.state_l['a']) != 0:  # 正常编码
        code_l.append(cube.state_l['a'])
        coded_l.append(Cube.index_l(cube.state_l['a']))

    else:  # 小循环
        for key in Cube.check_l:  # 寻找未编码块
            if key == 'a' or key == 'b':  # 跳过缓冲块
                continue
            cur_pos = Cube.index_l(key)
            if cur_pos not in cube.rd_l and cur_pos not in cube.rd_f_l:  # 跳过已归位的块
                code_l.append(key)
                coded_l.append(Cube.index_l(key))
                cur_loop = Cube.index_l(key)
                predict_code_length_l += 1  # 小循环导致编码长度加1
                break

    while predict_code_length_l - len(code_l) > 0:
        cur_pos = Cube.index_l(cube.state_l[code_l[-1]])  # 记录当前位置（简化代码）
        if cur_pos != 0 and cur_pos != cur_loop:  # 当小循环开始或结束时，需要寻找新的未编码方块
            code_l.append(cube.state_l[code_l[-1]])
            coded_l.append(cur_pos)

        else:  # 小循环
            if cur_pos == cur_loop:
                code_l.append(cube.state_l[code_l[-1]])  # 小循环结束位置
                coded_l.append(cur_pos)

            for key in Cube.check_l:
                if key == 'a' or key == 'b':  # 跳过缓冲块
                    continue
                cur_pos = Cube.index_l(key)
                if cur_pos not in coded_l and cur_pos not in cube.rd_l and cur_pos not in cube.rd_f_l:  # 跳过所有已编码块和已归位块
                    code_l.append(key)
                    coded_l.append(cur_pos)
                    cur_loop = cur_pos
                    predict_code_length_l += 1  # 小循环导致编码长度加1
                    break

    # 角块编码
    cur_loop = -1  # 记录当前所在小循环

    if Cube.index_j(cube.state_j['j']) != 3:  # 正常编码
        code_j.append(cube.state_j['j'])
        coded_j.append(Cube.index_j(cube.state_j['j']))

    else:  # 小循环
        for key in Cube.check_j:  # 寻找未编码块
            if key == 'j' or key == 'k' or key == 'l':  # 跳过缓冲块
                continue
            cur_pos = Cube.index_j(key)  # 记录当前位置（简化代码）
            if cur_pos not in cube.rd_j and cur_pos not in cube.rd_f_j:  # 跳过已归位的块
                code_j.append(key)
                coded_j.append(Cube.index_j(key))
                cur_loop = Cube.index_j(key)
                predict_code_length_j += 1  # 小循环导致编码长度加1
                break

    while predict_code_length_j - len(code_j) > 0:
        cur_pos = Cube.index_j(cube.state_j[code_j[-1]])
        if cur_pos != 3 and cur_pos != cur_loop:  # 当小循环开始或结束时，需要寻找新的未编码方块
            code_j.append(cube.state_j[code_j[-1]])
            coded_j.append(cur_pos)

        else:  # 小循环
            if cur_pos == cur_loop:
                code_j.append(cube.state_j[code_j[-1]])  # 小循环结束位置
                coded_j.append(cur_pos)

            for key in Cube.check_j:
                if key == 'j' or key == 'k' or key == 'l':  # 跳过缓冲块
                    continue
                cur_pos = Cube.index_j(key)
                if cur_pos not in coded_j and cur_pos not in cube.rd_j and cur_pos not in cube.rd_f_j:  # 跳过所有已编码块和已归位块
                    code_j.append(key)
                    coded_j.append(cur_pos)
                    cur_loop = cur_pos
                    predict_code_length_j += 1  # 小循环导致编码长度加1
                    break

    odd_even_check = 0
    # 奇偶校验
    special_j = 0
    if len(code_l) % 2 == 1:
        odd_even_check = 1
        if Cube.index_l(code_l[-1]) == 3:
            if code_l[-1] == 'h':
                cube.rd_f_l.append(3)
            code_l.pop()

        else:
            code_l.append('g')

        if Cube.index_j(code_j[-1]) == 2:
            special_j = Cube.hue_j(code_j[-1])
            code_j.pop()
        else:
            code_j.append('g')
    print('odd_even_check = ', odd_even_check)
    print("棱块编码：", code_l)
    print("角块编码：", code_j)

    # 开始复原
    stack = []
    # 棱块复原
    op_l = []
    recovered = 0
    while recovered < len(code_l):

        cur_two = [code_l[recovered], code_l[recovered + 1]]
        recovered += 2
        cur_t_pos = [Cube.index_l(cur_two[0]), Cube.index_l(cur_two[1])]
        cur_hue = [Cube.hue_l(cur_two[0]), Cube.hue_l(cur_two[1])]
        allowed_pos = [[1, 1], [1, 1]]

        # 判断禁用操作
        for j in range(2):  # 当前块
            # 若为CG块
            if cur_t_pos[j] == 1:
                allowed_pos[j][1] = 0
                allowed_pos[1 - j][0] = 0
                break

            if cur_t_pos[j] == 3:
                allowed_pos[j][0] = 0
                allowed_pos[1 - j][1] = 0
                break

            for i in range(2):  # 要去的块
                for step in Cube.setup_l[cur_t_pos[j]][2 * i + 1]:
                    if step[0] in Cube.forbidden_l[cur_t_pos[1 - j]]:
                        allowed_pos[j][i] = 0

        # setup判断
        i = -1
        j = -1
        flag = 0
        for lst in allowed_pos:
            i += 1
            j = -1
            for a in lst:
                j += 1
                if a == 1:
                    flag = 1
                    break
            if flag:
                break

        # 部分setup公式导致的色相变化
        for l in range(2):
            if cur_t_pos[l] == 2:
                cur_hue[l] = 1 - cur_hue[l]
        for l in range(2):
            if cur_t_pos[l] == 8 and i ^ j ^ l == 0:
                cur_hue[l] = 1 - cur_hue[l]

        for l in range(2):
            if cur_t_pos[l] == 9 and (i ^ j ^ l):
                cur_hue[l] = (not cur_hue[l]) + 0

        # setup是否导致顺序颠倒
        if i ^ j:
            cur_hue.reverse()

        # 进行setup
        for element in Cube.setup_l[cur_t_pos[i]][2 * j + 1]:
            op_l.append(element)
            stack.append(element)
        for element in Cube.setup_l[cur_t_pos[1 - i]][2 * (2 - j) - 1]:
            op_l.append(element)
            stack.append(element)

        # 判断需使用的公式：
        for element in Cube.formula_l[cur_hue[0]][cur_hue[1]][i ^ j]:
            op_l.append(element)

        # reverse
        while stack:
            temp = stack.pop()
            if len(temp) == 2:
                if temp[1] == '\'':
                    temp = temp[0]
            else:
                temp = temp + '\''
            op_l.append(temp)
        op_l.append('||')

    print('棱块复原操作：', end=' ')
    for element in op_l:
        print(element, end=' ')
    print('')

    # 角块复原
    op_j = []
    recovered = 0
    while recovered < len(code_j):
        cur_two = [code_j[recovered], code_j[recovered + 1]]
        recovered += 2
        cur_t_pos = [Cube.index_j(cur_two[0]), Cube.index_j(cur_two[1])]
        cur_hue = [Cube.hue_j(cur_two[0]), Cube.hue_j(cur_two[1])]
        allowed_pos = [[1, 1], [1, 1]]

        # 判断禁用操作
        for j in range(2):  # 当前块
            # 若为0号块
            if cur_t_pos[j] == 0:
                allowed_pos[j][1] = 0
                allowed_pos[1 - j][0] = 0
                break
            # 若为2号块
            if cur_t_pos[j] == 2:
                allowed_pos[j][0] = 0
                allowed_pos[1 - j][1] = 0
                break

            for i in range(2):  # 要去的块
                for step in Cube.setup_j[cur_t_pos[j]][2 * i]:
                    if step[0] in Cube.forbidden_j[cur_t_pos[1 - j]]:
                        allowed_pos[j][i] = 0

        # setup判断
        i = -1
        j = -1
        flag = 0
        for lst in allowed_pos:
            i += 1
            j = -1
            for a in lst:
                j += 1
                if a == 1:
                    flag = 1
                    break
            if flag:
                break

        # 部分setup公式导致的色相变化
        # i^j^l 代表当前块使用的setup公式序号
        if (cur_t_pos[0] != 1 or cur_t_pos[1] != 5) and (cur_t_pos[0] != 5 or cur_t_pos[1] != 1):
            for l in range(2):
                if cur_t_pos[l] == 4:
                    cur_hue[l] = (cur_hue[l] + 1) % 3
                if cur_t_pos[l] == 1 or cur_t_pos[l] == 6 or cur_t_pos[l] == 7:
                    if i ^ j ^ l:
                        cur_hue[l] = (cur_hue[l] + 2) % 3
                    else:
                        cur_hue[l] = (cur_hue[l] + 1) % 3

            # setup是否导致顺序颠倒
            if i ^ j:
                cur_hue.reverse()

            # 进行setup
            for element in Cube.setup_j[cur_t_pos[i]][2 * j]:
                op_j.append(element)
                stack.append(element)
            for element in Cube.setup_j[cur_t_pos[1 - i]][2 * (1 - j)]:
                op_j.append(element)
                stack.append(element)

            # 判断需使用的公式：
            for element in Cube.formula_j[cur_hue[0]][cur_hue[1]][i ^ j]:
                op_j.append(element)

            # reverse
            while stack:
                temp = stack.pop()
                if len(temp) == 2:
                    if temp[1] == '\'':
                        temp = temp[0]
                else:
                    temp = temp + '\''
                op_j.append(temp)
            op_j.append('||')
        else:
            op_j.append('L')
            op_j.append('B\'')
            stack.append('L')
            stack.append('B\'')
            cur_hue[0] = (cur_hue[0] + 1) % 3
            cur_hue[1] = (cur_hue[1] + 4) % 3
            re = 0
            if cur_t_pos[0] == 5:
                re = 1
                cur_hue = cur_hue.reverse()
            for element in Cube.formula_j[cur_hue[0]][cur_hue[1]][re]:
                op_j.append(element)
            while stack:
                temp = stack.pop()
                if len(temp) == 2:
                    if temp[1] == '\'':
                        temp = temp[0]
                else:
                    temp = temp + '\''
                op_j.append(temp)
            op_j.append('||')

    print('角块复原操作：', end=' ')
    for element in op_j:
        print(element, end=' ')
    print('')

    LP = []
    if odd_even_check:
        print('奇偶校验', end='')
        LP = ['R', 'U', 'R\'', 'F\'', 'R', 'U', 'R\'', 'U\'', 'R\'', 'F', 'R2', 'U\'', 'R\'', 'U\'', '||']
        for element in LP:
            print(element, end=' ')
        print('')

    # 棱块翻色
    color_turning_l = []
    while cube.rd_f_l:
        block = cube.rd_f_l.pop()

        if block == 0:
            continue
        # setup
        for op in Cube.color_setup_l[block]:
            color_turning_l.append(op)
            stack.append(op)

        # 翻色
        for opt in Cube.color_formula_l:
            color_turning_l.append(opt)

        # reverse
        while stack:
            temp = stack.pop()
            if len(temp) == 2:
                if temp[1] == '\'':
                    temp = temp[0]
            else:
                temp = temp + '\''
            color_turning_l.append(temp)
        color_turning_l.append('||')

    print('棱块翻色操作：', end=' ')
    for element in color_turning_l:
        print(element, end=' ')
    print('')

    # 角块翻色
    color_turning_j = []
    while cube.rd_f_j:

        block = cube.rd_f_j.pop()

        if block == 3:
            continue
        # setup
        for op in Cube.color_setup_j[int(block)]:
            color_turning_j.append(op)
            stack.append(op)

        # 翻色
        hue = Cube.hue_j(cube.state_j[Cube.standard_j[block * 3]])
        for opt in Cube.color_formula_j[2- hue]:
            color_turning_j.append(opt)

        # reverse
        while stack:
            temp = stack.pop()
            if len(temp) == 2:
                if temp[1] == '\'':
                    temp = temp[0]
            else:
                temp = temp + '\''
            color_turning_j.append(temp)
        color_turning_j.append('||')

    if special_j:
        for opt in Cube.color_setup_j[2]:
            color_turning_j.append(opt)
        for opt in Cube.color_formula_j[2 - special_j]:
            color_turning_j.append(opt)
        color_turning_j.append('L\'')
        color_turning_j.append('B\'')

    print('角块翻色操作：', end=' ')
    for element in color_turning_j:
        print(element, end=' ')
    print('')

    return op_l + op_j + LP + color_turning_l + color_turning_j


if __name__ == "__main__":
    cube = Cube()
    cube.input_state()
    cube.print_state()
    cube.update_rd()
    solvecube(cube)
