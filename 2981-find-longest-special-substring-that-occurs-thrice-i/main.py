class Solution:
    def maximumLength(self, s: str) -> int:
        d = {chr(c): [0] for c in range(97, 97 + 26)}

        p = s[0]
        d[p][-1] += 1

        for c in list(s)[1:]:
            if c == p:
                d[c][-1] += 1
            else:
                d[c].append(1)
            p = c

        for c, l in d.items():
            if 0 in d[c]:
                d[c].remove(0)
            d[c] = sorted(d[c])

        maxN = -1

        for c, l in d.items():
            if len(l) == 0:
                continue

            m1 = l[-1] - 2
            m2 = m3 = 0

            if len(l) >= 2:
                m2 = min(l[-2], l[-1] - 1)

            if len(l) >= 3:
                m3 = l[-3]

            m = max(m1, m2, m3)

            if m > 0 and m > maxN:
                maxN = m

        return maxN
