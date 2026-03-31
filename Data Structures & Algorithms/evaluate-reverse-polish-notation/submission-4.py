class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        for t in tokens:
            print(q)
            if t not in "+-*/":
                q.append(int(t))
            else:
                a = q.pop()
                b = q.pop()
                if t == "+":
                    res = b + a
                elif t == "-":
                    res = b - a
                elif t == "*":
                    res = b * a
                else:
                    res = b / a
                q.append(int(res))

        return q[-1]

