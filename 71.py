class Solution:
  def simplifyPath(self, path: str) -> str:
    path = path.split('/')
    res = []
    for item in path:
      if item == '' or item == '.':
        continue
      elif item == '..':
        if len(res) > 0:
          res.pop()
      else:
        res.append(item)
    return '/' + '/'.join(res)

solu = Solution()  
path = "/home/"
print(solu.simplifyPath(path))
