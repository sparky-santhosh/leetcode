class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {')': '(', '}': '{', ']': '['}   
        for i in s:
            if i in d.values():
                l.append(i)
            elif i in d:
                if not l or l.pop() != d[i]:
                    return False   
        return not l