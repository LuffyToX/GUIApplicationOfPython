# -*- coding: utf-8 -*-
# 迷宫：递归、栈、队列


class Maze:
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 当前位置四个方向（东、西、南、北）的偏移量
    path = []                                  # 存储找到的路径


    def __init__(self, maze=None):
        self.maze = maze


    def mark(self, pos):
        """ 将搜索过的位置标记为 2 pos 是一个二元组 (i, j) """

        self.maze[pos[0]][pos[1]] = 2


    def passable(self, pos):
        """ 检查迷宫的位置是否可通行 pos 是一个二元组 (i, j) """

        # 0 代表可通行 || 1 代表不可通行
        return self.maze[pos[0]][pos[1]] == 0


    def findPathRecursion(self, start, end):
        """ 递归实现 """

        self.mark(start)

        # 已到达出口，将该位置加入 path
        if start == end:
            self.path.append(start)
            return True

        # 否则按四个方向顺序探查
        for i in range(4):
            nextp = start[0] + self.dirs[i][0], start[1] + self.dirs[i][1]
            # 考虑下一个可能方向，不可行的相邻位置不管
            if self.passable(nextp):
                # 如果从 nextp 可达出口，将该位置加入 path
                if self.findPathRecursion(nextp, end):
                    self.path.append(start)
                    return True
        return False


    def seePath(self, path):
        """ 可视化搜索路径 """

        for i, p in enumerate(path):
            if i == 0:
                self.maze[p[0]][p[1]] = "E"
            elif i == len(path) - 1:
                self.maze[p[0]][p[1]] = "S"
            else:
                self.maze[p[0]][p[1]] = 3
        print("\n")
        for r in self.maze:
            for c in r:
                if c == 3:
                    print('\033[0;31m' + "*" + " " + '\033[0m', end="")
                elif c == "S" or c == "E":
                    print('\033[0;34m' + c + " " + '\033[0m', end="")
                elif c == 2:
                    print('\033[0;32m' + "#" + " " + '\033[0m', end="")
                elif c == 1:
                    print('\033[0;;40m' + " " * 2 + '\033[0m', end="")
                else:
                    print(" " * 2, end="")
            print()


if __name__ == "__main__":
    mazeLst = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
               [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    mazeInstance = Maze(mazeLst)
    mazeInstance.findPathRecursion((1, 1), (10, 12))
    mazeInstance.seePath(mazeInstance.path)
