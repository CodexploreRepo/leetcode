class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        dest = {}
        for path in paths:
            if path[0] not in dest:
                dest[path[0]]=path[1]
        for path in paths:
            if path[1] not in dest:
                return path[1]
