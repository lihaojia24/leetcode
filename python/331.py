class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        st = []
        for node in preorder.split(","):
            st.append(node)
            while len(st) > 2 and st[-1] == st[-2] == '#' and st[-3] != '#':
                st.pop()
                st.pop()
                st.pop()
                st.append('#')
        return len(st) == 1 and st[0] == '#'