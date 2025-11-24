class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        parents = collections.defaultdict(list)
        layer = {beginWord}
        found = False
        
        while layer and not found:
            next_layer = collections.defaultdict(list)
            wordSet -= layer
            
            for word in layer:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]: continue
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in wordSet:
                            if new_word == endWord:
                                found = True
                            parents[new_word].append(word)
                            next_layer[new_word].append(word)
            
            layer = set(next_layer.keys())

        if not found:
            return []
            
        res = []
        def dfs(node, path):
            if node == beginWord:
                res.append(path[::-1])
                return
            
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        dfs(endWord, [endWord])
        return res