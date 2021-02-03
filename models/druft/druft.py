from anytree import Node, RenderTree
import pickle
import sys 
# import resource

class Tree:
    def __init__(self):
        self.root = Node('root')
    def add_sentence(self, node, sentence, source):
        if sentence == '\n' or sentence == '':
            leaf = Node("leaf", parent=node, src=source)
            return
        else:
            for child in node.children:
                if child.name == sentence[0]:
                    self.add_sentence(child, sentence[1:], source)
                    return
            new_Node = Node(sentence[0], parent=node)
            self.add_sentence(new_Node, sentence[1:], source)
    def find_best_match(self, node, sentence):
        ret = []
        if node.name == "leaf":
            ret.append(node.src)
            return  ret
        if sentence == "":
            return self.find_max_in_point(node, [])
        for child in node.children:
           if(len(ret)<5):
              if child.name == sentence[0]:
                ret += self.find_best_match(child, sentence[1:])
        if len(ret) <= 5:
            for child in node.children:
                if(len(ret)<5):
                  if child.name != sentence[0]:
                      ret += self.find_best_match(child, sentence[1:])
        return ret[:5]
    def find_max_in_point(self, node, lst=[]):
        for child in node.children:
            if child.name == "leaf":
                lst.append(child.src)
            else:
                lst+=(self.find_max_in_point(child, lst=[]))
        return lst
tree = Tree()

# tree.add_sentence(tree.root, "cool\n", ("cool", "cool.txt"))
# tree.add_sentence(tree.root, "hcat\n", ("hcat", "cat.txt"))
# tree.add_sentence(tree.root, "hello\n", ("hello", "hello.txt"))
# tree.add_sentence(tree.root, "hell\n", ("hell", "hell.txt"))
# tree.add_sentence(tree.root, "hell\n", ("hell", "hell.txt"))
# tree.add_sentence(tree.root, "hey\n", ("hey", "hey.txt"))
# tree.add_sentence(tree.root, "hop\n", ("hop", "hop.txt"))
# tree.add_sentence(tree.root, "hop\n", ("hop", "hop.txt"))

# for pre, fill, node in RenderTree(tree.root):
#     print("%s%s" % (pre, node.name))
# print(RenderTree(tree.root))
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


f=open("C:/Users/metzg/Documents/google_project/Aechive/0130903086.txt","r",encoding="utf-8")
lines =  f.readlines()
lines.sort()
for line in lines:
  tree.add_sentence(tree.root, line,(line,"0130903086"))
  for index in find(line, ' '):
    tree.add_sentence(tree.root, line[index+1:],(line,"0130903086"))
print(sys.getsizeof(tree))
max_rec = 0x100000

# May segfault without this line. 0x100 is a guess at the size of each stack frame.
# resource.setrlimit(resource.RLIMIT_STACK, [0x100 * max_rec, resource.RLIM_INFINITY])
sys.setrecursionlimit(max_rec)

with open('company_data.pkl', 'wb') as output:
    pickle.dump(tree, output, pickle.HIGHEST_PROTOCOL)

with open('company_data.pkl', 'rb') as input:
    tree1 = pickle.load(input)

print(tree1.find_best_match(tree1.root, "this"))