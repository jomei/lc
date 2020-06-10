class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        close = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in close:
                if len(st) == 0:
                    return False
                if st.pop() != close[c]:
                    return False
            else:
                st.append(c)
        return st == []