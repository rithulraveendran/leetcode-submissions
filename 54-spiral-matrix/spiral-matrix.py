class Solution:
    def spiralOrder(self, m: list[list[int]]) -> list[int]:
        a, b, c, d, r = 0, len(m) - 1, 0, len(m[0]) - 1, []
        while a <= b and c <= d:
            for j in range(c, d + 1): r.append(m[a][j])
            a += 1
            for i in range(a, b + 1): r.append(m[i][d])
            d -= 1
            if a <= b:
                for j in range(d, c - 1, -1): r.append(m[b][j])
                b -= 1
            if c <= d:
                for i in range(b, a - 1, -1): r.append(m[i][c])
                c += 1
        return r