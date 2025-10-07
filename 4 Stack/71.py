class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_items = path.split("/")

        for item in path_items:
            if item == "." or not item:
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)

print(Solution().simplifyPath("/a/./b/../../c/"))  # Output: "/c"
print(Solution().simplifyPath("/../"))  # Output: "/"
print(Solution().simplifyPath("/home//foo/"))  # Output: "/home/foo"
