import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. Lowercase and extract only valid alphanumeric words
        # This completely fixes the punctuation and spacing issues
        l = re.findall(r'\w+', paragraph.lower())
        
        # 2. Build the frequency map
        d = dict()
        for i in l:
            d[i] = d.get(i, 0) + 1
        
        # 3. Safely remove the banned words
        for i in banned:
            d.pop(i, None)
            
        # 4. Return the key with the maximum value
        return max(d, key=d.get)