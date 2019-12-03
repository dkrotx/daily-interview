class Node:
    def __init__(self, value = '^'):
        self.value = value
        self.childs = dict()
        self.ref_cnt = 1

    def subnode(self, c):
        if c in self.childs:
            self.childs[c].ref_cnt += 1
        else:
            self.childs[c] = Node()
   
        return self.childs[c]
        

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.subnode(c)

    def uniq_prefixes(self):
        prefixes = []

        def traverse(node, prefix=''):
            if node != self.root and node.ref_cnt == 1:
                prefixes.append(prefix)
                return

            for value, child in node.childs.items():
                traverse(child, prefix + value)

        traverse(self.root)
        return prefixes
            


def shortest_unique_prefix(words):
    tree = PrefixTree()
    for w in words:
        tree.insert(w)

    return tree.uniq_prefixes()
   

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
