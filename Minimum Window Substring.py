class Solution:

    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        if len(t) > len(s):
            return ""
        counts = dict()
        positive_count = 0
        for c in t:
            was = counts.get(c, 0)
            if was == 0:
                positive_count += 1
            counts[c] = was + 1
        a = 0
        b = -1
        min_a = None
        min_b = None
        while True:
            if positive_count <= 0:
                while True:
                    if min_a is None or b - a < min_b - min_a:
                        min_a = a
                        min_b = b
                    prev_a = s[a]
                    was = counts.get(prev_a, 0)
                    counts[prev_a] = was + 1
                    if was == 0:
                        positive_count += 1  
                    a += 1
                    if a > b:
                        break
                    if positive_count > 0:
                        break
            b += 1
            if b >= len_s:
                break
            next_b = s[b]
            was = counts.get(next_b, 0) 
            counts[next_b] = was - 1
            if was == 1:
                positive_count -= 1
        return "" if min_a is None else s[min_a:min_b+1]