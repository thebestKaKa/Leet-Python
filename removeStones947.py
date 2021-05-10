import collections


class Solution(object):
    # 并查集
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        edge = collections.defaultdict(list)

        for i, (xi, yi) in enumerate(stones):
            for j, (xj, yj) in enumerate(stones):
                if xi == xj or yi == yj:
                    edge[i].append(j)
        num = 0
        check = set()

        def 深度优先遍历(x: int):
            check.add(x)
            for temp1 in edge[x]:
                if temp1 not in check:
                    深度优先遍历(temp1)

        for i in range(n):
            if i not in check:
                深度优先遍历(i)
                num += 1
        return n - num


if __name__ == "__main__":
    s = Solution()
    stones = [[0, 1], [1, 0]]
    print(s.removeStones(stones))
