from pprint import pprint as print 

class Trie:

    def __init__(self):
        self.root = [True, dict()]

    def insert(self, word: str) -> None:
        nowd = self.root[1]
        for idx, s in enumerate(word):
            if idx != len(word)-1:
                if s not in nowd:
                    nowd[s] = [False, dict()]
                nowd = nowd[s][1]
            else:
                if s not in nowd:
                    nowd[s] = [True, dict()]
                else:
                    nowd[s][0] = True
    
    
    def search(self, word: str) -> bool:
        nowd = self.root[1]
        for idx, s in enumerate(word):
            if s not in nowd:
                return False
            if idx == len(word)-1:
                return nowd[s][0]
            nowd = nowd[s][1]
        return False
            

    def startsWith(self, prefix: str) -> bool:
        nowd = self.root[1]
        for s in prefix:
            if s not in nowd:
                return False
            nowd = nowd[s][1]
        return True
        
        
    
if __name__ == "__main__":
    t = Trie()
    t.insert("aaaa")
    print(t.root)
    
    print(t.search("aaaaaaa"))
    print(t.startsWith("ab"))
    
