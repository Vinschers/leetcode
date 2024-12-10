class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        delta_indices = list(range(len(spaces)))
        idx = [0] * len(spaces)
        for i in range(len(spaces)):
            idx[i] = spaces[i] + delta_indices[i]

        idx = set(idx)
        ss = [" "] * (len(s) + len(spaces))
        ls = list(s)
        i = 0
        j = 0

        while j < len(ls):
            if i not in idx:
                ss[i] = ls[j]
                j += 1
            i += 1

        return "".join(ss)
