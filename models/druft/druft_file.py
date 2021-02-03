import  os
import pickle
from druft import  Tree,find
def insert_to_tree(f,filename,tree):
    lines =  f.readlines()
    lines.sort()
    for line in lines:
        tree.add_sentence(tree.root, line,(line,filename))
        for index in find(line, ' '):
            tree.add_sentence(tree.root, line[index+1:],(line,filename))

for root, dirs, files in os.walk('C:/Users/metzg/Documents/google_project/Aechive'):
    tree = Tree()
    for file in files:
        print(file)
        # with open(os.path.join(root, file), "r",encoding="utf-8") as f:
            # insert_to_tree(f,file,tree)
    # with open('company_data.pkl', 'wb') as output:
    #     pickle.dump(tree, output, pickle.HIGHEST_PROTOCOL)


