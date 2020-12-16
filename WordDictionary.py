import collections
class TrieNode:
    def __init__(self):
        self.isWord = False
        # The main difference between defaultdict and dict is that when you try to access or modify a key 
        # that's not present in the dictionary, a default value is automatically given to that key
        self.children = collections.defaultdict(TrieNode)
        
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):

    def search(self, word):
    
    def dfs(self, node, word):