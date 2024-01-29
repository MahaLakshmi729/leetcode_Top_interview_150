class Solution:
    def reverseWords(self, s: str) -> str:
        i, j = 0, len(s) - 1
        while i <= j and s[i] == ' ':
            i += 1  
        while j >= i and s[j] == ' ':
            j -= 1  
        s = s[i : j + 1] 
        words = s.split()

        out = []
        for k in range(len(words) - 1, 0, -1):

            out.append(words[k])
        
        out.append(words[0])

        return ' '.join(out)  