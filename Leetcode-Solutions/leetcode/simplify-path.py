class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for dir in path:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir == "." or dir == "":
                continue
            else:
                stack.append(dir)
        # print(path)
        # stack.pop()
        return "/" + "/".join(stack)
            
            
                