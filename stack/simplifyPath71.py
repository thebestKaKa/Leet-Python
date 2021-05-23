# encoding:utf-8
# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），
# 请你将其转化为更加简洁的规范路径。
#
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；
# 两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
# 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
#
# 请注意，返回的 规范路径 必须遵循下述格式：
#
# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 返回简化后得到的 规范路径

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        ans = []
        count = 0  # 上级计数器
        for i in range(len(path)):
            stk.append(path[i])

        print(stk)
        while len(stk) > 0:
            if len(stk) >= 2 and stk[-1] + stk[-2] == "//":
                ans.append('/')
                stk.pop()
                stk.pop()
                continue
            if stk[-1] == '/':
                ans.append('/')
                stk.pop()
                continue
            if len(stk) >= 3 and stk[-3] + stk[-2] + stk[-1] == "...":
                pass
            elif len(stk) >= 3 and stk[-2] + stk[-1] == ".." and stk[-3] != "/":
                pass
            elif len(stk) >= 2 and stk[-1] == "." and stk[-2] != "/" and stk[-2] != ".":
                pass
            elif len(stk) >= 2 and stk[-1] + stk[-2] == "..":
                count += 1
                stk.pop()
                stk.pop()
                continue
            elif stk[-1] == '.':
                stk.pop()
                continue
            name = ""
            while stk[-1] != '/':
                name = stk.pop() + name
            if count > 0:
                count -= 1
                continue
            else:
                ans.append(name)
        ans = list(reversed(ans))
        res = "/"
        print(ans)
        for i in range(len(ans)):
            if ans[i] == '..':
                continue
            if ans[i] != '/':
                res = res + ans[i] + "/"
        if len(res) == 1:
            return res
        else:
            return res[0:-1]


if __name__ == "__main__":
    s = Solution()
    a = "/a/./b/../../c/"
    res = s.simplifyPath(a)
    print(res)
