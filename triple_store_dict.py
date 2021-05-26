import re

new_dic1 = {}
i = 0
# filename = "..." for example "watdiv1M_wo_dot.txt"
# The input text file should not contain '.', otherwise this will give errors. 
with open(filename) as doc:
    lines = doc.read()
    for line in re.split("\n", lines):
        for obj in re.split("\t", line):
            if(obj not in new_dic1):
                i = i + 1
                new_dic1[obj] = i
                
# For further queries contact me at sambhavshah284@gmail.com                
