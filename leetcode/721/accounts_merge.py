class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts: return []
        graph = collections.defaultdict(set)
        email2name = {}
        for account in accounts:
            if len(account) >= 2:
                name, emails = account[0], account[1:]
                if len(emails) == 1: 
                    graph[emails[0]].add(emails[0])
                    email2name[emails[0]] = name
                for i in range(len(emails) - 1):         
                    graph[emails[i]].add(emails[i + 1])
                    graph[emails[i + 1]].add(emails[i])
                    email2name[emails[i]] = name
                    email2name[emails[i + 1]] = name
                    
        def dfs(e, path, visited):
            visited.add(e)
            path.add(e)
            for nei in graph[e]:
                if nei in visited: continue
                dfs(nei, path, visited)
        
        # print(graph)
        res = []
        seen = set()
        for email in graph:
            if email in seen: continue
            path = set()
            dfs(email, path, set())
            seen |= path
            res.append([email2name[list(path)[0]] ] + sorted(list(path)) )
        return res  
