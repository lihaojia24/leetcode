class Solution:
    def entityParser(self, text: str) -> str:
        m = {
            '&quot;': '"',
            '&apos;': "'",
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
            '&amp;': '&',
        }
        i, n = 0, len(text)
        ans = []
        while i < n:
            isEntity = False
            if text[i] == '&':
                for k in m:
                    if i + len(k) - 1 < n and text[i:i+len(k)] == k:
                        ans.append(m[k])
                        i += len(k)
                        isEntity = True
                        break
            if not isEntity:
                ans.append(text[i])
                i += 1
        return ''.join(ans)

S = Solution() 
s = "&amp; is an HTML entity but &ambassador; is not."
print(S.entityParser(s))