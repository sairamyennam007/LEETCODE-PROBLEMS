class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr=path.split("/")
        if not path:
                return ""
        else:
            stk=[]
            for num in arr:
                if num =='.':
                    continue
                elif num=='..':
                    if stk:
                      stk.pop()
                      stk.pop()
                elif num=="":
                    continue
                else:
                    stk.append("/")
                    stk.append(num)
            if not stk:
                stk.append("/")
        return "".join(stk)
