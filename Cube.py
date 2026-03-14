class Cube:
    standard_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'w', 'x', 'y', 'z']

    standard_j = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'w', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'x', 'y', 'z']

    setup_l = {1: {1: []}, 2: {1: ['B', 'L'], 3: ['B\'', 'R\'']}, 3: {3: []},
               4: {1: ['D\'', 'L2', 'D'], 3: ['D', 'R2', 'D\'']}, 5: {1: ['L2'], 3: ['D2', 'R2']},
               6: {1: ['D', 'L2', 'D\''], 3: ['D\'', 'R2', 'D']}, 7: {1: ['D2', 'L2'], 3: ['R2']},
               8: {1: ['E\'', 'L\''], 3: ['R']}, 9: {1: ['L\''], 3: ['E', 'R']}, 10: {1: ['L'], 3: ['B2', 'R\'']},
               11: {1: ['B2', 'L'], 3: ['R\'']}}

    setup_j = {0: {0: []}, 1: {0: ['L'], 2: ['B\'']}, 2: {2: []}, 4: {0: ['L\''], 2: ['D2', 'B']},
               5: {0: ['L2'], 2: ['B2']},
               6: {0: ['D2', 'L\''], 2: ['B']}, 7: {0: ['D\'', 'L\''], 2: ['D', 'B']}}

    check_l = {'a': 'b', 'b': 'a', 'c': 'd', 'd': 'c', 'e': 'f', 'f': 'e', 'g': 'h', 'h': 'g', 'i': 'j', 'j': 'i',
               'k': 'l', 'l': 'k', 'm': 'n', 'n': 'm', 'o': 'p', 'p': 'o', 'q': 'r', 'r': 'q', 's': 't', 't': 's',
               'w': 'x', 'x': 'w', 'y': 'z', 'z': 'y'}

    check_j = {'a': 'bc', 'b': 'ca', 'c': 'ab', 'd': 'ef', 'e': 'fd', 'f': 'de', 'g': 'hi', 'h': 'ig', 'i': 'gh',
               'j': 'kl', 'k': 'lj', 'l': 'jk', 'w': 'mn', 'm': 'nw', 'n': 'wm', 'o': 'pq', 'p': 'qo', 'q': 'op',
               'r': 'st', 's': 'tr', 't': 'rs', 'x': 'yz', 'y': 'zx', 'z': 'xy'}

    forbidden_l = {1: ['L', 'U'], 2: ['B', 'U'], 3: ['R', 'U'], 4: ['D', 'U'], 5: ['L', 'D'], 6: ['B', 'D'],
                   7: ['D', 'R'], 8: ['E', 'R'], 9: ['E', 'L'], 10: ['L', 'B', 'E'], 11: ['R', 'B', 'E']}
    forbidden_j = {0: ['U', 'F', 'L'], 1: ['U', 'B', 'L'], 2: ['U', 'B', 'R'], 3: ['U', 'F', 'R'], 4: ['D', 'F', 'L'],
                   5: ['D', 'B', 'L'], 6: ['D', 'B', 'R'], 7: ['D', 'F', 'R']}

    formula_l = {0: {0: {0: ['R2', 'U', 'R', 'U', 'R\'', 'U\'', 'R\'', 'U\'', 'R\'', 'U', 'R\''],
                         1: ['R', 'U\'', 'R', 'U', 'R', 'U', 'R', 'U\'', 'R\'', 'U\'', 'R2']},
                     1: {0: ['U\'', 'R\'', 'U\'', 'R', 'U', 'M', 'U\'', 'R\'', 'U', 'M\'', 'R', 'U'],
                         1: ['U\'', 'M', 'R\'', 'U\'', 'R', 'U', 'M\'', 'U\'', 'R\'', 'U', 'R', 'U']}},
                 1: {0: {0: ['U\'', 'M\'', 'R', 'U', 'R\'', 'U\'', 'M', 'U', 'R', 'U\'', 'R\'', 'U'],
                         1: ['U\'', 'R', 'U', 'R\'', 'U\'', 'M\'', 'U', 'R', 'U\'', 'M', 'R\'', 'U']},
                     1: {0: ['M', 'U', 'M\'', 'U2', 'M', 'U', 'M\''],
                         1: ['M', 'U\'', 'M\'', 'U2', 'M', 'U\'', 'M\'']}}}

    formula_j = {0: {0: {0: ['R2', 'F2', 'R\'', 'B\'', 'R', 'F2', 'R\'', 'B', 'R\''],
                         1: ['R', 'B\'', 'R', 'F2', 'R\'', 'B', 'R', 'F2', 'R2']},
                     1: {0: ['R\'', 'U\'', 'D\'', 'R\'', 'D', 'R', 'U', 'R\'', 'D\'', 'R', 'D', 'R'],
                         1: ['R\'', 'D\'', 'R\'', 'D', 'R', 'U\'', 'R\'', 'D\'', 'R', 'D', 'U', 'R']},
                     2: {0: ['U\'', 'R\'', 'U2', 'R\'', 'D\'', 'R', 'U2', 'R\'', 'D', 'R2', 'U'],
                         1: ['U\'', 'R2', 'D\'', 'R', 'U2', 'R\'', 'D', 'R', 'U2', 'R', 'U']}},
                 1: {0: {0: ['R2', 'D', 'R\'', 'U2', 'R', 'D\'', 'R\'', 'U2', 'R\''],
                         1: ['R', 'U2', 'R', 'D', 'R\'', 'U2', 'R', 'D\'', 'R2']},
                     1: {0: ['R', 'U', 'D\'', 'R\'', 'D\'', 'R', 'U2', 'R\'', 'D', 'R', 'D', 'U', 'R\''],
                         1: ['R', 'U\'', 'D\'', 'R\'', 'D\'', 'R', 'U2', 'R\'', 'D', 'R', 'D', 'U\'', 'R\'']},
                     2: {0: ['R\'', 'U\'', 'R2', 'D\'', 'R2', 'D', 'R2', 'U', 'R2', 'D\'', 'R2', 'D', 'R\''],
                         1: ['R', 'D\'', 'R2', 'D', 'R2', 'U\'', 'R2', 'D\'', 'R2', 'D', 'R2', 'U', 'R']}},
                 2: {0: {0: ['R', 'B', 'R\'', 'F', 'R', 'B\'', 'R\'', 'F\''],
                         1: ['F', 'R', 'B', 'R\'', 'F\'', 'R', 'B\'', 'R\'']},
                     1: {0: ['R\'', 'U', 'L', 'U\'', 'R', 'U', 'L\'', 'U\''],
                         1: ['U', 'L', 'U\'', 'R\'', 'U', 'L\'', 'U\'', 'R']},
                     2: {0: ['F\'', 'U', 'R\'', 'D', 'R', 'U2', 'R\'', 'D\'', 'R', 'U', 'F'],
                         1: ['F\'', 'U\'', 'R\'', 'D', 'R', 'U2', 'R\'', 'D\'', 'R', 'U\'', 'F']}}}

    # 旋转操作会影响到的棱块，角块和中心块,以及变动的坐标
    # 9 = 10, 10 - -9
    influence = {'U': [0, 1, 2, 3, 0, 1, 2, 3, 0, 2, 0],
                 'D': [4, 5, 6, 7, 4, 5, 6, 7, 1, 0, 2],
                 'F': [0, 4, 8, 9, 0, 3, 7, 4, 2, 0, 1],
                 'B': [2, 6, 10, 11, 2, 1, 5, 6, 3, 1, 0],
                 'L': [1, 5, 9, 10, 1, 0, 4, 5, 4, 2, 1],
                 'R': [3, 7, 8, 11, 3, 2, 6, 7, 5, 1, 2],
                 'M': [0, 2, 4, 6, 0, 1, 2, 3, 1, 2],
                 'E': [8, 9, 10, 11, 2, 3, 4, 5, 2, 0],
                 'S': []}

    color_setup_l = [[], ['L\'', 'B\''], [], ['R', 'B'],
                     ['D2', 'B2'], ['D\'', 'B2'], ['B2'], ['D', 'B2'],
                     ['E', 'B'], ['E\'', 'B\''], ['B\''], ['B']]
    color_setup_j = [[], ['L'], ['B', 'L'], [], ['L\''], ['L2'], ['B2', 'L'], ['D\'', 'L\'']]

    color_formula_l = ['M\'', 'U', 'M\'', 'U', 'M\'', 'U2', 'M', 'U', 'M', 'U', 'M', 'U2']
    color_formula_j = [
        ['R', 'B', 'R\'', 'B\'', 'R', 'B', 'R\'', 'B\'', 'F', 'B', 'R', 'B\'', 'R\'', 'B', 'R', 'B\'', 'R\'', 'F\''],
        ['B', 'R', 'B\'', 'R\'', 'B', 'R', 'B\'', 'R\'', 'F', 'R', 'B', 'R\'', 'B\'', 'R', 'B', 'R\'', 'B\'', 'F\'']]

    @classmethod
    def hue_l(cls, letter):
        return cls.standard_l.index(letter) % 2

    @classmethod
    def hue_j(cls, letter):
        return cls.standard_j.index(letter) % 3

    @classmethod
    def index_l(cls, letter):
        return cls.standard_l.index(letter) // 2

    @classmethod
    def index_j(cls, letter):
        return cls.standard_j.index(letter) // 3

    def __init__(self):  # 初始化
        self.state_l = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i',
                        'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r',
                        's': 's', 't': 't', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
        self.state_j = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i',
                        'j': 'j', 'k': 'k', 'l': 'l', 'w': 'w', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q',
                        'r': 'r', 's': 's', 't': 't', 'x': 'x', 'y': 'y', 'z': 'z'}
        self.state_c = [0, 1, 2, 3, 4, 5]
        self.rd_l = []  # 完全复位的棱块
        self.rd_j = []  # 完全复位的角块
        self.rd_f_l = []  # 翻转复位的棱块
        self.rd_f_j = []  # 翻转复位的角块
        # 坐标，色相，颜色
        self.coord_l = \
            [[0, 1, 1, 0, 'u', 'f'], [-1, 1, 0, 0, 'u', 'l'], [0, 1, -1, 0, 'u', 'b'], [1, 1, 0, 0, 'u', 'r'],
             [0, -1, 1, 0, 'd', 'f'], [-1, -1, 0, 0, 'd', 'l'], [0, -1, -1, 0, 'd', 'b'], [1, -1, 0, 0, 'd', 'r'],
             [1, 0, 1, 0, 'f', 'r'], [-1, 0, 1, 0, 'f', 'l'], [-1, 0, -1, 0, 'b', 'l'], [1, 0, -1, 0, 'b', 'r']]
        # 根据色相确认循环顺序
        self.coord_j = \
            [[-1, 1, 1, 0, 'u', 'f', 'l'], [-1, 1, -1, 0, 'u', 'l', 'b'],
             [1, 1, -1, 0, 'u', 'b', 'r'], [1, 1, 1, 0, 'u', 'r', 'f'],
             [-1, -1, 1, 0, 'd', 'l', 'f'], [-1, -1, -1, 0, 'd', 'b', 'l'],
             [1, -1, -1, 0, 'd', 'r', 'b'], [1, -1, 1, 0, 'd', 'f', 'r']]
        self.coord_c = \
            [[0, 1, 0, 'u'], [0, -1, 0, 'd'], [0, 0, 1, 'f'],
             [0, 0, -1, 'b'], [-1, 0, 0, 'l'], [1, 0, 0, 'r']]
        self.keep_draw = True

    def print_state(self):  # 输出当前状态
        print("当前棱块状态：", end='')
        for value in self.state_l.values():
            print(value, end=" ")
        print("\n当前角块状态：", end='')
        for value in self.state_j.values():
            print(value, end=" ")
        print('')

    def input_state(self):  # 输入魔方状态
        i = 0

        print("输入棱信息：")
        leng = list(input())

        for key in self.state_l:  # 录入已有数据
            flag = i % 2
            if flag:
                i += 1
            else:
                self.state_l[key] = leng[i // 2]
                i += 1

        i = 0
        print("输入角信息：")
        j = list(input())

        for key in self.state_j:  # 录入已有数据
            flag = i % 3
            if flag:
                i += 1
            else:
                self.state_j[key] = j[i // 3]
                i += 1

        self.set_full()
        self.update_coord()
        self.update_rd()

    def set_full(self):  # 根据输入，补全魔方状态
        i = 0

        key_buf = None

        for key in self.state_l:
            flag = i % 2
            if flag:
                self.state_l[key] = Cube.check_l[key_buf]
                i += 1
            else:
                key_buf = self.state_l[key]
                i += 1
        i = 0
        for key in self.state_j:
            flag = i % 3
            if flag:
                self.state_j[key] = Cube.check_j[key_buf][flag - 1]
                i += 1
            else:
                key_buf = self.state_j[key]
                i += 1

    def update_rd(self):  # 更新归位块
        self.rd_l = []
        self.rd_f_l = []
        i = -1

        for key in self.state_l:
            i += 1
            if i % 2 == 0:
                if key == self.state_l[key]:  # 检查完全复位块
                    self.rd_l.append(Cube.index_l(key))
                elif Cube.index_l(self.state_l[key]) == Cube.index_l(key):
                    self.rd_f_l.append(Cube.index_l(key))

        self.rd_j = []
        self.rd_f_j = []
        i = -1

        for key in self.state_j:
            i += 1
            if i % 3 == 0:
                if key == self.state_j[key]:
                    self.rd_j.append(Cube.index_j(key))
                elif Cube.index_j(self.state_j[key]) == Cube.index_j(key):
                    self.rd_f_j.append(Cube.index_j(key))

    def update_coord(self):
        # 棱块坐标
        lst = [value for value in self.state_l.values()]
        for i in range(12):
            index = lst.index(Cube.standard_l[i * 2]) // 2
            x = int((index % 2) * ((1 - ((index + 1) / 2 % 2)) * 2 - 1) + (index // 8) * ((index + 1) % 2) * (
                    (1 - (index - 8) / 2) * 2 - 1))

            self.coord_l[i][0] = x
            self.coord_l[i][1] = int((index // 4 + 2) % 3 - 1)
            self.coord_l[i][2] = int((1 - ((index % 4) // 2)) * 2 - 1 + x + (index // 8) * -x)
            self.coord_l[i][3] = lst.index(Cube.standard_l[i * 2]) % 2

        # 角块坐标
        lst = [value for value in self.state_j.values()]
        for i in range(8):
            index = lst.index(Cube.standard_j[i * 3]) // 3
            self.coord_j[i][0] = int((index % 4 // 2) * 2 - 1)
            self.coord_j[i][1] = int(1 - (index // 4 * 2))
            self.coord_j[i][2] = int((index % 4 + 3) % 4 // 2 * 2 - 1)

            self.coord_j[i][3] = (3 - lst.index(Cube.standard_j[i * 3]) % 3) % 3

    def spin(self, op):
        # 等于1意味不逆向
        reversal = 1
        double = 0
        if len(op) == 2:
            if op[1] == '2':
                double = 1
            else:  # 任何其他字符都视为'
                reversal = -1
        elif len(op) == 1:
            op = op + '+'
        # 棱块
        first_coord = 9
        second_coord = 10
        if op[0] == 'M' or op[0] == 'E' or op[0] == 'S':
            first_coord = 8
            second_coord = 9
            if op[0] != 'S':
                reversal = -reversal
        state_l = dict(self.state_l)
        for i in range(4):
            index = Cube.influence[op[0]][i]
            actual_index = Cube.standard_l.index(self.state_l[Cube.standard_l[index * 2]]) // 2

            coord1 = self.coord_l[actual_index][Cube.influence[op[0]][first_coord]]
            coord2 = self.coord_l[actual_index][Cube.influence[op[0]][second_coord]]
            self.coord_l[actual_index][Cube.influence[op[0]][first_coord]] = reversal * coord2
            self.coord_l[actual_index][Cube.influence[op[0]][second_coord]] = -reversal * coord1
            if double:
                coord1 = self.coord_l[actual_index][Cube.influence[op[0]][first_coord]]
                coord2 = self.coord_l[actual_index][Cube.influence[op[0]][second_coord]]
                self.coord_l[actual_index][Cube.influence[op[0]][first_coord]] = reversal * coord2
                self.coord_l[actual_index][Cube.influence[op[0]][second_coord]] = -reversal * coord1

            if (op[0] == 'B' or op[0] == 'F' or op[0] == 'M' or op[0] == 'E' or op[0] == 'S') and (op[1] != '2'):
                self.coord_l[actual_index][3] = int(not self.coord_l[actual_index][3])

            x = self.coord_l[actual_index][0]
            y = self.coord_l[actual_index][1]
            z = self.coord_l[actual_index][2]
            target_index = int(abs(y) * (x - 2 * y - abs(z) - 5.5 + (x * z / 2)) + 9 - z + (1 - x * z) / 2)

            state_l[Cube.standard_l[target_index * 2]] = Cube.standard_l[
                actual_index * 2 + self.coord_l[actual_index][3]]

        self.state_l = dict(state_l)
        # print(self.coord_l[actual_index])

        # 角块
        state_j = dict(self.state_j)
        if op[0] != 'M' and op[0] != 'E' and op[0] != 'S':
            for i in range(4, 8):
                index = Cube.influence[op[0]][i]
                actual_index = Cube.standard_j.index(self.state_j[Cube.standard_j[index * 3]]) // 3

                coord1 = self.coord_j[actual_index][Cube.influence[op[0]][9]]
                coord2 = self.coord_j[actual_index][Cube.influence[op[0]][10]]
                self.coord_j[actual_index][Cube.influence[op[0]][9]] = reversal * coord2
                self.coord_j[actual_index][Cube.influence[op[0]][10]] = -reversal * coord1
                if double:
                    coord1 = self.coord_j[actual_index][Cube.influence[op[0]][9]]
                    coord2 = self.coord_j[actual_index][Cube.influence[op[0]][10]]
                    self.coord_j[actual_index][Cube.influence[op[0]][9]] = reversal * coord2
                    self.coord_j[actual_index][Cube.influence[op[0]][10]] = -reversal * coord1

                if (op[0] != 'U' and op[0] != 'D') and (op[1] != '2'):
                    self.coord_j[actual_index][3] = (self.coord_j[actual_index][3] + 2 - (i % 2)) % 3

                x = self.coord_j[actual_index][0]
                y = self.coord_j[actual_index][1]
                z = self.coord_j[actual_index][2]
                target_index = int(x - 2 * y + x * z / 2 + 3.5)

                state_j[Cube.standard_j[target_index * 3]] = Cube.standard_j[
                    actual_index * 3 + self.coord_j[actual_index][3]]

            self.state_j = dict(state_j)

        # 中心块
        state_c = list(self.state_c)
        if op[0] == 'M' or op[0] == 'E' or op[0] == 'S':

            for i in range(4, 8):
                index = Cube.influence[op[0]][i]
                actual_index = self.state_c[index]

                coord1 = self.coord_c[actual_index][Cube.influence[op[0]][8]]
                coord2 = self.coord_c[actual_index][Cube.influence[op[0]][9]]
                self.coord_c[actual_index][Cube.influence[op[0]][8]] = reversal * coord2
                self.coord_c[actual_index][Cube.influence[op[0]][9]] = -reversal * coord1
                if double:
                    coord1 = self.coord_c[actual_index][Cube.influence[op[0]][8]]
                    coord2 = self.coord_c[actual_index][Cube.influence[op[0]][9]]
                    self.coord_c[actual_index][Cube.influence[op[0]][8]] = reversal * coord2
                    self.coord_c[actual_index][Cube.influence[op[0]][9]] = -reversal * coord1

                x = self.coord_c[actual_index][0]
                y = self.coord_c[actual_index][1]
                z = self.coord_c[actual_index][2]

                target_index = int((y * y - y) / 2 + 2.5 * z * z - 0.5 * z + 4.5 * x * x + 0.5 * x)
                state_c[target_index] = actual_index

            self.state_c = list(state_c)

        self.set_full()
