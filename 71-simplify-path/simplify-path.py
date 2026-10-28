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
                if num =='.' or num=="":
                    continue
                elif num=='..':
                    if stk:
                      stk.pop()
                else:
                    stk.append(num)
        return "/"+"/".join(stk)
