class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        files = path.split("/")
        for each in files:
            if each == "..":
                if stack:
                    stack.pop()
            elif each == "." or each == "":
                continue
            else:
                stack.append(each)
        return "/" + "/".join(stack)