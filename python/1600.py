from collections import defaultdict
from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.childs = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.childs[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = list()
        def perOrder(name: str) -> None:
            if name not in self.dead:
                ans.append(name)
            for child in self.childs[name]:
                perOrder(child)
        perOrder(self.king)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()