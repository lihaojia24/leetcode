from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        resTmp = [[]]
        resTmpWidth = []
        tmpWidth = 0
        flag = " "
        for word in words:
            if tmpWidth != 0:
                tmpWidth += 1
            tmpWidth += len(word)
            if tmpWidth > maxWidth:
                resTmpWidth.append(tmpWidth - len(word) - len(resTmp[-1]))
                resTmp.append([word])
                tmpWidth = len(word)
            else:
                resTmp[-1].append(word)

        for resLine, lineWidth in zip(resTmp[:-1], resTmpWidth):
            # print(resLine, lineWidth)
            gapTotal = maxWidth - lineWidth
            if len(resLine) == 1:
                tmp = resLine[0]
                tmp += flag * (maxWidth - len(tmp))
                res.append(tmp)
            else:
                gap = gapTotal // (len(resLine) - 1)
                gapPlus = gapTotal % (len(resLine) - 1)
                blanks = flag * (gap+1)
                tmp = blanks.join(resLine[:gapPlus+1])
                blanks = flag * gap
                tmp2 = blanks.join(resLine[gapPlus+1:])
                res.append(blanks.join([tmp, tmp2]))
        tmp =  flag.join(resTmp[-1])
        tmp += flag * (maxWidth - len(tmp))
        res.append(tmp)

        return res

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
solu = Solution()
print(solu.fullJustify(words, maxWidth))