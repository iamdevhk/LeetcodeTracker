class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        w=s.split(' ')
        st=[]
        for i in w:
            if i=='':
                continue
            else:
                st.insert(0,i)
        return (' '.join(st))